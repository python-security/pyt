"""This module contains helper function useful when working with the ast module."""
import ast
import os

def generate_ast(path):
    """Generate an Abstract Syntax Tree using the ast module."""
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return ast.parse(f.read())
    raise IOError('Input needs to be a file. Path: ' + path)

def list_to_dotted_string(list_of_components):
    """Convert a list to a string seperated by a dot."""
    return '.'.join(list_of_components)
    
def get_call_names_helper(node, result):
    """Recursively finds all function names."""
    if isinstance(node, ast.Name):
        result.append(node.id)
        return result
    elif isinstance(node, ast.Call):
        return result
    elif isinstance(node, ast.Subscript):
        return result
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


class Arguments(object):
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
