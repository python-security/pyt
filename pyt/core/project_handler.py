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


def get_modules(path, prepend_module_root=True):
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

                module_name_parts = []
                if prepend_module_root:
                    module_name_parts.append(module_root)
                if directory:
                    module_name_parts.append(directory)

                if filename == '__init__.py':
                    path = root
                else:
                    module_name_parts.append(os.path.splitext(filename)[0])
                    path = os.path.join(root, filename)

                modules.append(('.'.join(module_name_parts), path))

    return modules


def _is_python_file(path):
    if os.path.splitext(path)[1] == '.py':
        return True
    return False
