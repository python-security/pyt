import os

from pyt.core.project_handler import _is_python_file


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
            if _is_python_file(filename):
                full_path = os.path.join(root, filename)
                directory = os.path.dirname(os.path.realpath(full_path)).split(module_root)[-1].replace(os.sep, '.')
                directory = directory.replace('.', '', 1)
                if directory:
                    modules.append(('.'.join((module_root, directory, filename.replace('.py', ''))), full_path))
                else:
                    modules.append(('.'.join((module_root, filename.replace('.py', ''))), full_path))

    return modules
