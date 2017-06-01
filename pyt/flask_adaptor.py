"""Adaptor for Flask web applications."""
import ast

from .ast_helper import Arguments, get_call_names
from .framework_adaptor import FrameworkAdaptor, TaintedNode
from .interprocedural_cfg import interprocedural
from .module_definitions import project_definitions


class FlaskAdaptor(FrameworkAdaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def get_last(self, iterator):
        """Get last element of iterator."""
        item = None
        for item in iterator:
            pass
        return item

    def is_flask_route_function(self, ast_node):
        """Check whether function uses a decorator."""
        for decorator in ast_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if self.get_last(get_call_names(decorator.func)) == 'route':
                    return True
        return False

    def get_cfg(self, definition):
        """Build a function cfg and return it."""
        cfg = interprocedural(definition.node, self.project_modules,
                              self.local_modules, definition.path,
                              definition.module_definitions)

        args = Arguments(definition.node.args)

        if args:
            definition_lineno = definition.node.lineno

            cfg.nodes[0].outgoing = list()
            cfg.nodes[1].ingoing = list()

            for i, argument in enumerate(args, 1):
                taint = TaintedNode(argument, argument, None, [], line_number=definition_lineno, path=definition.path)
                previous_node = cfg.nodes[0]
                previous_node.connect(taint)
                cfg.nodes.insert(1, taint)

            last_inserted = cfg.nodes[i]
            after_last = cfg.nodes[i+1]
            last_inserted.connect(after_last)

        return cfg

    def get_func_nodes(self):
        """Get all nodes from a function."""
        return [definition for definition in project_definitions.values() if isinstance(definition.node, ast.FunctionDef)]

    def find_flask_route_functions(self, cfg):
        """Find all flask functions with decorators."""
        for definition in self.get_func_nodes():
            if definition.node and self.is_flask_route_function(definition.node):
                yield self.get_cfg(definition)

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for cfg in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions(cfg))
        self.cfg_list.extend(function_cfgs)
