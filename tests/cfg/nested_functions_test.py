import os.path

from ..base_test_case import BaseTestCase
from ..test_utils import get_modules_and_packages

from pyt.core.project_handler import get_directory_modules


class NestedTest(BaseTestCase):
    def test_nested_user_defined_function_calls(self):

        path = os.path.normpath('examples/nested_functions_code/nested_user_defined_function_calls.py')

        project_modules = get_modules_and_packages(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        EXPECTED = ["Entry module",
                    "foo = 'bar'",
                    "save_1_foo = foo",
                    "save_2_foo = foo",
                    "temp_2_inner_arg = foo",
                    "inner_arg = temp_2_inner_arg",
                    "Function Entry inner",
                    "inner_ret_val = inner_arg + 'hey'",
                    "ret_inner = inner_ret_val",
                    "Exit inner",
                    "foo = save_2_foo",
                    "~call_2 = ret_inner",
                    "temp_1_outer_arg = ~call_2",
                    "outer_arg = temp_1_outer_arg",
                    "Function Entry outer",
                    "outer_ret_val = outer_arg + 'hey'",
                    "ret_outer = outer_ret_val",
                    "Exit outer",
                    "foo = save_1_foo",
                    "~call_1 = ret_outer",
                    "abc = ~call_1",
                    "Exit module"]

        for node, expected_label in zip(self.cfg.nodes, EXPECTED):
            self.assertEqual(node.label, expected_label)
