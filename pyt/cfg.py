"""This module contains classes for generating a Control Flow Graph of a python program.

The class CFG is the main entry point to this module
The method generate_ast(path) can the used to generate input for the CFG class' create method
"""

import ast
import os
from collections import namedtuple, OrderedDict
from copy import deepcopy
import logging

from label_visitor import LabelVisitor
from right_hand_side_visitor import RHSVisitor
from module_definitions import ModuleDefinition, ModuleDefinitions, LocalModuleDefinition
from project_handler import get_directory_modules
from ast_helper import generate_ast, get_call_names_as_string

CALL_IDENTIFIER = '¤'
ControlFlowNode = namedtuple('ControlFlowNode', 'test last_nodes break_statements')
SavedVariable = namedtuple('SavedVariable', 'LHS RHS')
ConnectStatements = namedtuple('ConnectStatements', 'first_statement last_statements break_statements')
logger = logging.getLogger(__name__)


class IgnoredNode(object):
    """Ignored Node sent from a ast node that is not yet implemented."""


class Node(object):
    """A Control Flow Graph node that contains a list of ingoing and outgoing nodes and a list of its variables."""
    
    def __init__(self, label, ast_node, *, line_number=None):
        """Create a Node that can be used in a CFG.

        Args:
            label (str): The label of the node, describing the expression it represents.
            line_number(Optional[int]): The line of the expression the Node represents.
        """
        self.ingoing = list()
        self.outgoing = list()

        self.label = label
        self.ast_node = ast_node
        self.line_number = line_number

        # Used by the Fixedpoint algorithm
        self.old_constraint = set()
        self.new_constraint = set()

    def connect(self, successor):
        """Connect this node to its successor node by setting its outgoing and the successors ingoing."""
        if isinstance(self, ConnectToExitNode) and not type(successor) is EntryExitNode:
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
        return ' '.join(('Label: ', self.label))

    def __repr__(self):
        """Print a representation of the node."""
        label = ' '.join(('Label: ', self.label))
        line_number = 'Line number: ' + str(self.line_number)
        outgoing = ''
        ingoing = ''
        if self.ingoing is not  None:
            ingoing = ' '.join(('ingoing:\t', str([x.label for x in self.ingoing])))
        else:
            ingoing = ' '.join(('ingoing:\t', '[]'))

        if self.outgoing is not None:
            outgoing = ' '.join(('outgoing:\t', str([x.label for x in self.outgoing])))
        else:
            outgoing = ' '.join(('outgoing:\t', '[]'))
    
        if self.old_constraint is not None:
            old_constraint = 'Old constraint:\t ' + ', '.join([x.label for x in self.old_constraint])
        else:
            old_constraint = 'Old constraint:\t '

        if self.new_constraint is not None:
            new_constraint = 'New constraint: ' +  ', '.join([x.label for x in self.new_constraint])
        else:
            new_constraint = 'New constraint:'
        return '\n' + '\n'.join((label, line_number, ingoing, outgoing, old_constraint, new_constraint))


class ConnectToExitNode():
    pass


class FunctionNode(Node):
    """CFG Node that represents a function definition.
    
    Used as a dummy for creating a list of function definitions.    
    """
    
    def __init__(self, ast_node):
        """Create a function node.
        
        This node is a dummy node representing a function definition
        """
        super(FunctionNode, self).__init__(self.__class__.__name__, ast_node)


class RaiseNode(Node, ConnectToExitNode):
    """CFG Node that represents a Raise statement."""
    
    def __init__(self, ast_node, *, line_number=None):
        """Create a Raise node."""
        super(RaiseNode, self).__init__(self.__class__.__name__, ast_node, line_number=line_number)


class BreakNode(Node):
    """CFG Node that represents a Break node."""
    
    def __init__(self, ast_node, *, line_number=None):
        super(BreakNode, self).__init__(self.__class__.__name__, ast_node, line_number=line_number)


class EntryExitNode(Node):
    """CFG Node that represents a Exit or an Entry node."""
    
    def __init__(self, label):
        super(EntryExitNode, self).__init__(label, None)

        
class AssignmentNode(Node):
    """CFG Node that represents an assignment."""
    
    def __init__(self, label, left_hand_side, ast_node, right_hand_side_variables, *, line_number=None):
        """Create an Assignment node.

        Args:
            label (str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
        """
        super(AssignmentNode, self).__init__(label, ast_node, line_number=line_number)
        self.left_hand_side = left_hand_side
        self.right_hand_side_variables = right_hand_side_variables

    def __repr__(self):
        output_string = super(AssignmentNode, self).__repr__()
        output_string += '\n'
        return ''.join((output_string, 'left_hand_side:\t', str(self.left_hand_side), '\n', 'right_hand_side_variables:\t', str(self.right_hand_side_variables)))


class RestoreNode(AssignmentNode):
    """Node used for handling restore nodes returning from function calls."""

    def __init__(self, label, left_hand_side, right_hand_side_variables, *, line_number=None):
        """Create an Restore node.

        Args:
            label (str): The label of the node, describing the expression it represents.
            left_hand_side(str): The variable on the left hand side of the assignment. Used for analysis.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
        """
        super(RestoreNode, self).__init__(label, left_hand_side, None, right_hand_side_variables, line_number=line_number)
        

class ReturnNode(AssignmentNode, ConnectToExitNode):
    """CFG node that represents a return from a call."""
    
    def __init__(self, label, left_hand_side, right_hand_side_variables, *, line_number=None):
        """Create an CallReturn node.

        Args:
            label (str): The label of the node, describing the expression it represents.
            restore_nodes(list[Node]): List of nodes that where restored in the function call.
            right_hand_side_variables(list[str]): A list of variables on the right hand side.
            line_number(Optional[int]): The line of the expression the Node represents.
        """
        super(ReturnNode, self).__init__(label, left_hand_side, None, right_hand_side_variables, line_number=line_number)    

class Arguments(object):
    """Represents arguments of a function."""
    
    def __init__(self, args):
        """Create an Argument container class.

        Args:
            args(list(ast.args): The arguments in a function AST node.
        """
        self.args = args.args
        self.varargs = args.vararg
        self.kwarg = args.kwarg
        self.kwonlyargs = args.kwonlyargs
        self.defaults = args.defaults
        self.kw_defaults = args.kw_defaults

        self.arguments = list()
        if self.args:
            self.arguments.extend([x.arg for x in self.args])
        if self.varargs:
            self.arguments.extend(self.varargs.arg)
        if self.kwarg:
            self.arguments.extend(self.kwarg.arg)
        if self.kwonlyargs:
            self.arguments.extend([x.arg for x in self.kwonlyargs])

    def __getitem__(self, key):
        return self.arguments.__getitem__(key)
        
    
class Function(object):
    """Representation of a function definition in the program."""
    
    def __init__(self, nodes, args, decorator_list):
        """Create a Function representation.

        Args:
            nodes(list[Node]): The CFG of the Function.
            args(ast.args): The arguments from a function AST node.
            decorator_list(list[ast.decorator]): The list of decorators from a function AST node.
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
    

class CFG(ast.NodeVisitor):
    """A Control Flow Graph containing a list of nodes."""
    
    def __init__(self, project_modules, local_modules):
        """Create an empty CFG."""
        self.nodes = list()
        self.function_index = 0
        self.undecided = False
        self.project_modules = project_modules
        self.local_modules = local_modules
        self.function_names = list()
        self.module_definitions_stack = list()

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

    def append_node(self, Node):
        """Append a node to the CFG and return it."""
        self.nodes.append(Node)
        return Node
        
    def create(self, module_node):
        """Create a Control Flow Graph.

        Args:
            module_node(ast.Module) is the first node (Module) of an Abstract Syntax Tree generated with the module_node module.
        """
        self.module_definitions_stack.append(ModuleDefinitions())
        
        entry_node = self.append_node(EntryExitNode("Entry module"))
                
        module_statements = self.visit(module_node)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty, there is nothing to analyse.')
        
        if not isinstance(module_statements, IgnoredNode):
            first_node = module_statements.first_statement

            if not CALL_IDENTIFIER in first_node.label:
                entry_node.connect(first_node)

            exit_node = self.append_node(EntryExitNode("Exit module"))
        
            last_nodes = module_statements.last_statements
            exit_node.connect_predecessors(last_nodes)
        else:
            exit_node = self.append_node(EntryExitNode("Exit module"))    
            entry_node.connect(exit_node)

    def create_function(self, function_node):
        """Create a Control Flow Graph for at separate function

        Args:
            function_node: is the node to create a CFG of
        """
        self.module_definitions_stack.append(ModuleDefinitions())
        
        self.function_names.append(function_node.name)
        
        entry_node = self.append_node(EntryExitNode("Entry module"))
                
        module_statements = self.stmt_star_handler(function_node.body)

        first_node = module_statements.first_statement
        
        if not CALL_IDENTIFIER in first_node.label:
            entry_node.connect(first_node)

        exit_node = self.append_node(EntryExitNode("Exit module"))
        
        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)
            
    def get_first_statement(self, node_or_tuple):
        """Find the first statement of the provided object.

        Returns:
            The node if is is a node.
            The first element in the tuple if it is a tuple.
        """
        if isinstance(node_or_tuple, tuple):
            return node_or_tuple[0]
        else:
            return node_or_tuple

    def node_to_connect(self, node):
        """Determine if node should be in the final CFG."""
        if isinstance(node, IgnoredNode):
            return False
        elif isinstance(node, ControlFlowNode):
            return True
        elif type(node) is FunctionNode:
            return False
        else:
            return True

    def connect_control_flow_node(self, control_flow_node, next_node):
        """Connect a ControlFlowNode properly to the next_node."""
        for last in control_flow_node[1]:                         # list of last nodes in ifs and elifs
            if isinstance(next_node, ControlFlowNode):
                last.connect(next_node.test)        # connect to next if test case
            else:
                last.connect(next_node)        

    def connect_nodes(self, nodes):
        """Connect the nodes in a list linearly."""
        for n, next_node in zip(nodes, nodes[1:]):
            if isinstance(n, ControlFlowNode):             # case for if
                self.connect_control_flow_node(n, next_node)
            elif isinstance(next_node, ControlFlowNode):  # case for if
                n.connect(next_node[0])
            elif type(next_node) is RestoreNode:
                continue
            elif CALL_IDENTIFIER in next_node.label:
                continue
            else:
                n.connect(next_node)

    def get_last_statements(self, cfg_statements):
        """Retrieve the last statements from a cfg_statments list."""
        if isinstance(cfg_statements[-1], ControlFlowNode):
            return cfg_statements[-1].last_nodes
        else:
            return [cfg_statements[-1]]

    def stmt_star_handler(self, stmts):
        """Handle stmt* expressions in an AST node.

        Links all statements together in a list of statements, accounting for statements with multiple last nodes
        """
        cfg_statements = list()
        break_nodes = list()

        for stmt in stmts:
            node = self.visit(stmt)

            if isinstance(node, ControlFlowNode):
                break_nodes.extend(node.break_statements)
            elif type(node) is BreakNode:
                break_nodes.append(node)

            if self.node_to_connect(node):
                cfg_statements.append(node)
       
        self.connect_nodes(cfg_statements)

        if cfg_statements: # When body of module only contains ignored nodes
            first_statement = self.get_first_statement(cfg_statements[0])
            last_statements = self.get_last_statements(cfg_statements)
            return ConnectStatements(first_statement=first_statement, last_statements=last_statements, break_statements=break_nodes)
        return IgnoredNode()
    
    def visit_Module(self, node):
        return self.stmt_star_handler(node.body)

    def visit_ClassDef(self, node):
        logger.debug(node.name)
        self.add_to_definitions(node)

        local_definitions = self.module_definitions_stack[-1]
        local_definitions.classes.append(node.name)

        parent_definitions = self.get_parent_definitions()
        if parent_definitions:
            parent_definitions.classes.append(node.name)
        
        self.stmt_star_handler(node.body)

        local_definitions.classes.pop()
        if parent_definitions:
            parent_definitions.classes.pop()
        
        return IgnoredNode()

    def get_parent_definitions(self):
        parent_definitions = None
        if len(self.module_definitions_stack) > 1:
            parent_definitions = self.module_definitions_stack[-2]
        return parent_definitions

    def visit_FunctionDef(self, node):
        logger.debug(node.name)
        self.add_to_definitions(node)
        
        return IgnoredNode()

    def add_to_definitions(self, node):
        local_definitions = self.module_definitions_stack[-1]
        parent_definitions = self.get_parent_definitions()

        if parent_definitions:
            parent_qualified_name = '.'.join(parent_definitions.classes + [node.name])
            parent_definition = ModuleDefinition(parent_definitions, parent_qualified_name, local_definitions.module_name)
            parent_definition.node = node
            parent_definitions.append(parent_definition)

        local_qualified_name = '.'.join(local_definitions.classes + [node.name])
        local_definition = LocalModuleDefinition(local_definitions, local_qualified_name, None)
        local_definition.node = node
        local_definitions.append(local_definition)

        self.function_names.append(node.name)
    
    def return_connection_handler(self, nodes, exit_node):
        """Connect all return statements to the Exit node."""
        for function_body_node in nodes:
            if isinstance(function_body_node, ConnectToExitNode):
                if not exit_node in function_body_node.outgoing:
                    function_body_node.connect(exit_node)                    

    def add_if_label(self, CFG_node):
        """Prepend 'if ' and append ':' to the label of a Node."""
        CFG_node.label = 'if ' + CFG_node.label + ':'

    def add_elif_label(self, CFG_node):
        """Add the el to an already add_if_label'ed Node."""
        CFG_node.label = 'el' + CFG_node.label

    def handle_or_else(self, orelse, test):
        """Handle the orelse part of an if node.

        Returns:
            The last nodes of the orelse branch
        """
        if isinstance(orelse[0], ast.If):
            control_flow_node  = self.visit(orelse[0])
            self.add_elif_label(control_flow_node.test)
            test.connect(control_flow_node.test)
            return control_flow_node.last_nodes
        else:
            else_connect_statements = self.stmt_star_handler(orelse)
            test.connect(else_connect_statements.first_statement)
            return else_connect_statements.last_statements

    def remove_breaks(self, last_statements):
        """Remove all break statements in last_statements."""
        return [n for n in last_statements if type(n) is not BreakNode]

    def visit_If(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.test)

        test = self.append_node(Node(label_visitor.result, node, line_number = node.lineno))
        
        self.add_if_label(test)

        body_connect_stmts = self.stmt_star_handler(node.body)
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

        return self.append_node(Node(label_visitor.result, node.__class__.__name__, node, line_number=node.lineno))

    def visit_Return(self, node):
        label = LabelVisitor()
        label.visit(node)

        this_function_name = self.function_names[-1]

        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node.value)
        LHS = 'ret_' + this_function_name
        return self.append_node(ReturnNode(LHS + ' = ' + label.result, LHS, rhs_visitor.result, line_number = node.lineno))

    def visit_Raise(self, node):
        label = LabelVisitor()
        label.visit(node)

        return self.append_node(RaiseNode(label.result, line_number=node.lineno))

    def visit_Try(self, node):
        return Node('Try', node)

    def get_names(self, node, result):
        """Recursively finds all names."""
        if isinstance(node, ast.Name):
            return node.id + result
        elif isinstance(node, ast.Subscript):
            return result
        else:
            return self.get_names(node.value, result + '.' + node.attr)

    def extract_left_hand_side(self, target):
        """Extract the left hand side varialbe from a target.

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
                
                new_assignment_nodes.append( self.assignment_call_node(label.result, new_ast_node))
                
            else:
                label.result += ' = '
                label.visit(value)
                
                new_assignment_nodes.append(self.append_node(AssignmentNode(label.result, self.extract_left_hand_side(target), ast.Assign(target, value), right_hand_side_variables, line_number = node.lineno)))


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
                
                new_assignment_nodes.append(self.append_node(AssignmentNode(label.result, left_hand_side, ast.Assign(target, node.value), right_hand_side_variables, line_number = node.lineno)))

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
                return self.append_node(AssignmentNode(label.result, self.extract_left_hand_side(node.targets[0]), node, rhs_visitor.result, line_number = node.lineno))

    def assignment_call_node(self, left_hand_label, ast_node):
        """Handle assignments that contain a function call on its right side."""
        self.undecided = True # Used for handling functions in assignments

        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(ast_node.value)

        call = self.visit(ast_node.value)
        
        call_label = ''
        call_assignment = None
        if isinstance(call, AssignmentNode): #  assignment after returned nonbuiltin
            call_label = call.left_hand_side
            call_assignment = AssignmentNode(left_hand_label + ' = ' + call_label, left_hand_label, ast_node, [call.left_hand_side], line_number=ast_node.lineno)
            call.connect(call_assignment)
        else: #  assignment to builtin
            call_label = call.label
            call_assignment = AssignmentNode(left_hand_label + ' = ' + call_label, left_hand_label, ast_node, rhs_visitor.result, line_number=ast_node.lineno)

        self.nodes.append(call_assignment)

        self.undecided = False
        
        return call_assignment
    
    def visit_AugAssign(self, node):
        label = LabelVisitor()
        label.visit(node)

        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(node.value)
    
        return self.append_node(AssignmentNode(label.result, self.extract_left_hand_side(node.target), node, rhs_visitor.result, line_number = node.lineno))

    def loop_node_skeleton(self, test, node):
        """Common handling of looped structures, while and for."""
        body_connect_stmts = self.stmt_star_handler(node.body)

        test.connect(body_connect_stmts.first_statement)        
        test.connect_predecessors(body_connect_stmts.last_statements)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list()
        last_nodes.extend(body_connect_stmts.break_statements)
        
        if node.orelse:
            orelse_connect_stmts = self.stmt_star_handler(node.orelse)

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

        test = self.append_node(Node(label_visitor.result, node, line_number = node.lineno))

        self.add_while_label(test)
        
        return self.loop_node_skeleton(test, node)

    def visit_For(self, node):
        self.undecided = True  # Used for handling functions in for loops

        #issue23
        iterator_label = LabelVisitor()
        iterator = iterator_label.visit(node.iter)
        self.undecided = False

        target_label = LabelVisitor()
        target = target_label.visit(node.target)

        for_node = self.append_node(Node("for " + target_label.result + " in " + iterator_label.result + ':', node, line_number = node.lineno))

        
        
        if isinstance(node.iter, ast.Call) and get_call_names_as_string(node.iter.func)  in self.function_names:
            last_node = self.visit(node.iter)
            last_node.connect(for_node)
            
        
        return self.loop_node_skeleton(for_node, node)

    def visit_Expr(self, node):
        return self.visit(node.value)

    def save_local_scope(self):
        """Save the local scope before entering a function call."""
        saved_variables = list()
        for assignment in [node for node in self.nodes if type(node) == AssignmentNode]:
            if isinstance(assignment, RestoreNode):
                continue
           
        # above can be optimized with the assignments dict
            save_name = 'save_' + str(self.function_index) + '_' + assignment.left_hand_side
            previous_node = self.nodes[-1]
            saved_scope_node = self.append_node(RestoreNode(save_name + ' = ' + assignment.left_hand_side, save_name, [assignment.left_hand_side]))
            
            saved_variables.append(SavedVariable(LHS = save_name, RHS = assignment.left_hand_side))
            previous_node.connect(saved_scope_node)
        return saved_variables

    def save_actual_parameters_in_temp(self, args, arguments):
        """Save the actual parameters of a function call."""
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + arguments[i]
            
            if isinstance(parameter, ast.Num):
                n = RestoreNode(temp_name + ' = ' + str(parameter.n), temp_name, None)
            elif isinstance(parameter, ast.Name):
                n = RestoreNode(temp_name + ' = ' + parameter.id, temp_name, [parameter.id])
            elif isinstance(parameter, ast.Str):
                label = LabelVisitor()
                label.visit(parameter)
                
                n = RestoreNode(temp_name + ' = ' + label.result, temp_name, None)
            else:
                raise TypeError('Unhandled type: ' + str(type(parameter)))
            
            self.nodes[-1].connect(n)
            self.nodes.append(n)

    def create_local_scope_from_actual_parameters(self, args, arguments):
        """Create the local scope before entering the body of a function call."""
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + arguments[i]                
            local_name = arguments[i]
            previous_node = self.nodes[-1]
            local_scope_node = self.append_node(RestoreNode(local_name + ' = ' + temp_name, local_name, [temp_name]))
            previous_node.connect(local_scope_node)

    def restore_saved_local_scope(self, saved_variables):
        """Restore the previously saved variables to their original values.

        Args:
           saved_variables(list[SavedVariable]).
        """
        restore_nodes = list()
        for var in saved_variables:
            restore_nodes.append(RestoreNode(var.RHS + ' = ' + var.LHS, var.RHS, [var.LHS]))

        for n, successor in zip(restore_nodes, restore_nodes[1:]):
            n.connect(successor)

        if restore_nodes:
            self.nodes[-1].connect(restore_nodes[0])
            self.nodes.extend(restore_nodes)

        return restore_nodes

    def return_handler(self, node, function_nodes, restore_nodes):
        """Handle the return from a function during a function call."""
        call_node = None
        for n in function_nodes:
            if isinstance(n, ConnectToExitNode):
                LHS = CALL_IDENTIFIER + 'call_' + str(self.function_index)
                previous_node = self.nodes[-1]
                if not call_node:
                    RHS = 'ret_' + get_call_names_as_string(node.func)
                    call_node = self.append_node(RestoreNode(LHS + ' = ' + RHS, LHS, [RHS]))
                    previous_node.connect(call_node)
                    
            else:
                # lave rigtig kobling
                pass

    def insert_function(self, cfg, node):
        function = cfg.functions[node.func.id]
        self.function_index += 1

        saved_variables = self.save_local_scope()

        self.save_actual_parameters_in_temp(node.args, function)

        self.create_local_scope_from_actual_parameters(node.args, function)

        function_nodes = cfg.insert_function_body(node)

        restore_nodes = self.restore_saved_local_scope(saved_variables)

        self.return_handler(node, function_nodes, restore_nodes)
            
        return self.nodes[-1]

    def add_function(self, call_node, definition):
        self.function_index += 1
        def_node = definition.node
        saved_variables = self.save_local_scope()

        self.save_actual_parameters_in_temp(call_node.args, Arguments(def_node.args))

        self.create_local_scope_from_actual_parameters(call_node.args, Arguments(def_node.args))

        function_nodes = self.get_function_nodes(definition)

        restore_nodes = self.restore_saved_local_scope(saved_variables)

        self.return_handler(call_node, function_nodes, restore_nodes)
        return self.nodes[-1]

    def get_function_nodes(self, definition):
        length = len(self.nodes)
        previous_node = self.nodes[-1]
        entry_node = self.append_node(EntryExitNode("Entry " + definition.name))
        previous_node.connect(entry_node)
        function_body_connect_statements = self.stmt_star_handler(definition.node.body)
        
        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryExitNode("Exit " + definition.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        self.return_connection_handler(self.nodes[length:], exit_node)

        return self.nodes[length:]

    def add_builtin(self, node):
        label = LabelVisitor()
        label.visit(node)
        builtin_call = Node(label.result, node, line_number = node.lineno)

        if not self.undecided:
            self.nodes.append(builtin_call)
        self.undecided = False
        return builtin_call

    def visit_Call(self, node):
        _id = get_call_names_as_string(node.func)
        logging.debug(_id)

        ast_node = None
        
        local_definitions = self.module_definitions_stack[-1]
        definition = local_definitions.get_definition(_id)
    
        if definition:
            if isinstance(definition.node, ast.ClassDef):
                init = local_definitions.get_definition(_id + '.__init__')
                self.add_builtin(node)
            elif isinstance(definition.node, ast.FunctionDef):
                self.undecided = False
                return self.add_function(node, definition)
            else:
                raise Exception('Definition was neither FunctionDef or ClassDef, cannot add the function ')
        return self.add_builtin(node)

    def add_class(self, call_node, def_node):
        label_visitor = LabelVisitor()
        label_visitor.visit(call_node)

        previous_node = self.nodes[-1]

        entry_node = self.append_node(EntryExitNode("Entry " + def_node.name))

        previous_node.connect(entry_node)

        function_body_connect_statements = self.stmt_star_handler(def_node.body)
        
        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryExitNode("Exit " + def_node.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        return Node(label_visitor.result, call_node)
        
    def visit_Name(self, node):
        label = LabelVisitor()
        label.visit(node)

        return self.append_node(Node(label.result, node, line_number = node.lineno))

    def visit_With(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node.items[0])

        with_node = Node(label_visitor.result, node)
        connect_statements = self.stmt_star_handler(node.body)
        with_node.connect(connect_statements.first_statement)
        return ControlFlowNode(with_node, connect_statements.last_statements, connect_statements.break_statements)

    def add_module(self, module, module_name, local_names):
        module_path = module[1]
        self.local_modules = get_directory_modules(module_path)
        tree = generate_ast(module_path)

        parent_definitions = self.module_definitions_stack[-1]
        parent_definitions.import_names = local_names
        
        module_definitions = ModuleDefinitions(local_names, module_name)
        self.module_definitions_stack.append(module_definitions)

        self.append_node(EntryExitNode('Entry ' + module[0]))
        self.visit(tree)
        exit_node = self.append_node(EntryExitNode('Exit ' + module[0]))

        self.module_definitions_stack.pop()

        return exit_node

    def visit_Import(self, node):
        for name in node.names:
            for module in self.local_modules:
                if name.name == module[0]:
                    return self.add_module(module, name.name, None)
            for module in self.project_modules:
                if name.name == module[0]:
                    return self.add_module(module, name.name, None)
        return IgnoredNode()

    def visit_ImportFrom(self, node):
        for module in self.local_modules:
            if node.module == module[0]:
                    return self.add_module(module, None, [name.name for name in node.names])
        for module in self.project_modules:
            if node.module == module[0]:
                    return self.add_module(module, None, [name.name for name in node.names])
        return IgnoredNode()

    def visit_Str(self, node):
        return IgnoredNode()

    def visit_Break(self, node):
        return self.append_node(BreakNode(node, line_number = node.lineno))

    def visit_Pass(self, node):
        return self.append_node(Node('pass', node, line_number = node.lineno))

    def visit_Continue(self, node):
        return self.append_node(Node('continue', node, line_number = node.lineno))
