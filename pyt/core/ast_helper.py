"""This module contains helper function.
Useful when working with the ast module."""

import ast
import os
import subprocess
from functools import lru_cache


BLACK_LISTED_CALL_NAMES = ['self']
recursive = False


def _convert_to_3(path):  # pragma: no cover
    """Convert python 2 file to python 3."""
    try:
        print('##### Trying to convert file to Python 3. #####')
        subprocess.call(['2to3', '-w', path])
    except subprocess.SubprocessError:
        print('Check if 2to3 is installed. '
              'https://docs.python.org/2/library/2to3.html')
        exit(1)


@lru_cache()
def generate_ast(path):
    """Generate an Abstract Syntax Tree using the ast module.

        Args:
            path(str): The path to the file e.g. example/foo/bar.py
    """
    if os.path.isfile(path):
        with open(path, 'r') as f:
            try:
                return ast.parse(f.read())
            except SyntaxError:  # pragma: no cover
                global recursive
                if not recursive:
                    _convert_to_3(path)
                    recursive = True
                    return generate_ast(path)
                else:
                    raise SyntaxError('The ast module can not parse the file'
                                      ' and the python 2 to 3 conversion'
                                      ' also failed.')
    raise IOError('Input needs to be a file. Path: ' + path)


def _get_call_names_helper(node):
    """Recursively finds all function names."""
    if isinstance(node, ast.Name):
        if node.id not in BLACK_LISTED_CALL_NAMES:
            yield node.id
    elif isinstance(node, ast.Subscript):
        yield from _get_call_names_helper(node.value)
    elif isinstance(node, ast.Str):
        yield node.s
    elif isinstance(node, ast.Attribute):
        yield node.attr
        yield from _get_call_names_helper(node.value)


def get_call_names(node):
    """Get a list of call names."""
    return reversed(list(_get_call_names_helper(node)))


def _list_to_dotted_string(list_of_components):
    """Convert a list to a string seperated by a dot."""
    return '.'.join(list_of_components)


def get_call_names_as_string(node):
    """Get a list of call names as a string."""
    return _list_to_dotted_string(get_call_names(node))


class Arguments():
    """Represents arguments of a function."""

    def __init__(self, args):
        """Argument container class.

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
