import ast
import inspect

from label_visitor import LabelVisitor
from vars_visitor import VarsVisitor


def generate_ast(path):
    '''Generates an Abstract Syntax Tree using the ast module.'''
    
    with open(path, 'r') as f:
        return ast.parse(f.read())

def print_CFG(CFG):
    '''Prints a CFG created by using the CFG class.'''
    print(inspect.stack()[1][3])
    for x, n in enumerate(CFG.nodes):
        print('Node: ' + str(x) + ' ' + str(n))


class Node(object):
    '''A Control Flow Graph node that contains a list of ingoing and outgoing nodes and a list of its variables.'''
    def __init__(self, label, ast_type, *, ingoing=None, outgoing=None, variables=None):
        if ingoing is None:
            self.ingoing = list()
        else:
            self.ingoing = ingoing
        
        if outgoing is None:
            self.outgoing = list()
        else:
            self.outgoing = outgoing
            
        if variables is None:
            self.variables = list()
        else:
            self.variables = variables
            
        self.label = label
        self.ast_type = ast_type

    def __str__(self):        
        label = ' '.join(('Label: ', self.label))
        ast_type = ' '.join(('Type: ', self.ast_type))
        outgoing = ''
        ingoing = ''
        if self.outgoing is not None:
            outgoing = ' '.join((' \toutgoing: ', str([x.label for x in self.outgoing])))
        else:
            outgoing = ' '.join((' \toutgoing: ', '[]'))
        if self.ingoing is not  None:
            ingoing = ' '.join(('ingoing: ', str([x.label for x in self.ingoing])))
        else:
            ingoing = ' '.join(('ingoing: ', '[]'))
    
        variables = ' '.join(('variables: ', ' '.join(self.variables)))
        return ' '.join((label, ast_type, outgoing, ingoing, variables))
    

class CFG(ast.NodeVisitor):
    nodes = list()

    def create(self, ast):
        '''
        Creates a Control Flow Graph.

        ast is an Abstract Syntax Tree generated with the ast module.
        '''

        start_node = Node('Start node', 'START')
        self.nodes.append(start_node)
        
        module_statements = self.visit(ast)

        first_node = module_statements[0]
        start_node.outgoing.append(first_node)

        exit_node = Node('Exit node', 'EXIT')
        self.nodes.append(exit_node)
        
        last_node = module_statements[-1]
        last_node.outgoing.append(exit_node)

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
            orelse_test.outgoing.append(inner_test)
            orelse_test.outgoing.append(body_first)
            
            ref_to_parent_next_node.append(orelse_test)
        else:
            stmts = self.stmt_star_handler(orelse_node)
            first_stmt = stmts[0]
            last_stmt = stmts[-1]
            orelse_test = first_stmt
            ref_to_parent_next_node.append(last_stmt)
            

        return orelse_test # return for previous elif to refer to
    
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
                    last.outgoing.append(next_node)
            elif isinstance(next_node,tuple): # case for if
                n.outgoing.append(next_node[0])
            else:
                n.outgoing.append(next_node)

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
            test.outgoing.append(orelse_test)
            
        test.outgoing.append(body_first)

        return (test, last_nodes)
            
    def visit_Assign(self, node):

        label = LabelVisitor()
        label.visit(node)

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        n = Node(label.result, node.__class__.__name__, variables = variables_visitor.result)
        self.nodes.append(n)
        
        return n

    def visit_AugAssign(self, node):

        label = LabelVisitor()
        label.visit(node)

        variables_visitor = VarsVisitor()
        variables_visitor.visit(node)

        n = Node(label.result, node.__class__.__name__, variables = variables_visitor.result)
        self.nodes.append(n)

        return n

    def visit_While(self, node): 
        test = self.visit(node.test)
        body_stmts = self.stmt_star_handler(node.body)

        body_first = body_stmts[0]
        test.outgoing.append(body_first)
        
        body_last = body_stmts[-1]
        body_last.outgoing.append(test)

        # last_nodes is used for making connections to the next node in the parent node
        # this is handled in stmt_star_handler
        last_nodes = list() 
        last_nodes.append(body_last)
        
        if node.orelse:
            orelse_stmts = self.stmt_star_handler(node.orelse)
            orelse_last = orelse_stmts[-1]
            orelse_first = orelse_stmts[0]

            test.outgoing.append(orelse_first)
            last_nodes.append(orelse_last)


        return (test,last_nodes)
        

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
