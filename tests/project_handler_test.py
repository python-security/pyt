import os
import sys
import unittest
from pprint import pprint

sys.path.insert(0, os.path.abspath('../pyt'))
from project_handler import get_python_modules, is_python_module


class ProjectHandlerTest(unittest.TestCase):
    """Tests for the project handler."""

    def test_is_python_module(self):
        python_module = './project_handler_test.py'
        not_python_module = '../.travis.yml'

        self.assertEqual(is_python_module(python_module), True)
        self.assertEqual(is_python_module(not_python_module), False)

    def test_get_python_modules(self):
        project_folder = os.path.normpath(os.path.join('..', 'example', 'test_project'))

        project_namespace = 'test_project'
        folder = 'folder'
        directory = 'directory'

        modules = get_python_modules(project_folder)

        app_path = os.path.join(project_folder, 'app.py')
        utils_path = os.path.join(project_folder,'utils.py')
        exceptions_path = os.path.join(project_folder, 'exceptions.py')
        some_path = os.path.join(project_folder, folder, 'some.py')
        indhold_path = os.path.join(project_folder, folder, 'indhold.py')

        app_name = project_namespace + '.' + 'app'
        utils_name = project_namespace + '.' + 'utils'
        exceptions_name = project_namespace + '.' + 'exceptions'
        some_name = project_namespace + '.' + folder + '.some'
        indhold_name = project_namespace + '.' + folder + '.' + directory + '.indhold'

        app_tuple = (app_name, app_path)
        utils_tuple = (utils_name, utils_path)
        exceptions_tuple = (exceptions_name, exceptions_path)
        some_tuple = (some_name, some_path)

        self.assertIn(app_tuple, modules)
        self.assertIn(utils_tuple, modules)
        self.assertIn(exceptions_tuple, modules)
        self.assertIn(some_tuple, modules)

        self.assertEqual(len(modules), 5)
