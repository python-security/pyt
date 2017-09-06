import ast
import os

from .base_test_case import BaseTestCase
from pyt import trigger_definitions_parser, vulnerabilities
from pyt.ast_helper import get_call_names_as_string
from pyt.base_cfg import Node
from pyt.constraint_table import constraint_table, initialize_constraint_table
from pyt.fixed_point import analyse
from pyt.framework_adaptor import FrameworkAdaptor
from pyt.framework_helper import is_flask_route_function
from pyt.lattice import Lattice
from pyt.project_handler import get_directory_modules, get_modules
from pyt.reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class EngineTest(BaseTestCase):
    def run_analysis(self, path):
        path = os.path.normpath(path)

        project_modules = get_modules(os.path.dirname(path))
        local_modules = get_directory_modules(os.path.dirname(path))

        self.cfg_create_from_file(path, project_modules, local_modules)

        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_flask_route_function)

        initialize_constraint_table(cfg_list)

        analyse(cfg_list, analysis_type=ReachingDefinitionsTaintAnalysis)

        return vulnerabilities.find_vulnerabilities(cfg_list, ReachingDefinitionsTaintAnalysis)

    def test_find_vulnerabilities_absolute_from_file_command_injection(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/absolute_from_file_command_injection.py')

        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_absolute_from_file_command_injection_2(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/absolute_from_file_command_injection_2.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_no_false_positive_absolute_from_file_command_injection_3(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/no_false_positive_absolute_from_file_command_injection_3.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)

    def test_blackbox_library_call(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/blackbox_library_call.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerability_log.vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: example/vulnerable_code_across_files/blackbox_library_call.py
             > User input at line 12, trigger word "get(": 
                ¤call_1 = ret_request.args.get('suggestion')
            Reassigned in: 
                File: example/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 12: param = ¤call_1
                File: example/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 16: ¤call_2 = ret_scrypt.encrypt('echo ' + param + ' >> ' + 'menu.txt', 'password')
                File: example/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 16: command = ¤call_2
                File: example/vulnerable_code_across_files/blackbox_library_call.py
                 > Line 17: hey = command
            File: example/vulnerable_code_across_files/blackbox_library_call.py
             > reaches line 18, trigger word "subprocess.call(": 
                ¤call_3 = ret_subprocess.call(hey)
            This vulnerability is unknown due to:  Label: ¤call_2 = ret_scrypt.encrypt('echo ' + param + ' >> ' + 'menu.txt', 'password')
        """

        self.assertTrue(self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION))

    def test_builtin_with_user_defined_inner(self):
        vulnerability_log = self.run_analysis('example/nested_functions_code/builtin_with_user_defined_inner.py')
        logger.debug("vulnerability_log.vulnerabilities is %s", vulnerability_log.vulnerabilities)
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerability_log.vulnerabilities[0])
        logger.debug("vulnerability_description is %s", vulnerability_description)
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: example/nested_functions_code/builtin_with_user_defined_inner.py
             > User input at line 20, trigger word "form[": 
                req_param = request.form['suggestion']
            Reassigned in: 
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 14: save_2_req_param = req_param
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 23: temp_2_inner_arg = req_param
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 14: inner_arg = temp_2_inner_arg
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 15: yes_vuln = inner_arg + 'hey'
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 16: ret_inner = yes_vuln
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 14: req_param = inner_arg
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 23: ¤call_2 = ret_inner
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 23: ¤call_1 = ret_scrypt.encrypt(¤call_2)
                File: example/nested_functions_code/builtin_with_user_defined_inner.py
                 > Line 23: foo = ¤call_1
            File: example/nested_functions_code/builtin_with_user_defined_inner.py
             > reaches line 24, trigger word "subprocess.call(": 
                ¤call_3 = ret_subprocess.call(foo)
            This vulnerability is unknown due to:  Label: ¤call_1 = ret_scrypt.encrypt(¤call_2)
        """
        self.assertTrue(self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION))

    def test_sink_with_result_of_user_defined_nested(self):
        vulnerability_log = self.run_analysis('example/nested_functions_code/sink_with_result_of_user_defined_nested.py')
        logger.debug("vulnerability_log.vulnerabilities is %s", vulnerability_log.vulnerabilities)
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerability_log.vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
             > User input at line 16, trigger word "form[": 
                req_param = request.form['suggestion']
            Reassigned in: 
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 6: save_1_req_param = req_param
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 10: save_2_req_param = req_param
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: temp_2_inner_arg = req_param
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 10: inner_arg = temp_2_inner_arg
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 11: inner_ret_val = inner_arg + 'hey'
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 12: ret_inner = inner_ret_val
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 10: req_param = inner_arg
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: ¤call_2 = ret_inner
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: temp_1_outer_arg = ¤call_2
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 6: outer_arg = temp_1_outer_arg
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 7: outer_ret_val = outer_arg + 'hey'
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 8: ret_outer = outer_ret_val
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 6: req_param = save_1_req_param
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: ¤call_1 = ret_outer
                File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
                 > Line 17: result = ¤call_1
            File: example/nested_functions_code/sink_with_result_of_user_defined_nested.py
             > reaches line 18, trigger word "subprocess.call(": 
                ¤call_3 = ret_subprocess.call(result,shell=True)
        """
        self.assertTrue(self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION))
        
    def test_sink_with_user_defined_inner(self):
        vulnerability_log = self.run_analysis('example/nested_functions_code/sink_with_user_defined_inner.py')
        logger.debug("vulnerability_log.vulnerabilities is %s", vulnerability_log.vulnerabilities)
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerability_log.vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: example/nested_functions_code/sink_with_user_defined_inner.py
             > User input at line 16, trigger word "form[": 
                req_param = request.form['suggestion']
            Reassigned in: 
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 6: save_2_req_param = req_param
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 10: save_3_req_param = req_param
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: temp_3_inner_arg = req_param
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 10: inner_arg = temp_3_inner_arg
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 11: inner_ret_val = inner_arg + 'hey'
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 12: ret_inner = inner_ret_val
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 10: req_param = inner_arg
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: ¤call_3 = ret_inner
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: temp_2_outer_arg = ¤call_3
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 6: outer_arg = temp_2_outer_arg
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 7: outer_ret_val = outer_arg + 'hey'
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 8: ret_outer = outer_ret_val
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 6: req_param = save_2_req_param
                File: example/nested_functions_code/sink_with_user_defined_inner.py
                 > Line 18: ¤call_2 = ret_outer
            File: example/nested_functions_code/sink_with_user_defined_inner.py
             > reaches line 18, trigger word "subprocess.call(": 
                ¤call_1 = ret_subprocess.call(outer(inner(req_param)),shell=True)
        """
        self.assertTrue(self.string_compare_alpha(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION))

    def test_find_vulnerabilities_import_file_command_injection(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/import_file_command_injection.py')

        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_import_file_command_injection_2(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/import_file_command_injection_2.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_no_false_positive_import_file_command_injection_3(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/no_false_positive_import_file_command_injection_3.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)
