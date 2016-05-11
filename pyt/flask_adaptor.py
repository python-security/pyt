"""Contains a class that can be used as adaptor."""
import ast

from framework_adaptor import FrameworkAdaptor
from cfg import CFG
from project_handler import get_python_modules

class FlaskAdaptor(FrameworkAdaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def is_flask_route_function(self, ast_node):
        """Check whether function uses a decorator."""
        for decorator in ast_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if decorator.func.attr == 'route':
                    return True
        return False

    def get_cfg(self, ast_node, cfg):
        cfg = CFG(cfg.project_modules)
        cfg.create(ast_node)
        return cfg

    def find_flask_route_functions(self, cfg):
        """Find all flask functions with decorators."""
        for ast_node in cfg.module_definitions.items():
            if self.is_flask_route_function(ast_node[1]):
                yield self.get_cfg(ast_node[1], cfg)

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for cfg in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions(cfg))
        self.cfg_list.extend(function_cfgs)
