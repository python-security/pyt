from ast import NodeVisitor

class VarsVisitor(NodeVisitor):

    def visit_Name(self,node):
        self.result.append(node.id)

    def visit_Call(self,node):
        for arg in node.args:
            self.visit(arg)
        for keyword in node.keywords:
            self.visit(keyword)

    def visit_keyword(self, node):
        self.visit(node.value)

    def __init__(self):
        self.result = list()
