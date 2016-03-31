import ast
from collections import namedtuple, OrderedDict
from copy import deepcopy

from label_visitor import LabelVisitor
from vars_visitor import VarsVisitor

ENTRY = 'ENTRY'
EXIT = 'EXIT'
CALL_IDENTIFIER = '¤'


def generate_ast(path):
    '''Generates an Abstract Syntax Tree using the ast module.'''
    with open(path, 'r') as f:
        return ast.parse(f.read())

NodeInfo = namedtuple('NodeInfo', 'label variables')
ControlFlowNode = namedtuple('ControlFlowNode', 'test last_nodes')
SavedVariable = namedtuple('SavedVariable', 'LHS RHS')
Visitors = namedtuple('Visitors', 'variables_visitor label_visitor')
ConnectStatements = namedtuple('ConnectStatements', 'first_statement last_statements')


class IgnoredNode(object):
    '''Ignored Node sent from a ast node that is not yet implemented'''


class Node(object):
    '''A Control Flow Graph node that contains a list of ingoing and outgoing nodes and a list of its variables.'''
    def __init__(self, label, ast_type, *, line_number=None, variables=None):
        self.ingoing = list()
        self.outgoing = list()

        if variables is None:
            self.variables = list()
        else:
            self.variables = variables

        self.label = label
        self.ast_type = ast_type
        self.line_number = line_number

        # Used by the Fixedpoint algorithm
        self.old_constraint = set()
        self.new_constraint = set()

    def connect(self, successor):
        '''Connects this node to its successor node by setting its outgoing and the successors ingoing.'''
        self.outgoing.append(successor)
        successor.ingoing.append(self)

    def connect_predecessors(self, predecessors):
        for n in predecessors:
            self.ingoing.append(n)
            n.outgoing.append(self)

    def __str__(self):
        return ' '.join(('Label: ', self.label))

    def __repr__(self):        
        label = ' '.join(('Label: ', self.label))
        line_number = 'Line number: ' + str(self.line_number)
        ast_type = ' '.join(('Type:\t\t', self.ast_type))
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
    
        variables = ' '.join(('variables:\t', ' '.join(self.variables)))
        if self.old_constraint is not None:
            old_constraint = 'Old constraint:\t ' + ', '.join([x.label for x in self.old_constraint])
        else:
            old_constraint = 'Old constraint:\t '

        if self.new_constraint is not None:
            new_constraint = 'New constraint: ' +  ', '.join([x.label for x in self.new_constraint])
        else:
            new_constraint = 'New constraint:'
        return '\n' + '\n'.join((label, line_number, ast_type, ingoing, outgoing, variables, old_constraint, new_constraint))


class FunctionNode(Node):
    ''''''
    def __init__(self):
        super(FunctionNode, self).__init__(self.__class__.__name__, ast.FunctionDef().__class__.__name__)


class AssignmentNode(Node):
    ''''''
    def __init__(self, label, left_hand_side, *, line_number=None, variables=None):
        super(AssignmentNode, self).__init__(label, ast.Assign().__class__.__name__, line_number=line_number, variables=variables)
        self.left_hand_side = left_hand_side

    def __repr__(self):
        output_string = super(AssignmentNode, self).__repr__()
        output_string += '\n'
        return ''.join((output_string, 'left_hand_side:\t', str(self.left_hand_side)))


class RestoreNode(AssignmentNode):
    '''Node used for handling restore nodes returning from function calls'''

    def __init__(self, label, left_hand_side, *, line_number=None, variables=None):
        super(RestoreNode, self).__init__(label, left_hand_side, line_number=line_number, variables=variables)
        

class CallReturnNode(AssignmentNode):
    def __init__(self, label, ast_type, restore_nodes, *, line_number=None, variables=None):
        super(AssignmentNode, self).__init__(label, ast_type, line_number=line_number, variables=variables)
        self.restore_nodes = restore_nodes

    def __repr__(self):
        output_string = super(AssignmentNode, self).__repr__()
        output_string += '\n'
        return ''.join((output_string, 'restore_nodes:\t', str(self.restore_nodes)))
    

class Arguments(object):
    def __init__(self, args):
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
    def __init__(self, nodes, args):
        self.nodes = nodes
        self.arguments = Arguments(args)
    

class CFG(ast.NodeVisitor):
    '''A Control Flow Graph containing a list of nodes.'''
    def __init__(self):
        self.nodes = list()
        self.functions = OrderedDict()
        self.function_index = 0
        self.undecided = False

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
        
    def create(self, ast):
        '''
        Creates a Control Flow Graph.

        ast is an Abstract Syntax Tree generated with the ast module.
        '''

        entry_node = Node('Entry node', ENTRY)
        self.nodes.append(entry_node)
        
        module_statements = self.visit(ast)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty, there is nothing to analyse.')
        
        first_node = module_statements[0]
        entry_node.connect(first_node)

        exit_node = Node('Exit node', EXIT)
        self.nodes.append(exit_node)
            
        last_nodes = module_statements[1]
        exit_node.connect_predecessors(last_nodes)
    
    def flatten_cfg_statements(self, cfg_statements):
        '''For use in stmt_star_handler. Flattens the cfg_statements list by eliminating tuples
        The list now only contain the entry element of each statement'''
        return [x[0] if isinstance(x, tuple) else x for x in cfg_statements]

    def stmt_star_handler(self, stmts):
        '''handling of stmt* 

        links all statements together in a list of statements, accounting for statements with multiple last nodes'''
        cfg_statements = list()

        for stmt in stmts:
            n = self.visit(stmt)

            if isinstance(n, IgnoredNode):
                continue
            elif isinstance(n, ControlFlowNode):
                cfg_statements.append(n)
            elif n.ast_type is not ast.FunctionDef().__class__.__name__:
                cfg_statements.append(n)

       
        for n, next_node in zip(cfg_statements, cfg_statements[1:]):
            if isinstance(n, ControlFlowNode):             # case for if
                for last in n[1]:                         # list of last nodes in ifs and elifs
                    if isinstance(next_node, ControlFlowNode):
                        last.connect(next_node.test)        # connect to next if test case
                    else:
                        last.connect(next_node)
            elif isinstance(next_node, ControlFlowNode):  # case for if
                n.connect(next_node[0])
            elif type(next_node) is RestoreNode:
                continue
            elif CALL_IDENTIFIER in next_node.label:
                continue
            else:
                n.connect(next_node)

        last_statements = list()
        if isinstance(cfg_statements[-1], ControlFlowNode):
            last_statements.extend(cfg_statements[-1].last_nodes)
        else:
            last_statements.append(cfg_statements[-1])

        cfg_statements = self.flatten_cfg_statements(cfg_statements)
        return ConnectStatements(first_statement=cfg_statements[0], last_statements=last_statements)

    def run_visitors(self, *, variables_visitor_visit_node, label_visitor_visit_node):
        '''Creates and runs the VarsVisitor and LabelVisitor.

        Returns visitors in a tuple.'''
        variables_visitor = VarsVisitor()
        variables_visitor.visit(variables_visitor_visit_node)
        label_visitor = LabelVisitor()
        label_visitor.visit(label_visitor_visit_node)
        visitors = Visitors(variables_visitor, label_visitor)
        return visitors

    
    def visit_Module(self, node):
        return self.stmt_star_handler(node.body)

    def visit_FunctionDef(self, node):
        function_CFG = CFG()
        function_CFG.functions = self.functions
        self.functions[node.name] = Function(function_CFG.nodes, node.args)

        entry_node = Node('Entry node: ' + node.name, ENTRY)
        function_CFG.nodes.append(entry_node)
        
        function_body_connect_statements = function_CFG.stmt_star_handler(node.body)

        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = Node('Exit node: ' + node.name, EXIT)
        function_CFG.nodes.append(exit_node)

        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        return FunctionNode()

    def add_if_label(self, CFG_node):
        CFG_node.label = 'if ' + CFG_node.label + ':'

    def add_elif_label(self, CFG_node):
        CFG_node.label = 'el' + CFG_node.label

    def visit_If(self, node):
        test = self.visit(node.test)
        self.add_if_label(test)
        body_connect_stmts = self.stmt_star_handler(node.body)

        if node.orelse:
            if isinstance(node.orelse[0], ast.If):
                control_flow_node  = self.visit(node.orelse[0])
                self.add_elif_label(control_flow_node.test)
                test.connect(control_flow_node.test)
                body_connect_stmts.last_statements.extend(control_flow_node.last_nodes)
            else:
                else_connect_statements = self.stmt_star_handler(node.orelse)
                test.connect(else_connect_statements.first_statement)
                body_connect_stmts.last_statements.extend(else_connect_statements.last_statements)
        else:
            body_connect_stmts.last_statements.append(test) # if there is no orelse, test needs an edge to the next_node

        test.connect(body_connect_stmts.first_statement)

        return ControlFlowNode(test, body_connect_stmts.last_statements)

    def visit_NameConstant(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)

        n = Node(label_visitor.result, node.__class__.__name__, line_number=node.lineno)
        self.nodes.append(n)
        return n

    def visit_Return(self, node):
        label = LabelVisitor()
        label.visit(node)

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        this_function = list(self.functions.keys())[-1]
        n = Node('ret_' + this_function + ' = ' + label.result, node.__class__.__name__, line_number = node.lineno, variables = variables_visitor.result)
        self.nodes.append(n)

        return n

    def extract_left_hand_side(self, target):
        ''''''
        left_hand_side = target.id

        left_hand_side.replace('*', '')
        if '[' in left_hand_side:
            index = left_hand_side.index('[')
            left_hand_side = target[0:index]

        return left_hand_side

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Tuple):
            for i, target in enumerate(node.targets[0].elts):
                value = node.value.elts[i]
                visitors = self.run_visitors(variables_visitor_visit_node = value, label_visitor_visit_node = target)
                if isinstance(value, ast.Call):
                    return self.assignment_call_node(visitors.label_visitor.result, value)
                else:
                    visitors.label_visitor.result += ' = '
                    visitors.label_visitor.visit(value)
                
                n = AssignmentNode(visitors.label_visitor.result, self.extract_left_hand_side(target), line_number = node.lineno, variables = visitors.variables_visitor.result)
                self.nodes[-1].connect(n)
                self.nodes.append(n)
            return self.nodes[-1] # return the last added node

        else:
            if isinstance(node.value, ast.Call):
                label = LabelVisitor()
                label.visit(node.targets[0])
                return self.assignment_call_node(label.result, node.value)
            else:
                visitors = self.run_visitors(variables_visitor_visit_node = node.value, label_visitor_visit_node = node)

                n = AssignmentNode(visitors.label_visitor.result, self.extract_left_hand_side(node.targets[0]), line_number = node.lineno, variables = visitors.variables_visitor.result)
            
                self.nodes.append(n)
                return n
        # self.assignments[n.left_hand_side] = n # Use for optimizing saving scope in call

    def assignment_call_node(self, left_hand_label, value):
        self.undecided = True # Used for handling functions in assignments
        
        call = self.visit(value)
        
        call_label = ''
        call_assignment = None
        if isinstance(call, AssignmentNode):
            call_label = call.left_hand_side
            call_assignment = AssignmentNode(left_hand_label + ' = ' + call_label, left_hand_label)
            call.connect(call_assignment)
        else:
            call_label = call.label
            call_assignment = AssignmentNode(left_hand_label + ' = ' + call_label, left_hand_label)

        self.nodes.append(call_assignment)
        
        return call_assignment
    
    def visit_AugAssign(self, node):

        visitors = self.run_visitors(variables_visitor_visit_node = node,
                                     label_visitor_visit_node = node)
        

        n = AssignmentNode(visitors.label_visitor.result, self.extract_left_hand_side(node.target), line_number = node.lineno, variables = visitors.variables_visitor.result)
        self.nodes.append(n)
        # self.assignments[n.left_hand_side] = n
        
        return n

    def loop_node_skeleton(self, test, node):
        body_connect_stmts = self.stmt_star_handler(node.body)

        test.connect(body_connect_stmts.first_statement)        
        test.connect_predecessors(body_connect_stmts.last_statements)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list() 
        
        if node.orelse:
            orelse_connect_stmts = self.stmt_star_handler(node.orelse)

            test.connect(orelse_connect_stmts.first_statement)
            last_nodes.extend(orelse_connect_stmts.last_statements)
        else:
            last_nodes.append(test)  # if there is no orelse, test needs an edge to the next_node

        return ControlFlowNode(test, last_nodes)
    
    def visit_While(self, node):
        test = self.visit(node.test)
        return self.loop_node_skeleton(test, node)

    def visit_For(self, node):
        self.undecided = True  # Used for handling functions in for loops

        #issue23
        iterator_label = LabelVisitor()
        iterator = iterator_label.visit(node.iter)
        self.undecided = False 

        target_label = LabelVisitor()
        target = target_label.visit(node.target)

        for_node = Node("for " + target_label.result + " in " + iterator_label.result + ':', node.__class__.__name__, line_number = node.lineno)
        
        self.nodes.append(for_node)
        
        return self.loop_node_skeleton(for_node, node)

    def visit_Compare(self, node):
        
        variables_visitor = VarsVisitor()
        
        for i in node.comparators:
            variables_visitor.visit(i)
            
        variables_visitor.visit(node.left)

        label = LabelVisitor()
        label.visit(node)

        n = Node(label.result, node.__class__.__name__, line_number = node.lineno, variables = variables_visitor.result)
        self.nodes.append(n)

        return n

    def visit_Expr(self, node):
        return self.visit(node.value)

    def save_local_scope(self):
        saved_variables = list()
        for assignment in [node for node in self.nodes if isinstance(node, AssignmentNode)]:
            if isinstance(assignment, RestoreNode):
                continue
           
        # above can be optimized with the assignments dict
            save_name = 'save_' + str(self.function_index) + '_' + assignment.left_hand_side
            n = RestoreNode(save_name + ' = ' + assignment.left_hand_side, save_name, variables = assignment.variables)
            saved_variables.append(SavedVariable(LHS = save_name, RHS = assignment.left_hand_side))
            self.nodes[-1].connect(n)
            self.nodes.append(n)
        return saved_variables

    def save_actual_parameters_in_temp(self, args, function):
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + function.arguments[i]
            
            if isinstance(parameter, ast.Num):
                n = AssignmentNode(temp_name + ' = ' + str(parameter.n), temp_name)
            elif isinstance(parameter, ast.Name):
                n = AssignmentNode(temp_name + ' = ' + parameter.id, temp_name)
            else:
                raise TypeError('Unhandled type: ' + str(type(parameter)))
            
            self.nodes[-1].connect(n)
            self.nodes.append(n)

    def create_local_scope_from_actual_parameters(self, args, function):
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + function.arguments[i]                
            local_name = function.arguments[i]
            n = AssignmentNode(local_name + ' = ' + temp_name, local_name)
            self.nodes[-1].connect(n)
            self.nodes.append(n)

    def insert_function_body(self, node):
        function_nodes = deepcopy(self.functions[node.func.id].nodes)
        self.nodes[-1].connect(function_nodes[0])
        self.nodes.extend(function_nodes)
        return function_nodes

    def restore_saved_local_scope(self, saved_variables):
            restore_nodes = list()
            for var in saved_variables:
                restore_nodes.append(RestoreNode(var.RHS + ' = ' + var.LHS, var.RHS))

            for n, successor in zip(restore_nodes, restore_nodes[1:]):
                n.connect(successor)

            self.nodes[-1].connect(restore_nodes[0])
            self.nodes.extend(restore_nodes)
            return restore_nodes

    def return_handler(self, node, function_nodes, restore_nodes):
        for n in function_nodes:
            if n.ast_type == ast.Return().__class__.__name__:
                LHS = CALL_IDENTIFIER + 'call_' + str(self.function_index)
                call_node = RestoreNode(LHS + ' = ' + 'ret_' + node.func.id, LHS)
                self.nodes[-1].connect(call_node)
                self.nodes.append(call_node)
                    
            else:
                # lave rigtig kobling
                pass

    def visit_Call(self, node):
        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        label = LabelVisitor()
        label.visit(node)

        builtin_call = Node(label.result, node.__class__.__name__, line_number = node.lineno, variables = variables_visitor.result)
        
        if not isinstance(node.func, ast.Attribute) and node.func.id in self.functions:
            function = self.functions[node.func.id]
            self.function_index += 1
            
            saved_variables = self.save_local_scope()

            self.save_actual_parameters_in_temp(node.args, function)

            self.create_local_scope_from_actual_parameters(node.args, function)

            function_nodes = self.insert_function_body(node)

            restore_nodes = self.restore_saved_local_scope(saved_variables)

            self.return_handler(node, function_nodes, restore_nodes)
            
            return self.nodes[-1]
        else:
            if not self.undecided:
                self.nodes.append(builtin_call)
            self.undecided = False
            return builtin_call

    def visit_Name(self, node):
        vars = VarsVisitor()
        vars.visit(node)

        label = LabelVisitor()
        label.visit(node)

        n = Node(label.result,node.__class__.__name__, line_number = node.lineno, variables = vars.result)
        self.nodes.append(n)
        
        return n

    # Visitors that are just ignoring statements
    def visit_Import(self, node):
        return IgnoredNode()

    def visit_ImportFrom(self, node):
        return IgnoredNode()

    def visit_Str(self, node):
        return IgnoredNode()
