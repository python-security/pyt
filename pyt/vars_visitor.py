from ast import NodeVisitor

class VarsVisitor(NodeVisitor):
    def __init__(self):
        self.result = list()

    def visit_Name(self, node):
        self.result.append(node.id)

    #  Condition and call rule
    def visit_Call(self, node):
        for arg in node.args:
            self.visit(arg)
        for keyword in node.keywords:
            self.visit(keyword)
            
    def visit_keyword(self, node):
        self.visit(node.value)

    def visit_Compare(self, node):
        self.generic_visit(node)

    #  Assignment rule                
    def visit_Assign(self, node): 
        self.visit(node.value)

        
