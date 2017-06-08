"""Adaptor for Flask web applications."""
import ast

from .ast_helper import Arguments, get_call_names
from .framework_adaptor import FrameworkAdaptor, TaintedNode
from .interprocedural_cfg import interprocedural
from .module_definitions import project_definitions

class FlaskAdaptor(FrameworkAdaptor):
    """The Flask adaptor class manipulates the CFG to adapt to Flask applications."""

    def get_func_cfg_with_tainted_args(self, definition):
        """Build a function cfg and return it."""
        func_cfg = interprocedural(definition.node, self.project_modules,
                                   self.local_modules, definition.path,
                                   definition.module_definitions)

        args = Arguments(definition.node.args)
        if args:
            function_entry_node = func_cfg.nodes[0]
            function_entry_node.outgoing = []
            first_node_after_args = func_cfg.nodes[1]
            first_node_after_args.ingoing = []

            # We're just gonna give all the tainted args the lineno of the def
            definition_lineno = definition.node.lineno

            # Taint all the arguments
            for arg in args:
                tainted_node = TaintedNode(arg, arg,
                                           None, [],
                                           line_number=definition_lineno,
                                           path=definition.path)
                function_entry_node.connect(tainted_node)
                # 1 and not 0 for Entry Node to remain first in the list
                func_cfg.nodes.insert(1, tainted_node)

            first_arg = func_cfg.nodes[len(args)]
            first_arg.connect(first_node_after_args)

        return func_cfg

    def find_flask_route_functions(self):
        """Find all Flask functions with route decorators.

        Yields:
            CFG of a Flask function.
        """
        for definition in get_func_nodes():
            if definition.node and is_flask_route_function(definition.node):
                yield self.get_func_cfg_with_tainted_args(definition)

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for _ in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions())
        self.cfg_list.extend(function_cfgs)

def get_func_nodes():
    """Get all function nodes."""
    return [definition for definition in project_definitions.values() \
            if isinstance(definition.node, ast.FunctionDef)]


def is_flask_route_function(ast_node):
    """Check whether function uses a decorator."""
    for decorator in ast_node.decorator_list:
        if isinstance(decorator, ast.Call):
            if get_last_of_iterable(get_call_names(decorator.func)) == 'route':
                return True
    return False


def get_last_of_iterable(iterable):
    """Get last element of iterable."""
    item = None
    for item in iterable:
        pass
    return item
