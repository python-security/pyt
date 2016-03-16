import ast
import collections

from label_visitor import LabelVisitor
from vars_visitor import VarsVisitor
from left_hand_side_vars_visitor import LHSVarsVisitor

ENTRY = 'ENTRY'
EXIT = 'EXIT'

def generate_ast(path):
    '''Generates an Abstract Syntax Tree using the ast module.'''
    
    with open(path, 'r') as f:
        return ast.parse(f.read())

NodeInfo = collections.namedtuple('NodeInfo', 'label variables')
ControlFlowNode = collections.namedtuple('ControlFlowNode', 'test last_nodes')
        
class Node(object):
    '''A Control Flow Graph node that contains a list of ingoing and outgoing nodes and a list of its variables.'''
    def __init__(self, label, ast_type, *, variables=None):
        self.ingoing = list()
        self.outgoing = list()
                    
        if variables is None:
            self.variables = list()
        else:
            self.variables = variables
            
        self.label = label
        self.ast_type = ast_type

        # Used by the Fixedpoint algorithm
        self.old_constraint = set()
        self.new_constraint = set()
        
    def connect(self, successor):
        '''Connects this node to its successor node by setting its outgoing and the successors ingoing.'''
        
        self.outgoing.append(successor)
        successor.ingoing.append(self)
        

    def __str__(self):
        return ' '.join(('Label: ', self.label))
        
    def __repr__(self):        
        label = ' '.join(('Label: ', self.label))
        ast_type = ' '.join(('Type:\t\t', self.ast_type))
        outgoing = ''
        ingoing = ''
        if self.outgoing is not None:
            outgoing = ' '.join(('outgoing:\t', str([x.label for x in self.outgoing])))
        else:
            outgoing = ' '.join(('outgoing:\t', '[]'))
        if self.ingoing is not  None:
            ingoing = ' '.join(('ingoing:\t', str([x.label for x in self.ingoing])))
        else:
            ingoing = ' '.join(('ingoing:\t', '[]'))
    
        variables = ' '.join(('variables:\t', ' '.join(self.variables)))
        if self.old_constraint is not None:
            old_constraint = 'Old constraint:\t ' + ', '.join([x.label for x in self.old_constraint])
        else:
            old_constraint = 'Old constraint:\t '

        if self.new_constraint is not None:
            new_constraint = 'New constraint: ' +  ', '.join([x.label for x in self.new_constraint])
        else:
            new_constraint = 'New constraint:' 
        return '\n' + '\n'.join((label, ast_type, outgoing, ingoing, variables, old_constraint, new_constraint))
    
class AssignmentNode(Node):
    ''''''
    def __init__(self, label, ast_type, left_hand_side, *, variables = None):
        super(AssignmentNode, self).__init__(label, ast_type, variables = variables)
        self.left_hand_side = left_hand_side

    def __repr__(self):
        output_string = super(AssignmentNode, self).__repr__()
        output_string += '\n'
        return ''.join((output_string, 'left_hand_side:\t', str(self.left_hand_side)))
    
class CFG(ast.NodeVisitor):
    
    def __init__(self):
        self.nodes = list()

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

        first_node = module_statements[0]
        entry_node.connect(first_node)

        exit_node = Node('Exit node', EXIT)
        self.nodes.append(exit_node)
        
        last_node = module_statements[-1]
        last_node.connect(exit_node)
        

    def orelse_handler(self, orelse_node, ref_to_parent_next_node):
        ''' Handler for orelse nodes in If nodes. 
        
        orelse_node is a orelse node from the If.
        This is either a list with one if, or a stmt*
        
        ref_to__parent_next_node is a list of nodes that need a reference to the next statement in the syntax tree'''
        
        orelse_test = None
        
        if isinstance(orelse_node[0], ast.If):
            body_stmts = self.stmt_star_handler(orelse_node[0].body)
            body_first = body_stmts[0]
            body_last = body_stmts[-1]
            ref_to_parent_next_node.append(body_last)

            inner_test = self.orelse_handler(orelse_node[0].orelse, ref_to_parent_next_node)
            orelse_test =  self.visit(orelse_node[0].test)
            orelse_test.connect(inner_test)
            orelse_test.connect(body_first)
            
            ref_to_parent_next_node.append(orelse_test)
        else:
            stmts = self.stmt_star_handler(orelse_node)
            first_stmt = stmts[0]
            last_stmt = stmts[-1]
            orelse_test = first_stmt
            ref_to_parent_next_node.append(last_stmt)
            

        return orelse_test # return for previous elif to refer to
    
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
            cfg_statements.append(n)

        for n, next_node in zip(cfg_statements, cfg_statements[1:]):
            if isinstance(n,tuple): # case for if
                for last in n[1]:# list of last nodes in ifs and elifs
                    last.connect(next_node)
            elif isinstance(next_node,tuple): # case for if
                n.connect(next_node[0])
            else:
                n.connect(next_node)
                
        cfg_statements = self.flatten_cfg_statements(cfg_statements)
        return cfg_statements
    
    def visit_Module(self, node):
        return self.stmt_star_handler(node.body)

        
    def visit_If(self, node):
        test = self.visit(node.test)
        body_stmts = self.stmt_star_handler(node.body)
        
        body_first = body_stmts[0]
        body_last = body_stmts[-1]
        
        last_nodes = list()
        last_nodes.append(body_last)
        if node.orelse:
            orelse_test = self.orelse_handler(node.orelse, last_nodes)
            test.connect(orelse_test)
        else:
            last_nodes.append(test) # if there is no orelse, test needs an edge to the next_node

            
        test.connect(body_first)

        return ControlFlowNode(test, last_nodes)
            
    def visit_Assign(self, node):

        label = LabelVisitor()
        label.visit(node)

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        lhs_vars_visitor = LHSVarsVisitor()
        lhs_vars_visitor.visit(node)

        n = AssignmentNode(label.result, node.__class__.__name__, lhs_vars_visitor.result, variables = variables_visitor.result)
        self.nodes.append(n)
        
        return n

    def visit_AugAssign(self, node):

        label = LabelVisitor()
        label.visit(node)

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        lhs_vars_visitor = LHSVarsVisitor()
        lhs_vars_visitor.visit(node)

        n = AssignmentNode(label.result, node.__class__.__name__, lhs_vars_visitor.result, variables = variables_visitor.result)
        self.nodes.append(n)

        return n

    def loop_node_skeleton(self, test, node):
        body_stmts = self.stmt_star_handler(node.body)

        body_first = body_stmts[0]
        test.connect(body_first)
        
        body_last = body_stmts[-1]
        body_last.connect(test)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list() 
        
        if node.orelse:
            orelse_stmts = self.stmt_star_handler(node.orelse)
            orelse_last = orelse_stmts[-1]
            orelse_first = orelse_stmts[0]

            test.connect(orelse_first)
            last_nodes.append(orelse_last)
        else:
            last_nodes.append(test) # if there is no orelse, test needs an edge to the next_node

        return ControlFlowNode(test, last_nodes)
    
    def visit_While(self, node):
        test = self.visit(node.test)
        return self.loop_node_skeleton(test, node)

    def visit_For(self, node):
        target = self.visit(node.target)
        iterator = self.visit(node.iter)
        for_node = Node("for " + target.label + " in " + iterator.label, node.__class__.__name__)
        self.nodes.append(for_node)
        
        return self.loop_node_skeleton(for_node, node)

    def visit_Compare(self, node):
        
        variables_visitor = VarsVisitor()
        
        for i in node.comparators:
            variables_visitor.visit(i)
            
        variables_visitor.visit(node.left)

        label = LabelVisitor()
        label.visit(node)

        n = Node(label.result, node.__class__.__name__, variables = variables_visitor.result)
        self.nodes.append(n)

        return n

    def visit_Expr(self, node):
        return self.visit(node.value)
    
    def visit_Call(self, node):

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        label = LabelVisitor()
        label.visit(node)
        
        n = Node(label.result, node.__class__.__name__, variables = variables_visitor.result)
        self.nodes.append(n)
                
        return n

    def visit_Name(self, node):
        vars = VarsVisitor()
        vars.visit(node)

        label = LabelVisitor()
        label.visit(node)

        return NodeInfo(label.result, vars.result)
