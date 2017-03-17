import ast
import os

from .base_test_case import BaseTestCase
from pyt.ast_helper import get_call_names_as_string
from pyt.project_handler import get_directory_modules, get_python_modules


class ImportTest(BaseTestCase):
    def test_import(self):
        path = os.path.normpath('example/import_test_project/main.py')

        project_modules = get_python_modules(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        EXPECTED = ['Entry module',
                    'Module Entry A',
                    'Module Exit A',
                    'Module Entry A',
                    'Module Exit A',
                    'temp_1_s = \'str\'',
                    's = temp_1_s',
                    'Function Entry B',
                    'ret_B = s',
                    'Exit B',
                    '¤call_1 = ret_B',
                    'b = ¤call_1',
                    'c = A.B(\'sss\')',
                    'd = D.a(\'hey\')',
                    'Exit module']

        for node, expected_label in zip(self.cfg.nodes, EXPECTED):
            self.assertEqual(node.label, expected_label)

    def test_relative_level_1(self):
        path = os.path.normpath('example/import_test_project/relative_level_1.py')

        project_modules = get_python_modules(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        EXPECTED = ['Entry module',
                    'Module Entry A',
                    'Module Exit A',
                    'Module Entry A',
                    'Module Exit A',
                    'temp_1_s = \'str\'',
                    's = temp_1_s',
                    'Function Entry B',
                    'ret_B = s',
                    'Exit B',
                    '¤call_1 = ret_B',
                    'b = ¤call_1',
                    'c = A.B(\'sss\')',
                    'Exit module']

        for node, expected_label in zip(self.cfg.nodes, EXPECTED):
            self.assertEqual(node.label, expected_label)

    def test_relative_level_2(self):
        path = os.path.normpath('example/import_test_project/relative_level_2.py')

        project_modules = get_python_modules(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        try:
            self.cfg_create_from_file(path, project_modules, local_modules)
        except Exception as e:
            self.assertTrue("OSError('Input needs to be a file. Path: " in repr(e))
            self.assertTrue("example/A.py" in repr(e))

    def test_relative_between_folders(self):
        file_path = os.path.normpath('example/import_test_project/other_dir/relative_between_folders.py')
        project_path = os.path.normpath('example/import_test_project/h.py')

        project_modules = get_python_modules(os.path.dirname(project_path))
        local_modules = get_directory_modules(os.path.dirname(project_path))

        self.cfg_create_from_file(file_path, project_modules, local_modules)

        EXPECTED = ['Entry module',
                    'Module Entry foo.bar',
                    'Module Exit foo.bar',
                    'temp_1_s = \'hey\'',
                    's = temp_1_s',
                    'Function Entry H',
                    'ret_H = s',
                    'Exit H',
                    '¤call_1 = ret_H',
                    'result = ¤call_1',
                    'Exit module']

        for node, expected_label in zip(self.cfg.nodes, EXPECTED):
            self.assertEqual(node.label, expected_label)

    def test_get_call_names_single(self):
        m = ast.parse('hi(a)')
        call = m.body[0].value

        result = get_call_names_as_string(call.func)

        self.assertEqual(result, 'hi')

    def test_get_call_names_uselesscase(self):
        m = ast.parse('defg.hi(a)')
        call = m.body[0].value

        result = get_call_names_as_string(call.func)

        self.assertEqual(result, 'defg.hi')


    def test_get_call_names_multi(self):
        m = ast.parse('abc.defg.hi(a)')
        call = m.body[0].value

        result = get_call_names_as_string(call.func)

        self.assertEqual(result, 'abc.defg.hi')
