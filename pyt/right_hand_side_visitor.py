"""Contains a class that finds all names.
Used to find all variables on a right hand side(RHS) of assignment.
"""
import ast
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class RHSVisitor(ast.NodeVisitor):
    """Visitor collecting all names."""

    def __init__(self):
        """Initialize result as list."""
        self.result = list()

    def visit_Name(self, node):
        self.result.append(node.id)

    def visit_Call(self, node):
        logger.debug("hey i am here after all")
        if node.args:
            for arg in node.args:
                self.visit(arg)
        if node.keywords:
            for keyword in node.keywords:
                self.visit(keyword)
