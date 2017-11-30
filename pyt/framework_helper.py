"""Provides helper functions that help with determining if a function is a route function."""
import ast

from pyt.base_cfg import Function
from .ast_helper import get_call_names, Arguments


def is_function(function):
    """Always returns true because arg is always a function."""
    return True


def is_flask_route_function(ast_node):
    """Check whether function uses a route decorator."""
    for decorator in ast_node.decorator_list:
        if isinstance(decorator, ast.Call):
            if _get_last_of_iterable(get_call_names(decorator.func)) == 'route':
                return True
    return False


def is_django_view_function(ast_node):
    arguments = Arguments(ast_node.args)
    if 'request' in arguments:
        return True
    return False


def is_function_without_leading_(ast_node):
    if ast_node.name.startswith('_'):
        return False
    return True


def _get_last_of_iterable(iterable):
    """Get last element of iterable."""
    item = None
    for item in iterable:
        pass
    return item
