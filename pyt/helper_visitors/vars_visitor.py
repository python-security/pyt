import ast
import itertools

from ..core.ast_helper import get_call_names


class VarsVisitor(ast.NodeVisitor):
    def __init__(self):
        self.result = list()

    def visit_Name(self, node):
        self.result.append(node.id)

    def visit_BoolOp(self, node):
        for v in node.values:
            self.visit(v)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        self.visit(node.operand)

    def visit_Lambda(self, node):
        self.visit(node.body)

    def visit_IfExp(self, node):
        self.visit(node.test)
        self.visit(node.body)
        self.visit(node.orelse)

    def visit_Dict(self, node):
        for k in node.keys:
            if k is not None:
                self.visit(k)
        for v in node.values:
            self.visit(v)

    def visit_Set(self, node):
        for e in node.elts:
            self.visit(e)

    def comprehension(self, node):
        self.visit(node.target)
        self.visit(node.iter)
        for c in node.ifs:
            self.visit(c)

    def visit_ListComp(self, node):
        self.visit(node.elt)
        for gen in node.generators:
            self.comprehension(gen)

    def visit_SetComp(self, node):
        self.visit(node.elt)
        for gen in node.generators:
            self.comprehension(gen)

    def visit_DictComp(self, node):
        self.visit(node.key)
        self.visit(node.value)
        for gen in node.generators:
            self.comprehension(gen)

    def visit_GeneratorComp(self, node):
        self.visit(node.elt)
        for gen in node.generators:
            self.comprehension(gen)

    def visit_Yield(self, node):
        if node.value:
            self.visit(node.value)

    def visit_YieldFrom(self, node):
        self.visit(node.value)

    def visit_Compare(self, node):
        self.visit(node.left)
        for c in node.comparators:
            self.visit(c)

    def visit_Call(self, node):
        # This will not visit Flask in Flask(__name__) but it will visit request in `request.args.get()
        if not isinstance(node.func, ast.Name):
            self.visit(node.func)
        for arg_node in itertools.chain(node.args, node.keywords):
            arg = arg_node.value if isinstance(arg_node, ast.keyword) else arg_node
            if isinstance(arg, ast.Call):
                if isinstance(arg.func, ast.Name):
                    # We can't just visit because we need to add 'ret_'
                    self.result.append('ret_' + arg.func.id)
                elif isinstance(arg.func, ast.Attribute):
                    # e.g. html.replace('{{ param }}', param)
                    # func.attr is replace
                    # func.value.id is html
                    # We want replace
                    self.result.append('ret_' + arg.func.attr)
                elif isinstance(arg.func, ast.Call):
                    self.visit_curried_call_inside_call_args(arg)
                else:
                    raise Exception('Cannot visit vars of ' + ast.dump(arg))
            else:
                self.visit(arg)

    def visit_curried_call_inside_call_args(self, inner_call):
        # Curried functions aren't supported really, but we now at least have a defined behaviour.
        # In f(g(a)(b)(c)), inner_call is the Call node with argument c
        # Try to get the name of curried function g
        curried_func = inner_call.func.func
        while isinstance(curried_func, ast.Call):
            curried_func = curried_func.func
        if isinstance(curried_func, ast.Name):
            self.result.append('ret_' + curried_func.id)
        elif isinstance(curried_func, ast.Attribute):
            self.result.append('ret_' + curried_func.attr)

        # Visit all arguments except a (ignore the curried function g)
        not_curried = inner_call
        while not_curried.func is not curried_func:
            for arg in itertools.chain(not_curried.args, not_curried.keywords):
                self.visit(arg.value if isinstance(arg, ast.keyword) else arg)
            not_curried = not_curried.func

    def visit_Attribute(self, node):
        if not isinstance(node.value, ast.Name):
            self.visit(node.value)
        else:
            self.result.append(node.value.id)

    def slicev(self, node):
        if isinstance(node, ast.Slice):
            if node.lower:
                self.visit(node.lower)
            if node.upper:
                self.visit(node.upper)
            if node.step:
                self.visit(node.step)
        elif isinstance(node, ast.ExtSlice):
            if node.dims:
                for d in node.dims:
                    self.visit(d)
        else:
            self.visit(node.value)

    def visit_Subscript(self, node):
        if isinstance(node.value, ast.Attribute):
            # foo.bar[1]
            self.result.append(list(get_call_names(node.value))[0])
        self.visit(node.value)
        self.slicev(node.slice)

    def visit_Starred(self, node):
        self.visit(node.value)

    def visit_List(self, node):
        for el in node.elts:
            self.visit(el)

    def visit_Tuple(self, node):
        for el in node.elts:
            self.visit(el)
