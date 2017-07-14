"""This module contains helper function.
Useful when working with the ast module."""
import ast
import os
import subprocess


BLACK_LISTED_CALL_NAMES = ['self']
recursive = False
python_2_mode = False


def convert_to_3(path):
    """Convert python 2 file to python 3."""
    try:
        print('##### Trying to convert file to Python 3. #####')
        subprocess.call(['2to3', '-w', path])
    except:
        print('Check if 2to3 is installed. '
              'https://docs.python.org/2/library/2to3.html')
        exit(1)


def generate_ast(path, python_2=False):
    """Generate an Abstract Syntax Tree using the ast module.

        Args:
            path(str): The path to the file e.g. example/foo/bar.py
            python_2(bool): Determines whether or not to call 2to3.
    """
    # If set, it stays set.
    global python_2_mode
    if python_2:
        python_2_mode = True
    if os.path.isfile(path):
        with open(path, 'r') as f:
            try:
                return ast.parse(f.read())
            except SyntaxError:
                global recursive
                if not recursive:
                    if not python_2_mode:
                        convert_to_3(path)
                    recursive = True
                    return generate_ast(path)
                else:
                    raise SyntaxError('The ast module can not parse the file'
                                      ' and the python 2 to 3 conversion'
                                      ' also failed.')
    raise IOError('Input needs to be a file. Path: ' + path)


def list_to_dotted_string(list_of_components):
    """Convert a list to a string seperated by a dot."""
    return '.'.join(list_of_components)


def get_call_names_helper(node, result):
    """Recursively finds all function names."""
    if isinstance(node, ast.Name):
        if node.id not in BLACK_LISTED_CALL_NAMES:
            result.append(node.id)
        return result
    elif isinstance(node, ast.Call):
        return result
    elif isinstance(node, ast.Subscript):
        return get_call_names_helper(node.value, result)
    elif isinstance(node, ast.Str):
        result.append(node.s)
        return result
    else:
        result.append(node.attr)
        return get_call_names_helper(node.value, result)


def get_call_names_as_string(node):
    """Get a list of call names as a string."""
    return list_to_dotted_string(get_call_names(node))


def get_call_names(node):
    """Get a list of call names."""
    result = list()
    return reversed(get_call_names_helper(node, result))


class Arguments():
    """Represents arguments of a function."""

    def __init__(self, args):
        """Create an Argument container class.

        Args:
            args(list(ast.args): The arguments in a function AST node.
        """
        self.args = args.args
        self.varargs = args.vararg
        self.kwarg = args.kwarg
        self.kwonlyargs = args.kwonlyargs
        self.defaults = args.defaults
        self.kw_defaults = args.kw_defaults

        self.arguments = list()
        if self.args:
            self.arguments.extend([x.arg for x in self.args])
        if self.varargs:
            self.arguments.extend(self.varargs.arg)
        if self.kwarg:
            self.arguments.extend(self.kwarg.arg)
        if self.kwonlyargs:
            self.arguments.extend([x.arg for x in self.kwonlyargs])

    def __getitem__(self, key):
        return self.arguments.__getitem__(key)

    def __len__(self):
        return self.args.__len__()
