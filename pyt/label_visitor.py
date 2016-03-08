from ast import NodeVisitor

class LabelVisitor(NodeVisitor):
    def visit_Assign(self, node):
        for target in node.targets:
            self.visit(target)
        self.result = ' '.join((self.result,'='))
        self.insert_space()
        
        self.visit(node.value)

    def visit_AugAssign(self, node):
        self.visit(node.target)

        self.insert_space()
        self.visit(node.op)
        self.result = self.result + '='
        self.insert_space()
        self.visit(node.value)

    def visit_Compare(self,node):
        self.visit(node.left)
        self.insert_space()
        
        for op,com in zip(node.ops,node.comparators):
            self.visit(op)
            self.insert_space()
            self.visit(com)
            self.insert_space()

        self.result = self.result.rstrip()

    def visit_BinOp(self, node):
        self.visit(node.left)

        self.insert_space()
        self.visit(node.op)
        self.insert_space()
        
        self.visit(node.right)

    def visit_Call(self, node):
        self.visit(node.func)
        self.result += '('
        for arg in range(len(node.args)-1):
            self.visit(node.args[arg])
            self.result += ', '
            
        self.visit(node.args[-1])
            
        #keyword handling

        self.result += ')'

    def insert_space(self):
        self.result += ' '
        
    #  operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv
    def visit_Add(self, node):
        self.result += '+'

    def visit_Sub(self, node):
        self.result += '-'

    def visit_Mult(self, node):
        self.result += '*'

    def vist_MatMult(self, node):
        self.result += 'x'

    def visit_Div(self, node):
        self.result += '/'

    def visit_Mod(self, node):
        self.result += '%'

    def visit_Pow(self, node):
        self.result += '**'

    def visit_LShift(self, node):
        self.result += '<<'

    def visit_RShift(self, node):
        self.result += '>>'

    def visit_BitOr(self, node):
        self.result += '|'

    def visit_BitXor(self, node):
        self.result += '^'

    def visit_BitAnd(self, node):
        self.result += '&'

    def visit_FloorDiv(self, node):
        self.result += '//'


    # cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn
    def visit_Eq(self, node):
        self.result += '=='

    def visit_Gt(self, node):
        self.result += '>'

    def visit_Lt(self, node):
        self.result += '<'

    def visit_NotEq(self,node):
        self.result += '!='

    def visit_GtE(self,node):
        self.result += '>='

    def visit_LtE(self,node):
        self.result += '<='

    def visit_Is(self,node):
        self.result += 'is'

    def visit_IsNot(self,node):
        self.result += 'is not'

    def visit_In(self,node):
        self.result += 'in'

    def visit_NotIn(self,node):
        self.result +='not in'

    def visit_Num(self, node):
        self.result += str(node.n)

    def visit_Name(self,node):
        self.result += node.id

    def visit_Str(self,node):
        self.result += "'" + node.s + "'"


    def __init__(self):
        self.result = ''
