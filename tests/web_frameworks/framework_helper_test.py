from ..base_test_case import BaseTestCase

from pyt.web_frameworks import (
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_,
    _get_func_nodes
)


class FrameworkEngineTest(BaseTestCase):
    def test_find_flask_functions(self):
        self.cfg_create_from_file('examples/example_inputs/django_flask_and_normal_functions.py')

        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_flask_route_function(func.node):
                self.assertEqual(func.node.name, 'flask_function')
                i = i + 1
        # So it is supposed to be 1, because foo is not an app.route
        self.assertEqual(i, 1)

    def test_find_every_function_without_leading_underscore(self):
        self.cfg_create_from_file('examples/example_inputs/django_flask_and_normal_functions.py')

        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_function_without_leading_(func.node):
                i = i + 1
        # So it is supposed to be 3, because we count all functions without a leading underscore
        self.assertEqual(i, 3)

    def test_find_every_function(self):
        self.cfg_create_from_file('examples/example_inputs/django_flask_and_normal_functions.py')

        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_function(func.node):
                i = i + 1
        # So it is supposed to be 4, because we count all functions
        self.assertEqual(len(funcs), 4)

    def test_find_django_functions(self):
        self.cfg_create_from_file('examples/example_inputs/django_flask_and_normal_functions.py')

        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_django_view_function(func.node):
                self.assertEqual(func.node.name, 'django_function')
                i = i + 1
        # So it is supposed to be 1
        self.assertEqual(i, 1)

    def test_find_django_views(self):
        self.cfg_create_from_file('examples/example_inputs/django_views.py')

        funcs = _get_func_nodes()

        i = 0
        for func in funcs:
            if is_django_view_function(func.node):
                self.assertIn('view_function', func.node.name)
                i = i + 1
        # So it is supposed to be 2
        self.assertEqual(i, 2)
