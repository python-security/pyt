"""Contains a class that can be used as adaptor."""
import ast

from framework_adaptor import FrameworkAdaptor
from cfg import CFG, get_call_names
from project_handler import get_python_modules
from module_definitions import project_definitions

class FlaskAdaptor(FrameworkAdaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def is_flask_route_function(self, ast_node):
        """Check whether function uses a decorator."""
        for decorator in ast_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if get_call_names(decorator.func) == 'route':
                    return True
        return False

    def get_cfg(self, ast_node, cfg):
        cfg = CFG(cfg.project_modules)
        cfg.create_function(ast_node)
        return cfg

    def get_func_nodes(self):
        return (definition.node for definition in project_definitions if isinstance(definition.node, ast.FunctionDef))

    def find_flask_route_functions(self, cfg):
        """Find all flask functions with decorators."""
        for ast_node in self.get_func_nodes():
            if ast_node and self.is_flask_route_function(ast_node):
                yield self.get_cfg(ast_node, cfg)

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for cfg in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions(cfg))
        self.cfg_list.extend(function_cfgs)
