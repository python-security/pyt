import ast

from .ast_helper import get_call_names
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


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

    def visit_IfExpr(self, node):
        self.visit(node.test)
        self.visit(node.body)
        self.visit(node.orelse)

    def visit_Dict(self, node):
        for k in node.keys:
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

    def visit_Await(self, node):
        self.visit(node.value)

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
        if not isinstance(node.func, ast.Name):
            self.visit(node.func)
        if node.args:
            for arg in node.args:
                logger.debug("[voyager] arg is %s", arg)
                if isinstance(arg, ast.Call):
                    logger.debug("[voyager] arg.func is %s", arg.func)
                    if isinstance(arg.func, ast.Name):
                        logger.debug("[voyager] arg.func.id is %s", arg.func.id)
                        self.result.append('ret_' + arg.func.id)
                    elif isinstance(arg.func, ast.Attribute):
                        logger.debug("It is an attribute!")
                        logger.debug("[voyager] arg.func.attr is %s", arg.func.attr)
                        self.result.append('ret_' + arg.func.attr)
                        raise
                    else:
                        logger.debug("type(arg.func) is %s", type(arg.func))
                        raise
                else:
                    self.visit(arg)
        if node.keywords:
            for keyword in node.keywords:
                logger.debug("[voyager] keyword is %s", keyword)
                if isinstance(keyword, ast.Call):
                    self.result.append('ret_' + keyword.func.id)
                else:
                    self.visit(keyword)

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
