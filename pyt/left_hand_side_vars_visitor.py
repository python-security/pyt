from ast import NodeVisitor

class LHSVarsVisitor(NodeVisitor):

    def visit_Name(self,node):
        self.result.append(node.id)

