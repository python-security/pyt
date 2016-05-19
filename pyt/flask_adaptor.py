"""Contains a class that can be used as adaptor."""
import ast

from framework_adaptor import FrameworkAdaptor
from ast_helper import get_call_names
from cfg import build_cfg, build_function_cfg
from project_handler import get_python_modules
from module_definitions import project_definitions

class FlaskAdaptor(FrameworkAdaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def get_last(self, iterator):
        """Get last element of iterator.(Python is awesome!)."""
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

    def get_cfg(self, ast_node):
        """Build a function cfg and return it."""
        cfg = build_function_cfg(ast_node, self.project_modules, self.local_modules)
        return cfg

    def get_func_nodes(self):
        """Get all nodes from a function."""
        return [definition.node for definition in project_definitions.values() if isinstance(definition.node, ast.FunctionDef)]

    def find_flask_route_functions(self, cfg):
        """Find all flask functions with decorators."""
        for ast_node in self.get_func_nodes():
            if ast_node and self.is_flask_route_function(ast_node):
                yield self.get_cfg(ast_node)

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for cfg in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions(cfg))
        self.cfg_list.extend(function_cfgs)
