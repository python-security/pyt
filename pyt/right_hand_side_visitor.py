"""Contains a class that finds all names.

Used to find all variables on a right hand side(RHS) of assignment.
"""
from ast import NodeVisitor

class RHSVisitor(NodeVisitor):
    """Visitor collecting all names."""

    def __init__(self):
        """Initialize result as list."""
        self.result = list()

    def visit_Name(self, node):
        self.result.append(node.id)

    def visit_Call(self, node):
        if node.args:
            map(self.generic_visit, node.args)
        if node.keywords:
            map(self.generic_visit, node.keywords)
