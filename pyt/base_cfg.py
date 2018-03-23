import ast
import itertools

from .ast_helper import (
    get_call_names_as_string
)
from .base_cfg_helper import (
    CALL_IDENTIFIER,
    ConnectStatements,
    connect_nodes,
    extract_left_hand_side,
    get_first_node,
    get_first_statement,
    get_last_statements,
    remove_breaks
)
from .label_visitor import LabelVisitor
from .node_types import (
    AssignmentNode,
    AssignmentCallNode,
    BBorBInode,
    BreakNode,
    ControlFlowNode,
    IgnoredNode,
    Node,
    RestoreNode
)
from .right_hand_side_visitor import RHSVisitor
from .vars_visitor import VarsVisitor


class Visitor(ast.NodeVisitor):

    def visit_Module(self, node):
        return self.stmt_star_handler(node.body)

    def stmt_star_handler(
        self,
        stmts,
        prev_node_to_avoid=None
    ):
        """Handle stmt* expressions in an AST node.

        Links all statements together in a list of statements, accounting for statements with multiple last nodes.
        """
        break_nodes = list()
        cfg_statements = list()

        self.prev_nodes_to_avoid.append(prev_node_to_avoid)
        self.last_control_flow_nodes.append(None)

        first_node = None
        node_not_to_step_past = self.nodes[-1]

        for stmt in stmts:
            node = self.visit(stmt)

            if isinstance(node, ControlFlowNode) and node.test.label != 'Try':
                self.last_control_flow_nodes.append(node.test)
            else:
                self.last_control_flow_nodes.append(None)

            if isinstance(node, ControlFlowNode):
                break_nodes.extend(node.break_statements)
            elif isinstance(node, BreakNode):
                break_nodes.append(node)

            if not isinstance(node, IgnoredNode):
                cfg_statements.append(node)
                if not first_node:
                    if isinstance(node, ControlFlowNode):
                        first_node = node.test
                    else:
                        first_node = get_first_node(
                            node, 
                            node_not_to_step_past
                        )

        self.prev_nodes_to_avoid.pop()
        self.last_control_flow_nodes.pop()

        connect_nodes(cfg_statements)

        if cfg_statements:
            if first_node:
                first_statement = first_node
            else:
                first_statement = get_first_statement(cfg_statements[0])

            last_statements = get_last_statements(cfg_statements)

            return ConnectStatements(
                first_statement=first_statement,
                last_statements=last_statements,
                break_statements=break_nodes
            )
        else:  # When body of module only contains ignored nodes
            return IgnoredNode()


    def handle_or_else(self, orelse, test):
        """Handle the orelse part of an if or try node.

        Args:
            orelse(list[Node])
            test(Node)

        Returns:
            The last nodes of the orelse branch.
        """
        if isinstance(orelse[0], ast.If):
            control_flow_node = self.visit(orelse[0])
            control_flow_node.test.label = 'el' + control_flow_node.test.label

            test.connect(control_flow_node.test)
            return control_flow_node.last_nodes
        else:
            else_connect_statements = self.stmt_star_handler(
                orelse,
                prev_node_to_avoid=self.nodes[-1]
            )
            test.connect(else_connect_statements.first_statement)
            return else_connect_statements.last_statements

    def visit_If(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        test = self.append_node(Node(
            'if ' + label_visitor.result + ':',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

        body_connect_stmts = self.stmt_star_handler(node.body)
        if isinstance(body_connect_stmts, IgnoredNode):
            body_connect_stmts = ConnectStatements(
                first_statement=test,
                last_statements=[],
                break_statements=[]
            )
        test.connect(body_connect_stmts.first_statement)

        if node.orelse:
            orelse_last_nodes = self.handle_or_else(node.orelse, test)
            body_connect_stmts.last_statements.extend(orelse_last_nodes)
        else:
            body_connect_stmts.last_statements.append(test)  # if there is no orelse, test needs an edge to the next_node

        last_statements = remove_breaks(body_connect_stmts.last_statements)

        return ControlFlowNode(test, last_statements, break_statements=body_connect_stmts.break_statements)

    def visit_Raise(self, node):
        label = LabelVisitor()
        label.visit(node)

        return self.append_node(RaiseNode(
            label.result,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def handle_stmt_star_ignore_node(self, body, fallback_cfg_node):
        try:
            fallback_cfg_node.connect(body.first_statement)
        except AttributeError:
            body = ConnectStatements(
                first_statement=[fallback_cfg_node],
                last_statements=[fallback_cfg_node],
                break_statements=[]
            )
        return body

    def visit_Try(self, node):
        try_node = self.append_node(Node(
            'Try',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))
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

        last_statements.extend(remove_breaks(body.last_statements))

        return ControlFlowNode(try_node, last_statements, break_statements=body.break_statements)

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
                    extract_left_hand_side(target),
                    ast.Assign(target, value),
                    right_hand_side_variables,
                    line_number=node.lineno, path=self.filenames[-1]
                )))

        connect_nodes(new_assignment_nodes)
        return ControlFlowNode(new_assignment_nodes[0], [new_assignment_nodes[-1]], [])  # return the last added node

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

        connect_nodes(new_assignment_nodes)
        return ControlFlowNode(new_assignment_nodes[0], [new_assignment_nodes[-1]], [])  # return the last added node

    def visit_Assign(self, node):
        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node.value)
        if isinstance(node.targets[0], ast.Tuple):  #  x,y = [1,2]
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
                    extract_left_hand_side(node.targets[0]),
                    node,
                    rhs_visitor.result,
                    line_number=node.lineno,
                    path=self.filenames[-1]
                ))

    def assignment_call_node(self, left_hand_label, ast_node):
        """Handle assignments that contain a function call on its right side."""
        self.undecided = True  # Used for handling functions in assignments

        call = self.visit(ast_node.value)
        call_label = call.left_hand_side

        if isinstance(call, BBorBInode):
            # Necessary to know e.g.
            # `image_name = image_name.replace('..', '')`
            # is a reassignment.
            vars_visitor = VarsVisitor()
            vars_visitor.visit(ast_node.value)
            call.right_hand_side_variables.extend(vars_visitor.result)

        call_assignment = AssignmentCallNode(
            left_hand_label + ' = ' + call_label,
            left_hand_label,
            ast_node,
            [call.left_hand_side],
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
            extract_left_hand_side(node.target),
            node,
            rhs_visitor.result,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def loop_node_skeleton(self, test, node):
        """Common handling of looped structures, while and for."""
        body_connect_stmts = self.stmt_star_handler(
            node.body,
            prev_node_to_avoid=self.nodes[-1]
        )

        test.connect(body_connect_stmts.first_statement)
        test.connect_predecessors(body_connect_stmts.last_statements)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list()
        last_nodes.extend(body_connect_stmts.break_statements)

        if node.orelse:
            orelse_connect_stmts = self.stmt_star_handler(
                node.orelse,
                prev_node_to_avoid=self.nodes[-1]
            )

            test.connect(orelse_connect_stmts.first_statement)
            last_nodes.extend(orelse_connect_stmts.last_statements)
        else:
            last_nodes.append(test)  # if there is no orelse, test needs an edge to the next_node

        return ControlFlowNode(test, last_nodes, list())

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

    def visit_While(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        test = self.append_node(Node(
            'while ' + label_visitor.result + ':',
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

        return self.loop_node_skeleton(test, node)

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

        # Create e.g. ¤call_1 = ret_func_foo
        LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)
        RHS = 'ret_' + call_label.result[:index] + '('

        call_node = BBorBInode(
            label='',
            left_hand_side=LHS,
            right_hand_side_variables=[],
            line_number=node.lineno,
            path=self.filenames[-1],
            func_name=call_label.result[:index]
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
        # Used in get_sink_args, not using right_hand_side_variables because it is extended in assignment_call_node
        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node)
        call_node.args = rhs_visitor.result

        if blackbox:
            self.blackbox_assignments.add(call_node)

        self.connect_if_allowed(self.nodes[-1], call_node)
        self.nodes.append(call_node)

        return call_node

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
        return ControlFlowNode(
            with_node,
            connect_statements.last_statements,
            connect_statements.break_statements
        )

    def visit_Break(self, node):
        return self.append_node(BreakNode(
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
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Continue(self, node):
        return self.visit_miscelleaneous_node(
            node,
            custom_label='continue'
        )

    def visit_Global(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Name(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_NameConstant(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Pass(self, node):
        return self.visit_miscelleaneous_node(
            node,
            custom_label='pass'
        )

    def visit_Subscript(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Tuple(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_miscelleaneous_node(
        self,
        node,
        custom_label=None
    ):
        if custom_label:
            label = custom_label
        else:
            label_visitor = LabelVisitor()
            label_visitor.visit(node)
            label = label_visitor.result

        return self.append_node(Node(
            label,
            node,
            line_number=node.lineno,
            path=self.filenames[-1]
        ))

    def visit_Str(self, node):
        return IgnoredNode()

    def visit_Expr(self, node):
        return self.visit(node.value)

    def append_node(self, node):
        """Append a node to the CFG and return it."""
        self.nodes.append(node)
        return node
