from ast import NodeVisitor

class StacktraceVisitor(NodeVisitor):
    '''Debug class that can be used to return information about nodes in the ast generated from the ast module.'''

    def visit(self,node):
        '''Visits all nodes and prints their class name.'''
        print(node.__class__.__name__)
        self.generic_visit(node)
