"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
Then 
"""
import ast
import os

def is_python_module(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False

local_modules = list()
def get_directory_modules(directory):
    
    if not os.path.isdir(directory):
        directory = os.path.dirname(directory)

    if directory == '':
        return local_modules
    
        
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

def is_directory(path):
    if os.path.isdir(path):
        return True
    elif is_python_module(path):
        return False
    raise Exception(path, ' has to be a python module or a directory.')
