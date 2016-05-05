"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
Then 
"""
import ast
import os

from cfg import CFG


def is_python_module(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False

def get_python_modules(path):
    modules = list()
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if is_python_module(filename):
                modules.append((filename.replace('.py', ''), os.path.join(root, filename)))
    return modules

def get_project_module_names(path):
    project_modules = get_python_modules(path)
    project_module_names = list()
    for project_module in project_modules:
        project_module_names.append(project_module[0])
    return project_module_names

class Import():
    def __init__(self, name, module, path):
        self.name = name
        self.module = module
        self.path = path

class Alias():
    def __init__(self, name, asname=None):
        self.name = name
        self.asname = asname

class ImportVisitor(ast.NodeVisitor):
    def __init__(self, path):
        self.local_module_names = get_project_module_names(path)
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


def is_directory(path):
    if os.path.isdir(path):
        return True
    elif is_python_module(path):
        return False
    raise Exception(path, ' has to be a python module or a directory.')


def module_name_handler(node, name):
    if isinstance(node, ast.Import):
        return '.'.join(name.split('.')[0:-1])
    elif isinstance(node, ast.ImportFrom):
        return node.module
    else:
        raise Exception('Wrong type of node, ', node)


def get_all_imports(path):
    project_modules = get_python_modules(path)
    imports = list()
    for module in project_modules:
        imports.extend(get_imports(module[1]))
    return imports

def get_imports(module_path):
    imports = list()
    import_visitor = ImportVisitor(module_path)
    tree = generate_ast(module_path)
    import_visitor.visit(tree)
    for i in import_visitor.imports:
        for alias in i.names:
            _import = Import(alias.name, module_name_handler(i, alias.name), module_path)
            imports.append(_import)
    return imports

def file_to_cfg(path):
    tree = generate_ast(path)
    cfg = CFG()
    cfg.create(tree)
    return cfg

def file_to_cfgs(path, imports):
    tree = generate_ast(path)
    cfg = CFG(imports)
    cfg.create(tree)
    return cfg

def get_cfgs(path):
    cfg_list = list()
    if is_directory(path):
        project_modules = get_python_modules(path)
        imports = get_imports(project_modules[0][1])
        cfg_list.append(file_to_cfgs(project_modules[0][1], imports))
    else:
        cfg_list.append(file_to_cfg(path))

    return cfg_list

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)

    args = parser.parse_args()
    print(get_cfgs(args.filename))
