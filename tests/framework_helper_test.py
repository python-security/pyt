from .base_test_case import BaseTestCase
from pyt.framework_adaptor import _get_func_nodes
from pyt.framework_helper import (
    is_flask_route_function,
    is_function
)

class FrameworkEngineTest(BaseTestCase):
    def test_find_flask_functions(self):
        self.cfg_create_from_file('example/example_inputs/flask_function_and_normal_function.py')

        cfg_list = [self.cfg]
        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_flask_route_function(func.node):
                self.assertEqual(func.node.name, 'flask_function')
                i = i + 1
        # So it is supposed to be 1, because foo is not an app.route
        self.assertEqual(i, 1)

    def test_find_every_function(self):
        self.cfg_create_from_file('example/example_inputs/flask_function_and_normal_function.py')

        cfg_list = [self.cfg]
        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_function(func.node):
                i = i + 1
        # So it is supposed to be 2, because we count all functions
        self.assertEqual(len(funcs), 2)
