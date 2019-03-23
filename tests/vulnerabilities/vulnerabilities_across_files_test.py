import os

from .vulnerabilities_base_test_case import VulnerabilitiesBaseTestCase

from pyt.analysis.constraint_table import initialize_constraint_table
from pyt.analysis.fixed_point import analyse
from pyt.core.project_handler import (
    get_directory_modules,
    get_modules
)
from pyt.usage import (
    default_blackbox_mapping_file,
    default_trigger_word_file
)
from pyt.vulnerabilities import find_vulnerabilities
from pyt.web_frameworks import (
    FrameworkAdaptor,
    is_flask_route_function
)


class EngineTest(VulnerabilitiesBaseTestCase):
    def run_analysis(self, path):
        path = os.path.normpath(path)

        project_modules = get_modules(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_flask_route_function)

        initialize_constraint_table(cfg_list)

        analyse(cfg_list)

        return find_vulnerabilities(
            cfg_list,
            default_blackbox_mapping_file,
            default_trigger_word_file
        )

    def test_find_vulnerabilities_absolute_from_file_command_injection(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/absolute_from_file_command_injection.py')

        self.assert_length(vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_absolute_from_file_command_injection_2(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/absolute_from_file_command_injection_2.py')
        self.assert_length(vulnerabilities, expected_length=1)

    def test_no_false_positive_absolute_from_file_command_injection_3(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/no_false_positive_absolute_from_file_command_injection_3.py')  # noqa: E501
        self.assert_length(vulnerabilities, expected_length=0)

    def test_blackbox_library_call(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/blackbox_library_call.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code_across_files/blackbox_library_call.py
             > User input at line 12, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('suggestion')
            Reassigned in:
                File: examples/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 12: param = ~call_1
                File: examples/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 15: ~call_2 = ret_scrypt.encrypt('echo ' + param + ' >> ' + 'menu.txt', 'password')
                File: examples/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 15: command = ~call_2
                File: examples/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 16: hey = command
            File: examples/vulnerable_code_across_files/blackbox_library_call.py
             > reaches line 17, sink "subprocess.call(":
                ~call_3 = ret_subprocess.call(hey, shell=True)
            This vulnerability is unknown due to:
                Label: ~call_2 = ret_scrypt.encrypt('echo ' + param + ' >> ' + 'menu.txt', 'password')
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_builtin_with_user_defined_inner(self):
        vulnerabilities = self.run_analysis('examples/nested_functions_code/builtin_with_user_defined_inner.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/builtin_with_user_defined_inner.py
             > User input at line 16, source "form[":
                 req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 10: save_2_req_param = req_param
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 19: temp_2_inner_arg = req_param
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 10: inner_arg = temp_2_inner_arg
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 11: yes_vuln = inner_arg + 'hey'
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 12: ret_inner = yes_vuln
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 19: ~call_2 = ret_inner
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 19: ~call_1 = ret_scrypt.encrypt(~call_2)
                File: examples/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 19: foo = ~call_1
            File: examples/nested_functions_code/builtin_with_user_defined_inner.py
             > reaches line 20, sink "subprocess.call(":
                ~call_3 = ret_subprocess.call(foo, shell=True)
            This vulnerability is unknown due to:  Label: ~call_1 = ret_scrypt.encrypt(~call_2)
        """
        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_sink_with_result_of_blackbox_nested(self):
        vulnerabilities = self.run_analysis('examples/nested_functions_code/sink_with_result_of_blackbox_nested.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
             > User input at line 12, source "form[":
                req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: ~call_2 = ret_scrypt.encrypt(req_param)
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: ~call_1 = ret_scrypt.encrypt(~call_2)
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: result = ~call_1
            File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
             > reaches line 14, sink "subprocess.call(":
                ~call_3 = ret_subprocess.call(result, shell=True)
            This vulnerability is unknown due to:  Label: ~call_2 = ret_scrypt.encrypt(req_param)
        """
        OTHER_EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
             > User input at line 12, source "form[":
                req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: ~call_2 = ret_scrypt.encrypt(req_param)
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: ~call_1 = ret_scrypt.encrypt(~call_2)
                File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
                 > Line 13: result = ~call_1
            File: examples/nested_functions_code/sink_with_result_of_blackbox_nested.py
             > reaches line 14, sink "subprocess.call(":
                ~call_3 = ret_subprocess.call(result, shell=True)
            This vulnerability is unknown due to:  Label: ~call_1 = ret_scrypt.encrypt(~call_2)
        """
        self.assertTrue(
            self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION) or
            self.string_compare_alpha(vulnerability_description, OTHER_EXPECTED_VULNERABILITY_DESCRIPTION)
        )

    def test_sink_with_result_of_user_defined_nested(self):
        vulnerabilities = self.run_analysis('examples/nested_functions_code/sink_with_result_of_user_defined_nested.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
             > User input at line 16, source "form[":
                 req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 6: save_1_req_param = req_param
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 10: save_2_req_param = req_param
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: temp_2_inner_arg = req_param
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 10: inner_arg = temp_2_inner_arg
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 11: inner_ret_val = inner_arg + 'hey'
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 12: ret_inner = inner_ret_val
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: ~call_2 = ret_inner
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: temp_1_outer_arg = ~call_2
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 6: outer_arg = temp_1_outer_arg
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 7: outer_ret_val = outer_arg + 'hey'
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 8: ret_outer = outer_ret_val
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: ~call_1 = ret_outer
                File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: result = ~call_1
            File: examples/nested_functions_code/sink_with_result_of_user_defined_nested.py
             > reaches line 18, sink "subprocess.call(":
                ~call_3 = ret_subprocess.call(result, shell=True)
        """
        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_sink_with_blackbox_inner(self):
        vulnerabilities = self.run_analysis('examples/nested_functions_code/sink_with_blackbox_inner.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_blackbox_inner.py
             > User input at line 12, source "form[":
                req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_blackbox_inner.py
                 > Line 14: ~call_3 = ret_scrypt.encypt(req_param)
                File: examples/nested_functions_code/sink_with_blackbox_inner.py
                 > Line 14: ~call_2 = ret_scrypt.encypt(~call_3)
            File: examples/nested_functions_code/sink_with_blackbox_inner.py
             > reaches line 14, sink "subprocess.call(":
                ~call_1 = ret_subprocess.call(~call_2, shell=True)
            This vulnerability is unknown due to:  Label: ~call_2 = ret_scrypt.encypt(~call_3)
        """

        OTHER_EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_blackbox_inner.py
             > User input at line 12, source "form[":
                req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_blackbox_inner.py
                 > Line 14: ~call_3 = ret_scrypt.encypt(req_param)
                File: examples/nested_functions_code/sink_with_blackbox_inner.py
                 > Line 14: ~call_2 = ret_scrypt.encypt(~call_3)
            File: examples/nested_functions_code/sink_with_blackbox_inner.py
             > reaches line 14, sink "subprocess.call(":
                ~call_1 = ret_subprocess.call(~call_2, shell=True)
            This vulnerability is unknown due to:  Label: ~call_3 = ret_scrypt.encypt(req_param)
        """
        self.assertTrue(
            self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION) or
            self.string_compare_alpha(vulnerability_description, OTHER_EXPECTED_VULNERABILITY_DESCRIPTION)
        )

    def test_sink_with_user_defined_inner(self):
        vulnerabilities = self.run_analysis('examples/nested_functions_code/sink_with_user_defined_inner.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/nested_functions_code/sink_with_user_defined_inner.py
             > User input at line 16, source "form[":
                 req_param = request.form['suggestion']
            Reassigned in:
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 6: save_2_req_param = req_param
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 10: save_3_req_param = req_param
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: temp_3_inner_arg = req_param
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 10: inner_arg = temp_3_inner_arg
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 11: inner_ret_val = inner_arg + 'hey'
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 12: ret_inner = inner_ret_val
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: ~call_3 = ret_inner
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: temp_2_outer_arg = ~call_3
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 6: outer_arg = temp_2_outer_arg
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 7: outer_ret_val = outer_arg + 'hey'
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 8: ret_outer = outer_ret_val
                File: examples/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: ~call_2 = ret_outer
            File: examples/nested_functions_code/sink_with_user_defined_inner.py
             > reaches line 18, sink "subprocess.call(":
                ~call_1 = ret_subprocess.call(~call_2, shell=True)
        """
        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_find_vulnerabilities_import_file_command_injection(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/import_file_command_injection.py')

        self.assert_length(vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_import_file_command_injection_2(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/import_file_command_injection_2.py')
        self.assert_length(vulnerabilities, expected_length=1)

    def test_no_false_positive_import_file_command_injection_3(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code_across_files/no_false_positive_import_file_command_injection_3.py')  # noqa: E501
        self.assert_length(vulnerabilities, expected_length=0)
