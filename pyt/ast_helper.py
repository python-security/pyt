import ast
import os

def generate_ast(path):
    """Generate an Abstract Syntax Tree using the ast module."""
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return ast.parse(f.read())
    raise IOError('Input needs to be a file.')

def list_to_dotted_string(list_of_components):
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
    return list_to_dotted_string(get_call_names(node))

def get_call_names(node):
    result = list()
    return reversed(get_call_names_helper(node, result))
