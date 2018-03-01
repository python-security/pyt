import ast
import itertools
from collections import namedtuple

from .ast_helper import Arguments, get_call_names_as_string
from .label_visitor import LabelVisitor
from .right_hand_side_visitor import RHSVisitor
from .vars_visitor import VarsVisitor


ControlFlowNode = namedtuple('ControlFlowNode',
                             'test last_nodes break_statements')

ConnectStatements = namedtuple('ConnectStatements',
                               'first_statement' +
                               ' last_statements' +
                               ' break_statements')
CALL_IDENTIFIER = '¤'


class IgnoredNode():
    """Ignored Node sent from an ast node that should not return anything."""


class Node():
    """A Control Flow Graph node that contains a list of
    ingoing and outgoing nodes and a list of its variables."""

    def __init__(self, label, ast_node, *, line_number, path):
        """Create a Node that can be used in a CFG.

        Args:
            label(str): The label of the node, describing its expression.
            line_number(Optional[int]): The line of the expression of the Node.
        """
        self.label = label
        self.ast_node = ast_node
        self.line_number = line_number
        self.path = path
        self.ingoing = list()
        self.outgoing = list()

    def connect(self, successor):
        """Connect this node to its successor node by
        setting its outgoing and the successors ingoing."""
        if isinstance(self, ConnectToExitNode) and\
           not isinstance(successor, EntryOrExitNode):
            return

        self.outgoing.append(successor)
        successor.ingoing.append(self)

    def connect_predecessors(self, predecessors):
        """Connect all nodes in predecessors to this node."""
        for n in predecessors:
            self.ingoing.append(n)
            n.outgoing.append(self)

    def __str__(self):
        """Print the label of the node."""
        return ''.join((' Label: ', self.label))


    def __repr__(self):
        """Print a representation of the node."""
        label = ' '.join(('Label: ', self.label))
        line_number = 'Line number: ' + str(self.line_number)
        outgoing = ''
        ingoing = ''
        if self.ingoing:
            ingoing = ' '.join(('ingoing:\t', str([x.label for x in self.ingoing])))
        else:
            ingoing = ' '.join(('ingoing:\t', '[]'))

        if self.outgoing:
            outgoing = ' '.join(('outgoing:\t', str([x.label for x in self.outgoing])))
        else:
            outgoing = ' '.join(('outgoing:\t', '[]'))

        return '\n' + '\n'.join((label, line_number, ingoing, outgoing))


class ConnectToExitNode():
    pass


class FunctionNode(Node):
    """CFG Node that represents a function definition.

    Used as a dummy for creating a list of function definitions.
    """

    def __init__(self, ast_node):
        """Create a function node.

        This node is a dummy node representing a function definition.
        """
        super().__init__(self.__class__.__name__, ast_node)


class RaiseNode(Node, ConnectToExitNode):
    """CFG Node that represents a Raise statement."""

    def __init__(self, label, ast_node, *, line_number, path):
        """Create a Raise node."""
        super().__init__(label, ast_node, line_number=line_number, path=path)


class BreakNode(Node):
    """CFG Node that represents a Break node."""

    def __init__(self, ast_node, *, line_number, path):
        super().__init__(self.__class__.__name__, ast_node, line_number=line_number, path=path)


class EntryOrExitNode(Node):
    """CFG Node that represents an Exit or an Entry node."""

    def __init__(self, label):
        super().__init__(label, None, line_number=None, path=None)


class AssignmentNode(Node):
    """CFG Node that represents an assignment."""

    def __init__(self, label, left_hand_side, ast_node, right_hand_side_variables, *, line_number, path):
        """Create an Assignment node.

        Args:
            label(str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            ast_node(_ast.Assign, _ast.AugAssign, _ast.Return or None)
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
            path(string): Current filename.
        """
        super().__init__(label, ast_node, line_number=line_number, path=path)
        self.left_hand_side = left_hand_side
        self.right_hand_side_variables = right_hand_side_variables

    def __repr__(self):
        output_string = super().__repr__()
        output_string += '\n'
        return ''.join((output_string,
                        'left_hand_side:\t', str(self.left_hand_side), '\n',
                        'right_hand_side_variables:\t', str(self.right_hand_side_variables)))


class TaintedNode(AssignmentNode):
    pass


class RestoreNode(AssignmentNode):
    """Node used for handling restore nodes returning from function calls."""

    def __init__(self, label, left_hand_side, right_hand_side_variables, *, line_number, path):
        """Create a Restore node.

        Args:
            label(str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
            path(string): Current filename.
        """
        super().__init__(label, left_hand_side, None, right_hand_side_variables, line_number=line_number, path=path)


class BBorBInode(AssignmentNode):
    """Node used for handling restore nodes returning from blackbox or builtin function calls."""

    def __init__(self, label, left_hand_side, right_hand_side_variables, *, line_number, path):
        """Create a Restore node.

        Args:
            label(str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
            path(string): Current filename.
        """
        super().__init__(label, left_hand_side, None, right_hand_side_variables, line_number=line_number, path=path)
        self.args = list()
        self.inner_most_call = self


class AssignmentCallNode(AssignmentNode):
    """Node used for X."""

    def __init__(self,
                 label,
                 left_hand_side,
                 ast_node,
                 right_hand_side_variables,
                 vv_result,
                 *,
                 line_number,
                 path,
                 call_node):
        """Create a X.

        Args:
            label(str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            vv_result(list[str]): Necessary to know `image_name = image_name.replace('..', '')` is a reassignment.
            line_number(Optional[int]): The line of the expression the Node represents.
            path(string): Current filename.
            call_node(BBorBInode or RestoreNode): Used in connect_control_flow_node.
        """
        super().__init__(label, left_hand_side, ast_node, right_hand_side_variables, line_number=line_number, path=path)
        self.vv_result = vv_result
        self.call_node = call_node
        self.blackbox = False


class ReturnNode(AssignmentNode, ConnectToExitNode):
    """CFG node that represents a return from a call."""

    def __init__(self, label, left_hand_side, ast_node, right_hand_side_variables, *, line_number, path):
        """Create a CallReturn node.

        Args:
            label(str): The label of the node, describing the expression it represents.
            restore_nodes(list[Node]): List of nodes that were restored in the function call.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
            path(string): Current filename.
        """
        super().__init__(label, left_hand_side, ast_node, right_hand_side_variables, line_number=line_number, path=path)


class Function():
    """Representation of a function definition in the program."""

    def __init__(self, nodes, args, decorator_list):
        """Create a Function representation.

        Args:
            nodes(list[Node]): The CFG of the Function.
            args(ast.args): The arguments from a function AST node.
            decorator_list(list[ast.decorator]): The list of decorators
            from a function AST node.
        """
        self.nodes = nodes
        self.arguments = Arguments(args)
        self.decorator_list = decorator_list

    def __repr__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + repr(n), '\n\n'))
        return output

    def __str__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + str(n), '\n\n'))
        return output


class CFG():
    def __init__(self, nodes, blackbox_assignments):
        self.nodes = nodes
        self.blackbox_assignments = blackbox_assignments

    def __repr__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + repr(n), '\n\n'))
        return output

    def __str__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + str(n), '\n\n'))
        return output


class Visitor(ast.NodeVisitor):

    def append_node(self, Node):
        """Append a node to the CFG and return it."""
        self.nodes.append(Node)
        return Node

    def get_first_statement(self, node_or_tuple):
        """Find the first statement of the provided object.

        Returns:
            The first element in the tuple if it is a tuple.
            The node if it is a node.
        """
        if isinstance(node_or_tuple, tuple):
            return node_or_tuple[0]
        else:
            return node_or_tuple

    def should_connect_node(self, node):
        """Determine if node should be in the final CFG."""
        if isinstance(node, (FunctionNode, IgnoredNode)):
            return False
        else:
            return True

    def get_inner_most_function_call(self, call_node):
        # Loop to inner most function call
        # e.g. return scrypt.inner in `foo = scrypt.outer(scrypt.inner(image_name))`
        old_call_node = None
        while call_node != old_call_node:
            old_call_node = call_node
            if isinstance(call_node, BBorBInode):
                call_node = call_node.inner_most_call
            else:
                try:
                    call_node = call_node.first_node.inner_most_call
                except AttributeError:
                    try:
                        call_node = call_node.first_node
                    except AttributeError:
                        # No inner calls
                        # Possible improvement: Make new node for RestoreNode's made in process_function
                        #                       and make `self.inner_most_call = self`
                        pass
        return call_node

    def connect_control_flow_node(self, control_flow_node, next_node):
        """Connect a ControlFlowNode properly to the next_node."""
        for last in control_flow_node[1]:  # list of last nodes in ifs and elifs
            if isinstance(next_node, ControlFlowNode):
                last.connect(next_node.test)  # connect to next if test case
            elif isinstance(next_node, AssignmentCallNode):
                call_node = next_node.call_node
                inner_most_call_node = self.get_inner_most_function_call(call_node)
                last.connect(inner_most_call_node)
            else:
                last.connect(next_node)

    def connect_nodes(self, nodes):
        """Connect the nodes in a list linearly."""
        for n, next_node in zip(nodes, nodes[1:]):
            if isinstance(n, ControlFlowNode):  # case for if
                self.connect_control_flow_node(n, next_node)
            elif isinstance(next_node, ControlFlowNode):  # case for if
                n.connect(next_node[0])
            elif isinstance(next_node, RestoreNode):
                continue
            elif CALL_IDENTIFIER in next_node.label:
                continue
            else:
                n.connect(next_node)

    def get_last_statements(self, cfg_statements):
        """Retrieve the last statements from a cfg_statements list."""
        if isinstance(cfg_statements[-1], ControlFlowNode):
            return cfg_statements[-1].last_nodes
        else:
            return [cfg_statements[-1]]

    def stmt_star_handler(self, stmts, prev_node_to_avoid=None):
        """Handle stmt* expressions in an AST node.

        Links all statements together in a list of statements, accounting for statements with multiple last nodes.
        """
        break_nodes = list()
        cfg_statements = list()

        if prev_node_to_avoid:
            self.prev_nodes_to_avoid.append(prev_node_to_avoid)

        first_node = None
        node_not_to_step_past = self.nodes[-1]

        for stmt in stmts:
            node = self.visit(stmt)
            if isinstance(stmt, ast.While) or isinstance(stmt, ast.For):
                self.last_was_loop_stack.append(True)
            else:
                self.last_was_loop_stack.append(False)

            if isinstance(node, ControlFlowNode):
                break_nodes.extend(node.break_statements)
            elif isinstance(node, BreakNode):
                break_nodes.append(node)

            if node and not first_node: # (Make sure first_node isn't already set.)
                # first_node is always a "node_to_connect", because it won't have ingoing otherwise
                # If we have e.g.
                #   import os # An ignored node
                #   value = None
                # first_node will be `value = None`
                if hasattr(node, 'ingoing'):
                    ingoing = None
                    current_node = node
                    while current_node.ingoing:
                        # e.g. We don't want to step past the Except of an Except BB
                        if current_node.ingoing[0] == node_not_to_step_past:
                            break
                        ingoing = current_node.ingoing
                        current_node = current_node.ingoing[0]
                    if ingoing:
                        # Only set it once
                        first_node = ingoing[0]

            if node and self.should_connect_node(node):
                if not first_node:
                    if isinstance(node, ControlFlowNode):
                        first_node = node.test
                    else:
                        first_node = node
                cfg_statements.append(node)
        if prev_node_to_avoid:
            self.prev_nodes_to_avoid.pop()
        self.last_was_loop_stack.pop()

        self.connect_nodes(cfg_statements)

        if cfg_statements:
            if first_node:
                first_statement = first_node
            else:
                first_statement = self.get_first_statement(cfg_statements[0])

            last_statements = self.get_last_statements(cfg_statements)

            return ConnectStatements(first_statement=first_statement,
                                     last_statements=last_statements,
                                     break_statements=break_nodes)
        else:  # When body of module only contains ignored nodes
            return IgnoredNode()

    def visit_Module(self, node):
        return self.stmt_star_handler(node.body)

    def add_if_label(self, CFG_node):
        """Prepend 'if ' and append ':' to the label of a Node."""
        CFG_node.label = 'if ' + CFG_node.label + ':'

    def add_elif_label(self, CFG_node):
        """Add the el to an already add_if_label'ed Node."""
        CFG_node.label = 'el' + CFG_node.label

    def handle_or_else(self, orelse, test):
        """Handle the orelse part of an if or try node.

        Returns:
            The last nodes of the orelse branch.
        """
        if isinstance(orelse[0], ast.If):
            control_flow_node = self.visit(orelse[0])
            self.add_elif_label(control_flow_node.test)
            test.connect(control_flow_node.test)
            return control_flow_node.last_nodes
        else:
            else_connect_statements = self.stmt_star_handler(orelse, prev_node_to_avoid=self.nodes[-1])
            test.connect(else_connect_statements.first_statement)
            return else_connect_statements.last_statements

    def remove_breaks(self, last_statements):
        """Remove all break statements in last_statements."""
        return [n for n in last_statements if not isinstance(n, BreakNode)]

    def visit_If(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        test = self.append_node(Node(label_visitor.result, node, line_number=node.lineno, path=self.filenames[-1]))

        self.add_if_label(test)

        body_connect_stmts = self.stmt_star_handler(node.body)
        if isinstance(body_connect_stmts, IgnoredNode):
            body_connect_stmts = ConnectStatements(first_statement=test, last_statements=[], break_statements=[])
        test.connect(body_connect_stmts.first_statement)

        if node.orelse:
            orelse_last_nodes = self.handle_or_else(node.orelse, test)
            body_connect_stmts.last_statements.extend(orelse_last_nodes)
        else:
            body_connect_stmts.last_statements.append(test) # if there is no orelse, test needs an edge to the next_node

        last_statements = self.remove_breaks(body_connect_stmts.last_statements)

        return ControlFlowNode(test, last_statements, break_statements=body_connect_stmts.break_statements)

    def visit_NameConstant(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)
        return self.append_node(Node(label_visitor.result, node, line_number=node.lineno, path=self.filenames[-1]))

    def visit_Raise(self, node):
        label = LabelVisitor()
        label.visit(node)

        return self.append_node(RaiseNode(label.result, node, line_number=node.lineno, path=self.filenames[-1]))

    def handle_stmt_star_ignore_node(self, body, fallback_cfg_node):
        try:
            fallback_cfg_node.connect(body.first_statement)
        except AttributeError:
            body = ConnectStatements([fallback_cfg_node], [fallback_cfg_node], list())
        return body

    def visit_Try(self, node):
        try_node = self.append_node(Node('Try', node, line_number=node.lineno, path=self.filenames[-1]))
        body = self.stmt_star_handler(node.body)
        body = self.handle_stmt_star_ignore_node(body, try_node)

        last_statements = list()
        for handler in node.handlers:
            try:
                name = handler.type.id
            except AttributeError:
                name = ''
            handler_node = self.append_node(Node(
                'except ' + name + ':',
                handler,
                line_number=handler.lineno,
                path=self.filenames[-1]
            ))
            for body_node in body.last_statements:
                body_node.connect(handler_node)
            handler_body = self.stmt_star_handler(handler.body)
            handler_body = self.handle_stmt_star_ignore_node(handler_body, handler_node)
            last_statements.extend(handler_body.last_statements)

        if node.orelse:
            orelse_last_nodes = self.handle_or_else(node.orelse, body.last_statements[-1])
            body.last_statements.extend(orelse_last_nodes)

        if node.finalbody:
            finalbody = self.stmt_star_handler(node.finalbody)
            for last in last_statements:
                last.connect(finalbody.first_statement)

            for last in body.last_statements:
                last.connect(finalbody.first_statement)

            body.last_statements.extend(finalbody.last_statements)

        last_statements.extend(self.remove_breaks(body.last_statements))

        return ControlFlowNode(try_node, last_statements, break_statements=body.break_statements)

    def get_names(self, node, result):
        """Recursively finds all names."""
        if isinstance(node, ast.Name):
            return node.id + result
        elif isinstance(node, ast.Subscript):
            return result
        else:
            return self.get_names(node.value, result + '.' + node.attr)

    def extract_left_hand_side(self, target):
        """Extract the left hand side variable from a target.

        Removes list indexes, stars and other left hand side elements.
        """
        left_hand_side = self.get_names(target, '')

        left_hand_side.replace('*', '')
        if '[' in left_hand_side:
            index = left_hand_side.index('[')
            left_hand_side = target[0:index]

        return left_hand_side

    def assign_tuple_target(self, node, right_hand_side_variables):
        new_assignment_nodes = list()
        for i, target in enumerate(node.targets[0].elts):
            value = node.value.elts[i]

            label = LabelVisitor()
            label.visit(target)

            if isinstance(value, ast.Call):
                new_ast_node = ast.Assign(target, value)
                new_ast_node.lineno = node.lineno

                new_assignment_nodes.append(self.assignment_call_node(label.result, new_ast_node))

            else:
                label.result += ' = '
                label.visit(value)

                new_assignment_nodes.append(self.append_node(AssignmentNode(
                    label.result,
                    self.extract_left_hand_side(target),
                    ast.Assign(target, value),
                    right_hand_side_variables,
                    line_number=node.lineno, path=self.filenames[-1]
                )))


        self.connect_nodes(new_assignment_nodes)
        return ControlFlowNode(new_assignment_nodes[0], [new_assignment_nodes[-1]], []) # return the last added node

    def assign_multi_target(self, node, right_hand_side_variables):
        new_assignment_nodes = list()

        for target in node.targets:
            label = LabelVisitor()
            label.visit(target)
            left_hand_side = label.result
            label.result += ' = '
            label.visit(node.value)
            new_assignment_nodes.append(self.append_node(AssignmentNode(
                label.result,
                left_hand_side,
                ast.Assign(target, node.value),
                right_hand_side_variables,
                line_number=node.lineno, path=self.filenames[-1]
            )))

        self.connect_nodes(new_assignment_nodes)
        return ControlFlowNode(new_assignment_nodes[0], [new_assignment_nodes[-1]], []) # return the last added node

    def visit_Assign(self, node):
        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node.value)
        if isinstance(node.targets[0], ast.Tuple): #  x,y = [1,2]
            if isinstance(node.value, ast.Tuple):
                return self.assign_tuple_target(node, rhs_visitor.result)
            elif isinstance(node.value, ast.Call):
                call = None
                for element in node.targets[0].elts:
                    label = LabelVisitor()
                    label.visit(element)
                    call = self.assignment_call_node(label.result, node)
                return call
            else:
                label = LabelVisitor()
                label.visit(node)
                print('Assignment not properly handled.',
                      'Could result in not finding a vulnerability.',
                      'Assignment:', label.result)
                return self.append_node(AssignmentNode(
                    label.result,
                    label.result,
                    node,
                    rhs_visitor.result,
                    line_number=node.lineno,
                    path=self.filenames[-1]
                ))

        elif len(node.targets) > 1:                #  x = y = 3
            return self.assign_multi_target(node, rhs_visitor.result)
        else:
            if isinstance(node.value, ast.Call):   #  x = call()
                label = LabelVisitor()
                label.visit(node.targets[0])
                return self.assignment_call_node(label.result, node)
            else:                                  #  x = 4
                label = LabelVisitor()
                label.visit(node)
                return self.append_node(AssignmentNode(
                    label.result,
                    self.extract_left_hand_side(node.targets[0]),
                    node,
                    rhs_visitor.result,
                    line_number=node.lineno,
                    path=self.filenames[-1]
                ))

    def assignment_call_node(self, left_hand_label, ast_node):
        """Handle assignments that contain a function call on its right side."""
        self.undecided = True # Used for handling functions in assignments

        call = self.visit(ast_node.value)
        call_label = ''
        call_assignment = None

        # Necessary to know `image_name = image_name.replace('..', '')` is a reassignment.
        vars_visitor = VarsVisitor()
        vars_visitor.visit(ast_node.value)

        call_label = call.left_hand_side
        if isinstance(call, BBorBInode):
            call_assignment = AssignmentCallNode(
                left_hand_label + ' = ' + call_label,
                left_hand_label,
                ast_node,
                [call.left_hand_side],
                vv_result=vars_visitor.result,
                line_number=ast_node.lineno,
                path=self.filenames[-1],
                call_node=call
            )
        # Assignment after returned user-defined function call e.g. RestoreNode ¤call_1 = ret_outer
        elif isinstance(call, AssignmentNode):
            call_assignment = AssignmentCallNode(
                left_hand_label + ' = ' + call_label,
                left_hand_label,
                ast_node,
                [call.left_hand_side],
                vv_result=[],
                line_number=ast_node.lineno,
                path=self.filenames[-1],
                call_node=call
            )
        call.connect(call_assignment)

        self.nodes.append(call_assignment)
        self.undecided = False

        return call_assignment

    def visit_AugAssign(self, node):
        label = LabelVisitor()
        label.visit(node)

        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node.value)

        return self.append_node(AssignmentNode(
            label.result,
            self.extract_left_hand_side(node.target),
            node,
            rhs_visitor.result,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def loop_node_skeleton(self, test, node):
        """Common handling of looped structures, while and for."""
        body_connect_stmts = self.stmt_star_handler(node.body, prev_node_to_avoid=self.nodes[-1])

        test.connect(body_connect_stmts.first_statement)
        test.connect_predecessors(body_connect_stmts.last_statements)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list()
        last_nodes.extend(body_connect_stmts.break_statements)

        if node.orelse:
            orelse_connect_stmts = self.stmt_star_handler(node.orelse, prev_node_to_avoid=self.nodes[-1])

            test.connect(orelse_connect_stmts.first_statement)
            last_nodes.extend(orelse_connect_stmts.last_statements)
        else:
            last_nodes.append(test)  # if there is no orelse, test needs an edge to the next_node

        return ControlFlowNode(test, last_nodes, list())

    def add_while_label(self, node):
        """Prepend 'while' and append ':' to the label of a node."""
        node.label = 'while ' + node.label + ':'

    def visit_While(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        test = self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

        self.add_while_label(test)

        return self.loop_node_skeleton(test, node)

    def visit_For(self, node):
        self.undecided = True  # Used for handling functions in for loops

        iterator_label = LabelVisitor()
        iterator = iterator_label.visit(node.iter)
        self.undecided = False

        target_label = LabelVisitor()
        target = target_label.visit(node.target)

        for_node = self.append_node(Node(
            "for " + target_label.result + " in " + iterator_label.result + ':',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

        if isinstance(node.iter, ast.Call) and get_call_names_as_string(node.iter.func) in self.function_names:
            last_node = self.visit(node.iter)
            last_node.connect(for_node)

        return self.loop_node_skeleton(for_node, node)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def add_blackbox_or_builtin_call(self, node, blackbox):
        """Processes a blackbox or builtin function when it is called.
        Nothing gets assigned to ret_func_foo in the builtin/blackbox case.

        Increments self.function_call_index each time it is called, we can refer to it as N in the comments.
        Create e.g. ¤call_1 = ret_func_foo RestoreNode.

        Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument.
        Visit the arguments if they're calls. (save_def_args_in_temp)

        I do not think I care about this one actually -- Create e.g. def_arg1 = temp_N_def_arg1 for each argument.
        (create_local_scope_from_def_args)

        Add RestoreNode to the end of the Nodes.

        Args:
            node(ast.Call) : The node that calls the definition.
            blackbox(bool): Whether or not it is a builtin or blackbox call.
        Returns:
            call_node(BBorBInode): The call node.
        """
        # Increment function_call_index
        self.function_call_index += 1
        saved_function_call_index = self.function_call_index
        self.undecided = False

        call_label = LabelVisitor()
        call_label.visit(node)

        index = call_label.result.find('(')
        if index == -1:
            print("No ( in a call")
            raise

        # Create e.g. ¤call_1 = ret_func_foo
        LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)
        RHS = 'ret_' + call_label.result[:index] + '('

        call_node = BBorBInode(
            label="",
            left_hand_side=LHS,
            right_hand_side_variables=[],
            line_number=node.lineno,
            path=self.filenames[-1]
        )
        visual_args = list()
        rhs_vars = list()
        last_return_value_of_nested_call = None

        for arg in itertools.chain(node.args, node.keywords):
            if isinstance(arg, ast.Call):
                return_value_of_nested_call = self.visit(arg)

                if last_return_value_of_nested_call:
                    # connect inner to other_inner in e.g.
                    # `scrypt.outer(scrypt.inner(image_name), scrypt.other_inner(image_name))`
                    # I should probably loop to the inner most call of other_inner here.
                    try:
                        last_return_value_of_nested_call.connect(return_value_of_nested_call.first_node)
                    except AttributeError:
                        last_return_value_of_nested_call.connect(return_value_of_nested_call)
                else:
                    # I should only set this once per loop, inner in e.g.
                    # `scrypt.outer(scrypt.inner(image_name), scrypt.other_inner(image_name))`
                    # (inner_most_call is used when predecessor is a ControlFlowNode in connect_control_flow_node)
                    call_node.inner_most_call = return_value_of_nested_call
                last_return_value_of_nested_call = return_value_of_nested_call

                visual_args.append(return_value_of_nested_call.left_hand_side)
                rhs_vars.append(return_value_of_nested_call.left_hand_side)
            else:
                label = LabelVisitor()
                label.visit(arg)
                visual_args.append(label.result)

                vv = VarsVisitor()
                vv.visit(arg)
                rhs_vars.extend(vv.result)
        if last_return_value_of_nested_call:
            # connect other_inner to outer in e.g.
            # `scrypt.outer(scrypt.inner(image_name), scrypt.other_inner(image_name))`
            last_return_value_of_nested_call.connect(call_node)

        if len(visual_args) > 0:
            for arg in visual_args:
                RHS = RHS + arg + ", "
            # Replace the last ", " with a )
            RHS = RHS[:len(RHS)-2] + ')'
        else:
            RHS = RHS + ')'
        call_node.label = LHS + " = " + RHS

        call_node.right_hand_side_variables = rhs_vars
        # Used in get_sink_args
        call_node.args = rhs_vars

        if blackbox:
            self.blackbox_assignments.add(call_node)

        self.connect_if_allowed(self.nodes[-1], call_node)
        self.nodes.append(call_node)

        return call_node

    def visit_Name(self, node):
        label = LabelVisitor()
        label.visit(node)

        return self.append_node(Node(label.result, node, line_number=node.lineno, path=self.filenames[-1]))

    def visit_With(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.items[0])

        with_node = self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))
        connect_statements = self.stmt_star_handler(node.body)
        with_node.connect(connect_statements.first_statement)
        return ControlFlowNode(with_node, connect_statements.last_statements, connect_statements.break_statements)

    def visit_Str(self, node):
        return IgnoredNode()

    def visit_Break(self, node):
        return self.append_node(BreakNode(node, line_number=node.lineno, path=self.filenames[-1]))

    def visit_Pass(self, node):
        return self.append_node(Node(
            'pass',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Continue(self, node):
        return self.append_node(Node(
            'continue',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Delete(self, node):
        labelVisitor = LabelVisitor()
        for expr in node.targets:
            labelVisitor.visit(expr)
        return self.append_node(Node(
            'del ' + labelVisitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Assert(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        return self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Attribute(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)

        return self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Global(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)

        return self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Subscript(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)

        return self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Tuple(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)

        return self.append_node(Node(
            label_visitor.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))
