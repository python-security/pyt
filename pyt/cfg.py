from ast import parse
from ast import NodeVisitor
from label_visitor import LabelVisitor
from vars_visitor import VarsVisitor
from pprint import pprint
from inspect import stack

file_name = 'example.py'
obj = parse(open(file_name).read())


class Node(object):
    '''A Control Flow Graph node that contains a list of ingoing and outgoing nodes and a list of its variables.'''
    def __init__(self, label, *, ingoing=None, outgoing=None, variables=None):
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

    def __str__(self):        
        label = ' '.join(('Label: ',self.label))
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
        return ' '.join((label, outgoing, ingoing, variables))


def print_CFG(CFG):
    print(stack()[1][3])
    for x, n in enumerate(CFG):
        print('Node: ' + str(x) + ' ' + str(n))

    
CFG = list()

class Listener(NodeVisitor):
    visit_all = False

    if visit_all:
        def visit(self,node):
            print(node.__class__.__name__)
            self.generic_visit(node)

    def stmt_star_handler(self, stmts):
        cfg_statements = list()
        
        for stmt in stmts:
            n = self.visit(stmt)
            cfg_statements.append(n)

        for n, next_node in zip(cfg_statements, cfg_statements[1:]):
            if isinstance(n,tuple):
                n[0].outgoing.append(next_node)
                n[1].outgoing.append(next_node)
            elif isinstance(next_node,tuple):
                n.outgoing.append(next_node[0])
            else:
                n.outgoing.append(next_node)

        return cfg_statements
            
    def visit_Module(self, node):        
        self.stmt_star_handler(node.body)

        print_CFG(CFG)

    def visit_If(self, node):
        test = self.visit(node.test)
        body_stmts = self.stmt_star_handler(node.body)
        if node.orelse:
            orelse = self.visit(node.orelse)

        body_first = body_stmts[0]
        body_last = body_stmts[-1]
            
        test.outgoing.append(body_first)

        return (test,body_last)
            
    def visit_Assign(self, node):

        label = LabelVisitor()
        label.visit(node)

        vars = VarsVisitor()
        vars.visit(node)

        n = Node(label.result,variables=vars.result)
        CFG.append(n)
        
        print_CFG(CFG)
        
        return n


    def visit_While(self, node): 
        test = self.visit(node.test)
        body_stmts = self.stmt_star_handler(node.body)
        if node.orelse:
            orelse = self.visit(node.orelse)

        body_first = body_stmts[0]
        test.outgoing.append(body_first)
        
        body_last = body_stmts[-1]
        body_last.outgoing.append(test)
            
        print_CFG(CFG)

        return test
        

    def visit_Compare(self, node):
        
        vars = VarsVisitor()
        for i in node.comparators:
            vars.visit(i)
        vars.visit(node.left)

        label = LabelVisitor()
        label.visit(node)

        n = Node(label.result, variables = vars.result)
        CFG.append(n)

        print_CFG(CFG)

        return n

    def visit_Expr(self, node):
        return self.visit(node.value)
    
    def visit_Call(self, node):

        vars = VarsVisitor()
        vars.visit(node)

        label = LabelVisitor()
        label.visit(node)
        
        n = Node(label.result, variables = vars.result)
        CFG.append(n)

        print_CFG(CFG)
                
        return n


Listener().visit(obj)
