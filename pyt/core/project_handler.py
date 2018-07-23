"""Generates a list of CFGs from a path.

The module finds all python modules and generates an ast for them.
"""
import os


_local_modules = list()


def get_directory_modules(directory):
    """Return a list containing tuples of
    e.g. ('__init__', 'example/import_test_project/__init__.py')
    """
    if _local_modules and os.path.dirname(_local_modules[0][1]) == directory:
        return _local_modules

    if not os.path.isdir(directory):
        # example/import_test_project/A.py -> example/import_test_project
        directory = os.path.dirname(directory)

    if directory == '':
        return _local_modules

    for path in os.listdir(directory):
        if _is_python_file(path):
            # A.py -> A
            module_name = os.path.splitext(path)[0]
            _local_modules.append((module_name, os.path.join(directory, path)))

    return _local_modules


def get_modules(path):
    """Return a list containing tuples of
    e.g. ('test_project.utils', 'example/test_project/utils.py')
    """
    module_root = os.path.split(path)[1]
    modules = list()
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if _is_python_file(filename):
                directory = os.path.dirname(
                    os.path.realpath(
                        os.path.join(
                            root,
                            filename
                        )
                    )
                ).split(module_root)[-1].replace(
                    os.sep,  # e.g. '/'
                    '.'
                )
                directory = directory.replace('.', '', 1)
                modules.append((
                    '.'.join(p for p in (module_root, directory, _filename_to_module(filename)) if p),
                    os.path.join(root, filename)
                ))

    return modules


def _is_python_file(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False


def _filename_to_module(filename):
    if filename == '__init__.py':
        return ''
    else:
        return os.path.splitext(filename)[0]
