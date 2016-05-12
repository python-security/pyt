"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
Then 
"""
import ast
import os

CLASS_FUNCTION_SEPERATOR = ':'

def is_python_module(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False

local_modules = list()
def get_directory_modules(directory):
    
    if not os.path.isdir(directory):
        directory = os.path.dirname(directory)
        
    if local_modules and os.path.dirname(local_modules[0][1]) == directory:
        return local_modules
    
    for path in os.listdir(directory):
        if is_python_module(path):
            module_name = os.path.splitext(path)[0]
            local_modules.append((module_name, os.path.join(directory,path)))

    return local_modules

def get_python_modules(path):
    module_root = os.path.split(path)[1]
    modules = list()
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if is_python_module(filename):
                directory = os.path.dirname(os.path.realpath(os.path.join(root, filename))).split(module_root)[-1].replace(os.sep, '.')
                directory = directory.replace('.', '', 1)
                if directory:
                    modules.append(('.'.join((module_root, directory, filename.replace('.py', ''))), os.path.join(root, filename)))
                else:
                    modules.append(('.'.join((module_root, filename.replace('.py', ''))), os.path.join(root, filename)))

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


class Definition():
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __str__(self):
        return ', '.join(('Definition: ', self.name, self.path))

class Module():
    def __init__(self, path, imports, classes, functions):
        self.path = path
        self.imports = imports
        self.classes = classes
        self.functions = functions

    def __str__(self):
        return '\n'.join(('Module:', self.path, str([str(s) for s in self.imports]), str([str(s) for s in self.classes]), str([str(s) for s in self.functions])))


class DefinitionVisitor(ast.NodeVisitor):
    def __init__(self, path):
        self.local_module_names = get_project_module_names(path)
        self.imports = list()
        self.functions = list()
        self.classes = list()
        self.latest_class = None

    def visit_FunctionDef(self, node):
        function_name = ''
        if self.latest_class:
            function_name = self.latest_class
            function_name += CLASS_FUNCTION_SEPERATOR
        function_name += node.name
        self.functions.append(function_name)

    def visit_ClassDef(self, node):
        self.latest_class = node.name
        self.classes.append(node.name)
        for stmt in node.body:
            self.visit(stmt)
        self.latest_class = None
        
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


def get_project_definitions_and_imports(path):
    project_modules = get_python_modules(path)
    modules = list()
    for module in project_modules:
        modules.append(get_definitions_and_imports(module[1]))
    return modules

def get_definitions_and_imports(module_path):
    imports = list()
    functions = list()
    classes = list()
    definition_visitor = DefinitionVisitor(module_path)
    tree = generate_ast(module_path)
    definition_visitor.visit(tree)

    for i in definition_visitor.imports:
        for alias in i.names:
            _import = Import(alias.name, module_name_handler(i, alias.name), module_path)
            imports.append(_import)

    for function_name in definition_visitor.functions:
        functions.append(Definition(function_name, module_path))

    for class_name in definition_visitor.classes:
        classes.append(Definition(class_name, module_path))

    return Module(module_path, imports, classes, functions)

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
        modules = get_project_definitions_and_imports(path)
        for module in modules:
            print(module)
            #cfg_list.append(file_to_cfgs(project_modules[index][1], imports))
    else:
        cfg_list.append(file_to_cfg(path))

    return cfg_list

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)

    args = parser.parse_args()
    print(get_cfgs(args.filename))
