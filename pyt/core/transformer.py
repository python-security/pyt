import ast


class AsyncTransformer():
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


class ChainedFunctionTransformer():
    def visit_chain(self, node, depth=1):
        if (
            isinstance(node.value, ast.Call) and
            isinstance(node.value.func, ast.Attribute) and
            isinstance(node.value.func.value, ast.Call)
        ):
            # Node is assignment or return with value like `b.c().d()`
            call_node = node.value
            # If we want to handle nested functions in future, depth needs fixing
            temp_var_id = '__chain_tmp_{}'.format(depth)
            # AST tree is from right to left, so d() is the outer Call and b.c() is the inner Call
            unvisited_inner_call = ast.Assign(
                targets=[ast.Name(id=temp_var_id, ctx=ast.Store())],
                value=call_node.func.value,
            )
            ast.copy_location(unvisited_inner_call, node)
            inner_calls = self.visit_chain(unvisited_inner_call, depth + 1)
            for inner_call_node in inner_calls:
                ast.copy_location(inner_call_node, node)
            outer_call = self.generic_visit(type(node)(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id=temp_var_id, ctx=ast.Load()),
                        attr=call_node.func.attr,
                        ctx=ast.Load(),
                    ),
                    args=call_node.args,
                    keywords=call_node.keywords,
                ),
                **{field: value for field, value in ast.iter_fields(node) if field != 'value'}  # e.g. targets
            ))
            ast.copy_location(outer_call, node)
            ast.copy_location(outer_call.value, node)
            ast.copy_location(outer_call.value.func, node)
            return [*inner_calls, outer_call]
        else:
            return [self.generic_visit(node)]

    def visit_Assign(self, node):
        return self.visit_chain(node)

    def visit_Return(self, node):
        return self.visit_chain(node)


class IfExpRewriter(ast.NodeTransformer):
    """Splits IfExp ternary expressions containing complex tests into multiple statements

    Will change

    a if b(c) else d

    into

    a if __if_exp_0 else d

    with Assign nodes in assignments [__if_exp_0 = b(c)]
    """

    def __init__(self, starting_index=0):
        self._temporary_variable_index = starting_index
        self.assignments = []
        super().__init__()

    def visit_IfExp(self, node):
        if isinstance(node.test, (ast.Name, ast.Attribute)):
            return self.generic_visit(node)
        else:
            temp_var_id = '__if_exp_{}'.format(self._temporary_variable_index)
            self._temporary_variable_index += 1
            assignment_of_test = ast.Assign(
                targets=[ast.Name(id=temp_var_id, ctx=ast.Store())],
                value=self.visit(node.test),
            )
            ast.copy_location(assignment_of_test, node)
            self.assignments.append(assignment_of_test)
            transformed_if_exp = ast.IfExp(
                test=ast.Name(id=temp_var_id, ctx=ast.Load()),
                body=self.visit(node.body),
                orelse=self.visit(node.orelse),
            )
            ast.copy_location(transformed_if_exp, node)
            return transformed_if_exp

    def visit_FunctionDef(self, node):
        return node


class IfExpTransformer:
    """Goes through module and function bodies, adding extra Assign nodes due to IfExp expressions."""

    def visit_body(self, nodes):
        new_nodes = []
        count = 0
        for node in nodes:
            rewriter = IfExpRewriter(count)
            possibly_transformed_node = rewriter.visit(node)
            if rewriter.assignments:
                new_nodes.extend(rewriter.assignments)
                count += len(rewriter.assignments)
            new_nodes.append(possibly_transformed_node)
        return new_nodes

    def visit_FunctionDef(self, node):
        transformed = ast.FunctionDef(
            name=node.name,
            args=node.args,
            body=self.visit_body(node.body),
            decorator_list=node.decorator_list,
            returns=node.returns
        )
        ast.copy_location(transformed, node)
        return self.generic_visit(transformed)

    def visit_Module(self, node):
        transformed = ast.Module(self.visit_body(node.body))
        ast.copy_location(transformed, node)
        return self.generic_visit(transformed)


class PytTransformer(AsyncTransformer, IfExpTransformer, ChainedFunctionTransformer, ast.NodeTransformer):
    pass
