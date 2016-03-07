from ast import NodeVisitor

class LabelVisitor(NodeVisitor):
    def visit_Assign(self, node):
        for target in node.targets:
            self.visit(target)
        self.result = ' '.join((self.result,'='))
        self.visit(node.value)

    def visit_AugAssign(self, node):
        self.visit(node.target)
        self.visit(node.op)
        self.result = self.result + '='
        self.visit(node.value)

    def visit_Compare(self,node):
        self.visit(node.left)
        for op,com in zip(node.ops,node.comparators):
            self.visit(op)
            self.visit(com)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.op)
        self.visit(node.right)

    #  operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv
    def visit_Add(self, node):
        self.result = ' '.join((self.result, '+'))

    def visit_Sub(self, node):
        self.result = ' '.join((self.result, '-'))

    def visit_Mult(self, node):
        self.result = ' '.join((self.result, '*'))

    def vist_MatMult(self, node):
        self.result = ' '.join((self.result, 'x'))

    def visit_Div(self, node):
        self.result = ' '.join((self.result, '/'))

    def visit_Mod(self, node):
        self.result = ' '.join((self.result, '%'))

    def visit_Pow(self, node):
        self.result = ' '.join((self.result, '**'))

    def visit_LShift(self, node):
        self.result = ' '.join((self.result, '<<'))

    def visit_RShift(self, node):
        self.result = ' '.join((self.result, '>>'))

    def visit_BitOr(self, node):
        self.result = ' '.join((self.result, '|'))

    def visit_BitXor(self, node):
        self.result = ' '.join((self.result, '^'))

    def visit_BitAnd(self, node):
        self.result = ' '.join((self.result, '&'))

    def visit_FloorDiv(self, node):
        self.result = ' '.join((self.result, '//'))


    # cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn
    def visit_Eq(self, node):
        self.result = ' '.join((self.result, '=='))

    def visit_Gt(self, node):
        self.result = ' '.join((self.result,'>'))

    def visit_Lt(self, node):
        self.result = ' '.join((self.result,'<'))

    def visit_NotEq(self,node):
        self.result = ' '.join((self.result,'!='))

    def visit_GtE(self,node):
        self.result = ' '.join((self.result,'>='))

    def visit_LtE(self,node):
        self.result = ' '.join((self.result,'<='))

    def visit_Is(self,node):
        self.result = ' '.join((self.result,'is'))

    def visit_IsNot(self,node):
        self.result = ' '.join((self.result,'is not'))

    def visit_In(self,node):
        self.result = ' '.join((self.result,'in'))

    def visit_NotIn(self,node):
        self.result = ' '.join((self.result,'not in'))

    def visit_Num(self, node):
        self.result = self.join((self.result, str(node.n)))

    def visit_Name(self,node):
        self.result = self.join((self.result, node.id))

    def visit_Str(self,node):
        self.result = ' '.join((self.result,node.s))

    def join(self, strings):
        return ' '.join(filter(None,strings)) # filters out empty strings, providing a cleaner output


    def __init__(self):
        self.result = ''
