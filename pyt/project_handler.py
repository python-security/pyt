"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
"""
import os


local_modules = list()
def get_directory_modules(directory, flush_local_modules=False):
    """Return a list containing tuples of
    e.g. ('__init__', 'example/import_test_project/__init__.py')
    """
    if local_modules and os.path.dirname(local_modules[0][1]) == directory:
        return local_modules

    if flush_local_modules:
        del local_modules[:]

    if not os.path.isdir(directory):
        # example/import_test_project/A.py -> example/import_test_project
        directory = os.path.dirname(directory)

    if directory == '':
        return local_modules

    for path in os.listdir(directory):
        if is_python_file(path):
            # A.py -> A
            module_name = os.path.splitext(path)[0]
            local_modules.append((module_name, os.path.join(directory, path)))

    return local_modules

def get_modules(path):
    """Return a list containing tuples of
    e.g. ('test_project.utils', 'example/test_project/utils.py')
    """
    module_root = os.path.split(path)[1]
    modules = list()
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if is_python_file(filename):
                directory = os.path.dirname(os.path.realpath(os.path.join(root, filename))).split(module_root)[-1].replace(os.sep, '.')
                directory = directory.replace('.', '', 1)
                if directory:
                    modules.append(('.'.join((module_root, directory, filename.replace('.py', ''))), os.path.join(root, filename)))
                else:
                    modules.append(('.'.join((module_root, filename.replace('.py', ''))), os.path.join(root, filename)))

    return modules

def get_modules_and_packages(path):
    """Return a list containing tuples of
    e.g. ('folder', 'example/test_project/folder', '.folder')
         ('test_project.utils', 'example/test_project/utils.py')
    """
    module_root = os.path.split(path)[1]
    modules = list()
    for root, directories, filenames in os.walk(path):
        for directory in directories:
            if directory != '__pycache__':
                full_path = os.path.join(root, directory)
                relative_path = os.path.realpath(full_path).split(module_root)[-1].replace(os.sep, '.')
                # Remove the dot in front to be consistent
                modules.append((relative_path[1:], full_path, relative_path))

        for filename in filenames:
            if is_python_file(filename):
                full_path = os.path.join(root, filename)
                directory = os.path.dirname(os.path.realpath(full_path)).split(module_root)[-1].replace(os.sep, '.')
                directory = directory.replace('.', '', 1)
                if directory:
                    modules.append(('.'.join((module_root, directory, filename.replace('.py', ''))), full_path))
                else:
                    modules.append(('.'.join((module_root, filename.replace('.py', ''))), full_path))

    return modules

def is_python_file(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False
