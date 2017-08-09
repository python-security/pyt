"""Contains a class that finds all names.

Used to find all variables on a right hand side(RHS) of assignment.
"""
import ast


class RHSVisitor(ast.NodeVisitor):
    """Visitor collecting all names."""

    def __init__(self):
        """Initialize result as list."""
        self.result = list()

    def visit_Attribute(self, node):
        self.visit(node.value)

    def visit_Name(self, node):
        self.result.append(node.id)

    def visit_Call(self, node):
        self.visit(node.func)

        if node.args:
            for arg in node.args:
                self.visit(arg)
        if node.keywords:
            for keyword in node.keywords:
                self.visit(keyword)
