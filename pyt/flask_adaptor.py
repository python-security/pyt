"""Contains a class that can be used as adaptor."""
import ast

from framework_adaptor import FrameworkAdaptor


class FlaskAdaptor(FrameworkAdaptor):
    """The flask adaptor class manipulates the CFG to adapt to flask applications."""

    def is_flask_route_function(self, ast_node):
        """Check whether function uses a decorator."""
        for decorator in ast_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if decorator.func.value.id == 'app' and decorator.func.attr == 'route':
                    return True
        return False

    def find_flask_route_functions(self, module_definitions):
        """Find all flask functions with decorators."""
        for ast_node in module_definitions.items():
            if self.is_flask_route_function(ast_node[1]):
                yield ast_node[1]

    def run(self):
        """Executed by the super class, everything that needs to be executed goes here."""
        function_cfgs = list()
        for cfg in self.cfg_list:
            function_cfgs.extend(self.find_flask_route_functions(cfg.module_definitions))
        self.cfg_list.extend(function_cfgs)
