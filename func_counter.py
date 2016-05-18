import ast
import sys
import os

sys.path.insert(0, os.path.abspath('pyt'))
from cfg import get_call_names_as_string, generate_ast
from project_handler import get_python_modules

function_calls = list()
functions = dict()
classes = dict()

class Counter(ast.NodeVisitor):
    def visit_Call(self, node):
        n = get_call_names_as_string(node.func)
        function_calls.append(n)
        self.generic_visit(node)
        #Husk return, save vars overhead

    def visit_FunctionDef(self, node):
        if node.name in functions:
            node.name += '¤'
        functions[node.name] = len(node.body)
        for n in node.body:
            self.visit(n)

    def visit_ClassDef(self, node):
        if node.name in classes:
            node.name += '¤'
        classes[node.name] = len(node.body)
        for n in node.body:
            self.visit(n)


if __name__ == '__main__':
    module_paths = (m[1] for m in get_python_modules('../flaskbb/flaskbb'))
    for p in module_paths:        
        print(p)
        t = generate_ast(p)
        c = Counter()
        c.visit(t)

    max_func_len = max(functions.values())
    max_class_len = max(classes.values())
    restore_stuff = 6 #varies
    print(len(function_calls))
    print('estimate stuff: ', max_func_len*len(function_calls))
    print('estimate stuff: ', max_class_len*len(function_calls))

        
