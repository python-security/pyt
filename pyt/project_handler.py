"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
Then 
"""
import ast
import os

from cfg import CFG

class Import():
    def __init__(self, names, module=None, level=None):
        self.names = names
        self.module = module
        self.level = level

class Alias():
    def __init__(self, name, asname=None):
        self.name = name
        self.asname = asname

class ImportVisitor(ast.NodeVisitor):
    def __init__(self, local_module_names):
        self.local_module_names = local_module_names
        self.imports= list()

    def visit_Import(self, node):
        for name in node.names:
            if name.name in self.local_module_names:
                self.imports.append(node)

    def visit_ImportFrom(self, node):
        if node.module.split('.')[-1] in self.local_module_names:
            self.imports.append(node)

def generate_ast(path):
    """Generate an Abstract Syntax Tree using the ast module."""
    with open(path, 'r') as f:
        return ast.parse(f.read())

def is_python_module(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False

def is_directory(path):
    if os.path.isdir(path):
        return True
    elif is_python_module(path):
        return False
    raise Exception(path, ' has to be a python module or a directory.')

def get_python_modules(path):
    modules = list()
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if is_python_module(filename):
                modules.append((filename.replace('.py', ''), os.path.join(root, filename)))
    return modules

def directory_handler(path):
    local_modules = get_python_modules(path)
    local_module_names = list()
    for local_module in local_modules:
        local_module_names.append(local_module[0])
    
    for module in local_modules:
        import_visitor = ImportVisitor(local_module_names)
        tree = generate_ast(module[1])
        import_visitor.visit(tree)
        imports = import_visitor.imports
        print(imports)

def file_to_cfg(path):
    tree = generate_ast(path)
    cfg = CFG()
    cfg.create(tree)
    return cfg

def get_cfgs(path):
    cfg_list = list()
    if is_directory(path):
        directory_handler(path)
    else:
        cfg_list.append(file_to_cfg(path))

    return cfg_list

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)

    args = parser.parse_args()
    get_cfgs(args.filename)
