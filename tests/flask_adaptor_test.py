from .base_test_case import BaseTestCase
from pyt.flask_adaptor import FlaskAdaptor


class FlaskEngineTest(BaseTestCase):
    def test_find_flask_functions(self):

        self.cfg_create_from_file('example/example_inputs/flask_function_and_normal_function.py')

        cfg_list = [self.cfg]

        flask = FlaskAdaptor(cfg_list, list(), list())
        funcs = flask.get_func_nodes()

        i = 0
        for func in funcs:
            if flask.is_flask_route_function(func.node):
                self.assertEqual(func.node.name, 'flask_function')
                i = i + 1
        # So it is supposed to be 1, because foo is not an app.route
        self.assertEqual(i, 1)
