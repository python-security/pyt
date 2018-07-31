import ast


class AsyncTransformer(ast.NodeTransformer):
    """Converts all async nodes into their synchronous counterparts."""

    def visit_Await(self, node):
        """Awaits are treated as if the keyword was absent."""
        return self.visit(node.value)

    def visit_AsyncFunctionDef(self, node):
        return self.visit(ast.FunctionDef(**node.__dict__))

    def visit_AsyncFor(self, node):
        return self.visit(ast.For(**node.__dict__))

    def visit_AsyncWith(self, node):
        return self.visit(ast.With(**node.__dict__))
