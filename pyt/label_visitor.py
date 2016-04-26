from ast import NodeVisitor
import ast

class LabelVisitor(NodeVisitor):
    def handle_comma_separated(self, comma_separated_list):
        if comma_separated_list:
            for element in range(len(comma_separated_list)-1):
                self.visit(comma_separated_list[element])
                self.result += ', '
            
            self.visit(comma_separated_list[-1])
    
    def visit_Tuple(self, node):
        self.result += '('

        self.handle_comma_separated(node.elts)

        self.result += ')'

    def visit_List(self, node):
        self.result += '['

        self.handle_comma_separated(node.elts)
        
        self.result += ']'
    
    def visit_Return(self, node):
        if node.value:
            self.visit(node.value)
        
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
        self.result += '='
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

    def visit_UnaryOp(self, node):
        self.visit(node.op)
        self.visit(node.operand)

    
    def comprehensions(self, node):
        self.visit(node.elt)

        for expression in node.generators:
            self.result += ' for '
            self.visit(expression.target)
            self.result += ' in '
            self.visit(expression.iter)
        
    def visit_GeneratorExp(self, node):
        self.result += '('
        self.comprehensions(node)
        self.result += ')'
        
    def visit_ListComp(self, node):
        self.result += '['
        self.comprehensions(node)
        self.result += ']'

    def visit_SetComp(self, node):
        self.result += '{'
        self.comprehensions(node)
        self.result += '}'


    def visit_DictComp(self, node):
        self.result += '{'
        
        self.visit(node.key)
        self.result += ' : '
        self.visit(node.value)
        
        for expression in node.generators:
            self.result += ' for '
            self.visit(expression.target)
            self.result += ' in '
            self.visit(expression.iter)
            
        self.result += '}'
    def visit_Attribute(self, node):
        self.visit(node.value)
        self.result += '.'
        self.result += node.attr
        
    def visit_Call(self, node):
        self.visit(node.func)
        self.result += '('

        self.handle_comma_separated(node.args)
        
        #keyword handling

        self.result += ')'

    def insert_space(self):
        self.result += ' '

    def visit_NameConstant(self, node):
        self.result += str(node.value)
        
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

    #unaryop = Invert | Not | UAdd | USub
    def visit_Invert(self, node):
        self.result += '~'

    def visit_Not(self, node):
        self.result += 'not '

    def visit_UAdd(self, node):
        self.result += '+'

    def visit_USub(self, node):
        self.result += '-'

    def visit_Num(self, node):
        self.result += str(node.n)

    def visit_Name(self,node):
        self.result += node.id

    def visit_Str(self,node):
        self.result += "'" + node.s + "'"


    def __init__(self):
        self.result = ''
