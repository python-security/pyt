import os
import sys

sys.path.insert(1, os.path.abspath('../pyt'))
import vulnerabilities
import trigger_definitions_parser
from base_test_case import BaseTestCase
from base_cfg import Node
from fixed_point import analyse
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from flask_adaptor import FlaskAdaptor
from lattice import Lattice
from constraint_table import constraint_table, initialize_constraint_table


class EngineTest(BaseTestCase):
    def run_empty(self):
        return

    def get_lattice_elements(self, cfg_nodes):
        """Dummy analysis method"""
        return cfg_nodes

    def test_parse(self):
        definitions = vulnerabilities.parse(trigger_word_file=os.path.join(os.getcwd().replace('tests','pyt'), 'trigger_definitions', 'test_triggers.pyt'))

        self.assert_length(definitions.sources, expected_length=1)
        self.assert_length(definitions.sinks, expected_length=3)
        self.assert_length(definitions.sinks[0][1], expected_length=1)
        self.assert_length(definitions.sinks[1][1], expected_length=3)

    def test_parse_section(self):
        l = list(trigger_definitions_parser.parse_section(iter(['get'])))
        self.assert_length(l, expected_length=1)
        self.assertEqual(l[0][0], 'get')
        self.assertEqual(l[0][1], list())

        l = list(trigger_definitions_parser.parse_section(iter(['get', 'get -> a, b, c d s aq     a'])))
        self.assert_length(l, expected_length=2)
        self.assertEqual(l[0][0], 'get')
        self.assertEqual(l[1][0], 'get')
        self.assertEqual(l[1][1], ['a', 'b', 'c d s aq     a'])
        self.assert_length(l[1][1], expected_length=3)

    def test_label_contains(self):
        cfg_node = Node('label', None, line_number=None, path=None)
        trigger_words = [('get', [])]
        l = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=0)

        cfg_node = Node('request.get("stefan")', None, line_number=None, path=None)
        trigger_words = [('get', []), ('request', [])]
        l = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=2)

        trigger_node_1 = l[0]
        trigger_node_2 = l[1]
        self.assertEqual(trigger_node_1.trigger_word, 'get')
        self.assertEqual(trigger_node_1.cfg_node, cfg_node)
        self.assertEqual(trigger_node_2.trigger_word, 'request')
        self.assertEqual(trigger_node_2.cfg_node, cfg_node)
        
        cfg_node = Node('request.get("stefan")', None, line_number=None, path=None)
        trigger_words = [('get', []), ('get', [])]
        l = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=2)

    def test_find_triggers(self):
        self.cfg_create_from_file('../example/vulnerable_code/XSS.py')

        cfg_list = [self.cfg]

        FlaskAdaptor(cfg_list, [], [])        

        XSS1 = cfg_list[1]
        trigger_words = [('get', [])]

        l = vulnerabilities.find_triggers(XSS1.nodes, trigger_words)
        self.assert_length(l, expected_length=1)
        

    def test_find_sanitiser_nodes(self):
        cfg_node = Node(None, None, line_number=None, path=None)
        sanitiser_tuple  = vulnerabilities.Sanitiser('escape', cfg_node)
        sanitiser = 'escape'

        result = list(vulnerabilities.find_sanitiser_nodes(sanitiser, [sanitiser_tuple]))
        self.assert_length(result, expected_length=1)
        self.assertEqual(result[0], cfg_node)
        
        
    def test_build_sanitiser_node_dict(self):
        self.cfg_create_from_file('../example/vulnerable_code/XSS_sanitised.py')
        cfg_list = [self.cfg]

        FlaskAdaptor(cfg_list, [], [])       

        cfg = cfg_list[1]
        
        cfg_node = Node(None, None,  line_number=None, path=None)
        sinks_in_file = [vulnerabilities.TriggerNode('replace', ['escape'], cfg_node)]

        sanitiser_dict = vulnerabilities.build_sanitiser_node_dict(cfg, sinks_in_file)
        self.assert_length(sanitiser_dict, expected_length=1)
        self.assertIn('escape', sanitiser_dict.keys())

        self.assertEqual(sanitiser_dict['escape'][0], cfg.nodes[2])

    def test_is_sanitized_false(self):
        cfg_node_1 = Node('Not sanitising at all', None, line_number=None, path=None)
        cfg_node_2 = Node('something.replace("this", "with this")', None, line_number=None, path=None)
        sinks_in_file = [vulnerabilities.TriggerNode('replace', ['escape'], cfg_node_2)]
        sanitiser_dict = {'escape': [cfg_node_1]}

        ReachingDefinitionsTaintAnalysis.get_lattice_elements = self.get_lattice_elements
        lattice = Lattice([cfg_node_1, cfg_node_2], analysis_type=ReachingDefinitionsTaintAnalysis)
        constraint_table[cfg_node_1] = 0
        constraint_table[cfg_node_2] = 0

        result = vulnerabilities.is_sanitized(sinks_in_file[0], sanitiser_dict, lattice)
        self.assertEqual(result, False)
        
    def test_is_sanitized_true(self):
        cfg_node_1 = Node('Awesome sanitiser', None,  line_number=None, path=None)
        cfg_node_2 = Node('something.replace("this", "with this")', None, line_number=None, path=None)
        sinks_in_file = [vulnerabilities.TriggerNode('replace', ['escape'], cfg_node_2)]
        sanitiser_dict = {'escape': [cfg_node_1]}

        ReachingDefinitionsTaintAnalysis.get_lattice_elements = self.get_lattice_elements
        lattice = Lattice([cfg_node_1, cfg_node_2], analysis_type=ReachingDefinitionsTaintAnalysis)
        constraint_table[cfg_node_2] = 0b1

        result = vulnerabilities.is_sanitized(sinks_in_file[0], sanitiser_dict, lattice)
        self.assertEqual(result, True)
        
    def test_find_vulnerabilities_no_vuln(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_no_vuln.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)

    def test_find_vulnerabilities_sanitised(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_sanitised.py')

        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_vulnerable(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_reassign(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_reassign.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_variable_assign(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_variable_assign.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def run_analysis(self, path):
        self.cfg_create_from_file(path)

        cfg_list = [self.cfg]

        FlaskAdaptor(cfg_list, [], [])

        initialize_constraint_table(cfg_list)        

        analyse(cfg_list, analysis_type=ReachingDefinitionsTaintAnalysis)

        return vulnerabilities.find_vulnerabilities(cfg_list, ReachingDefinitionsTaintAnalysis)

    def test_find_vulnerabilities_assign_other_var(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_assign_to_other_var.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_variable_multiple_assign(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_variable_multiple_assign.py')        
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_variable_assign_no_vuln(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/XSS_variable_assign_no_vuln.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=0)

    def test_find_vulnerabilities_command_injection(self):
        vulnerability_log = self.run_analysis('../example/vulnerable_code/command_injection.py')
        self.assert_length(vulnerability_log.vulnerabilities, expected_length=1)
