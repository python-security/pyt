import os
import unittest

from ..test_utils import get_modules_and_packages

from pyt.core.project_handler import (
    get_modules,
    _is_python_file
)


class ProjectHandlerTest(unittest.TestCase):
    """Tests for the project handler."""

    def test_is_python_file(self):
        python_module = './project_handler_test.py'
        not_python_module = '../.travis.yml'

        self.assertEqual(_is_python_file(python_module), True)
        self.assertEqual(_is_python_file(not_python_module), False)

    def test_get_modules(self):
        project_folder = os.path.normpath(os.path.join('examples', 'test_project'))

        project_namespace = 'test_project'
        folder = 'folder'
        directory = 'directory'

        modules = get_modules(project_folder)

        app_path = os.path.join(project_folder, 'app.py')
        utils_path = os.path.join(project_folder, 'utils.py')
        exceptions_path = os.path.join(project_folder, 'exceptions.py')
        some_path = os.path.join(project_folder, folder, 'some.py')
        __init__path = os.path.join(project_folder, folder)
        indhold_path = os.path.join(project_folder, folder, directory, 'indhold.py')

        # relative_folder_name = '.' + folder
        app_name = project_namespace + '.' + 'app'
        utils_name = project_namespace + '.' + 'utils'
        exceptions_name = project_namespace + '.' + 'exceptions'
        some_name = project_namespace + '.' + folder + '.some'
        __init__name = project_namespace + '.' + folder
        indhold_name = project_namespace + '.' + folder + '.' + directory + '.indhold'

        app_tuple = (app_name, app_path)
        utils_tuple = (utils_name, utils_path)
        exceptions_tuple = (exceptions_name, exceptions_path)
        some_tuple = (some_name, some_path)
        __init__tuple = (__init__name, __init__path)
        indhold_tuple = (indhold_name, indhold_path)

        self.assertIn(app_tuple, modules)
        self.assertIn(utils_tuple, modules)
        self.assertIn(exceptions_tuple, modules)
        self.assertIn(some_tuple, modules)
        self.assertIn(__init__tuple, modules)
        self.assertIn(indhold_tuple, modules)

        self.assertEqual(len(modules), 6)

    def test_get_modules_no_prepend_root(self):
        project_folder = os.path.normpath(os.path.join('examples', 'test_project'))

        folder = 'folder'
        directory = 'directory'

        modules = get_modules(project_folder, prepend_module_root=False)

        app_path = os.path.join(project_folder, 'app.py')
        __init__path = os.path.join(project_folder, folder)
        indhold_path = os.path.join(project_folder, folder, directory, 'indhold.py')

        app_name = 'app'
        __init__name = folder
        indhold_name = folder + '.' + directory + '.indhold'

        app_tuple = (app_name, app_path)
        __init__tuple = (__init__name, __init__path)
        indhold_tuple = (indhold_name, indhold_path)

        self.assertIn(app_tuple, modules)
        self.assertIn(__init__tuple, modules)
        self.assertIn(indhold_tuple, modules)

        self.assertEqual(len(modules), 6)

    def test_get_modules_and_packages(self):
        project_folder = os.path.normpath(os.path.join('examples', 'test_project'))

        project_namespace = 'test_project'
        folder = 'folder'
        directory = 'directory'

        modules = get_modules_and_packages(project_folder)

        folder_path = os.path.join(project_folder, folder)
        app_path = os.path.join(project_folder, 'app.py')
        exceptions_path = os.path.join(project_folder, 'exceptions.py')
        utils_path = os.path.join(project_folder, 'utils.py')
        # directory_path = os.path.join(project_folder, folder, directory)
        some_path = os.path.join(project_folder, folder, 'some.py')
        indhold_path = os.path.join(project_folder, folder, directory, 'indhold.py')

        relative_folder_name = '.' + folder
        app_name = project_namespace + '.' + 'app'
        exceptions_name = project_namespace + '.' + 'exceptions'
        utils_name = project_namespace + '.' + 'utils'
        # relative_directory_name = '.' + folder + '.' + directory
        some_name = project_namespace + '.' + folder + '.some'
        indhold_name = project_namespace + '.' + folder + '.' + directory + '.indhold'

        folder_tuple = (
            relative_folder_name[1:],
            folder_path,
            relative_folder_name
        )
        app_tuple = (app_name, app_path)
        exceptions_tuple = (exceptions_name, exceptions_path)
        utils_tuple = (utils_name, utils_path)
        # directory_tuple = (
        #     relative_directory_name[1:],
        #     directory_path,
        #     relative_directory_name
        # )
        some_tuple = (some_name, some_path)
        indhold_tuple = (indhold_name, indhold_path)

        self.assertIn(folder_tuple, modules)
        self.assertIn(app_tuple, modules)
        self.assertIn(exceptions_tuple, modules)
        self.assertIn(utils_tuple, modules)
        self.assertIn(folder_tuple, modules)
        self.assertIn(some_tuple, modules)
        self.assertIn(indhold_tuple, modules)

        self.assertEqual(len(modules), 8)
