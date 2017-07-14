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

    # This fails due to a false positive in get_vulnerability
    # def test_absolute_from_file_does_not_exist(self):
    #     vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/absolute_from_file_does_not_exist.py')
    #     self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)

    def test_find_vulnerabilities_import_file_command_injection(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/import_file_command_injection.py')

        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_import_file_command_injection_2(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/import_file_command_injection_2.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_no_false_positive_import_file_command_injection_3(self):
        vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/no_false_positive_import_file_command_injection_3.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)

    # This fails due to a false positive in get_vulnerability
    # def test_import_file_does_not_exist(self):
    #     vulnerability_log = self.run_analysis('example/vulnerable_code_across_files/import_file_does_not_exist.py')
    #     self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)
