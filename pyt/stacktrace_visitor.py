import argparse
import os

from ast import NodeVisitor
from label_visitor import LabelVisitor

from cfg import generate_ast

parser = argparse.ArgumentParser()
parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)
args = parser.parse_args()

class StacktraceVisitor(NodeVisitor):
    """Debug class that can be used to return information about nodes in the ast generated from the ast module."""
    level = 0
    indent = '    '

    def visit_Store(self, node):
        pass
    
    def visit_Load(self, node):
        pass

    def visit_Num(self, node):
        print(self.indent * self.level + str(node.n))

    def visit_Str(self, node):
        print(self.indent * self.level + node.s)

    def visit_Name(self, node):
        print(self.indent * self.level + node.id)
        
    def visit_If(self, node):
        test_label = self.visit(node.test)
        print(node.__class__.__name__, self.indent * self.level + 'if', test_label + ':')
        
        self.level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.level-=1

        print(self.indent * self.level + 'else:')

        self.level += 1
        for stmt in node.orelse:
            self.visit(stmt)
        self.level-=1              

    def visit_NameConstant(self, node):
        label = LabelVisitor()
        label.visit(node)
        return label.result
    
    def visit_Compare(self, node):
        label = LabelVisitor()
        label.visit(node)
        return label.result

    def visit_Assign(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)
        print(node.__class__.__name__, self.indent * self.level + label_visitor.result)

    def visit_AugAssign(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)
        print(self.indent * self.level + label_visitor.result)
        
    def visit_While(self, node):
        test_label = self.visit(node.test)
        print('while', test_label + ':')
        
        self.level += 1
        for stmt in node.body:
            self.visit(stmt)
        self.level-=1

    def visit_Call(self, node):
        label_visitor = LabelVisitor()
        label_visitor.visit(node)
        print(self.indent* self.level + label_visitor.result)

if __name__ == '__main__':
    path = os.path.normpath(args.filename)
    tree = generate_ast(path)
    stack_trace = StacktraceVisitor()
    stack_trace.visit(tree)
