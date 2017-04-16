# import os.path

# from .base_test_case import BaseTestCase
# from pyt.project_handler import get_directory_modules, get_modules_and_packages


# class NestedTest(BaseTestCase):
    # def test_nested_function_calls(self):

    #     path = os.path.normpath('example/nested_functions_code/nested_function_calls.py')

    #     project_modules = get_modules_and_packages(os.path.dirname(path))
    #     local_modules = get_directory_modules(os.path.dirname(path))

    #     self.cfg_create_from_file(path, project_modules, local_modules)

    #     EXPECTED = ['Not Yet']

    #     for node, expected_label in zip(self.cfg.nodes, EXPECTED):
    #         self.assertEqual(node.label, expected_label)
