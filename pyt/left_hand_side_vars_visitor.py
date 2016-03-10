from ast import NodeVisitor

class LHSVarsVisitor(NodeVisitor):
    def __init__(self):
        self.result = set()

    def visit_Call(self, node):
        pass

    def visit_Assign(self, node):
        for target in node.targets:
            self.visit(target)

    def visit_AugAssign(self, node):
        self.visit(node.target)
        
    def visit_Name(self,node):
        self.result.add(node.id)
    
    def visit_Subscript(self, node):
        self.visit(node.value)
        
    def visit_Starred(self, node):
        self.visit(node.value)

    



