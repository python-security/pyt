import os
import sys

sys.path.insert(1, os.path.abspath('../pyt'))
from engine import Engine
from base_test_case import BaseTestCase

class EngineTest(BaseTestCase):
    def run_empty(self):
        return
    
    def test_parse(self):
        Engine.run = self.run_empty
        test_engine = Engine([], trigger_word_file=os.path.join(os.getcwd().replace('tests','pyt'), 'trigger_definitions', 'test_triggers.pyt'))
        
        
        test_engine.parse()

        self.assert_length(test_engine.sources, expected_length=1)
        self.assert_length(test_engine.sinks, expected_length=3)
        self.assert_length(test_engine.sinks[0][1], expected_length=1)
        self.assert_length(test_engine.sinks[1][1], expected_length=3)

    def test_parse_section(self):
        Engine.run = self.run_empty
        test_engine = Engine(None)

        l = list(test_engine.parse_section(iter(['get'])))
        self.assert_length(l, expected_length=1)
        self.assertEqual(l[0][0], 'get')
        self.assertEqual(l[0][1], list())

        l = list(test_engine.parse_section(iter(['get', 'get -> a, b, c d s aq     a'])))
        self.assert_length(l, expected_length=2)
        self.assertEqual(l[0][0], 'get')
        self.assertEqual(l[1][0], 'get')
        self.assertEqual(l[1][1], ['a', 'b', 'c d s aq     a'])
        self.assert_length(l[1][1], expected_length=3)

    def test_label_contains(self):
        Engine.run = self.run_empty
        test_engine = Engine(None)

        from cfg import Node
        cfg_node = Node('label', None, None, line_number=None)
        trigger_words = [('get', [])]
        l = list(test_engine.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=0)

        cfg_node = Node('request.get("stefan")', None, None, line_number=None)
        trigger_words = [('get', []), ('request', [])]
        l = list(test_engine.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=2)

        trigger_node_1 = l[0]
        trigger_node_2 = l[1]
        self.assertEqual(trigger_node_1.trigger_word_tuple.trigger_word, 'get')
        self.assertEqual(trigger_node_1.cfg_node, cfg_node)
        self.assertEqual(trigger_node_2.trigger_word_tuple.trigger_word, 'request')
        self.assertEqual(trigger_node_2.cfg_node, cfg_node)
        
        cfg_node = Node('request.get("stefan")', None, None, line_number=None)
        trigger_words = [('get', []), ('get', [])]
        l = list(test_engine.label_contains(cfg_node, trigger_words))
        self.assert_length(l, expected_length=2)

    def test_find_triggers(self):
        Engine.run = self.run_empty
        test_engine = Engine(None)

        from cfg import CFG, generate_ast
        cfg = CFG()
        tree = generate_ast('../example/vulnerable_code/XSS.py')
        cfg.create(tree)

        trigger_words = [('get', [])]

        l = test_engine.find_triggers(cfg.functions['XSS1'], trigger_words)
        self.assert_length(l, expected_length=1)
        

    def test_find_sanitiser_nodes(self):
        Engine.run = self.run_empty
        test_engine = Engine(None)

        from engine import Sanitiser, Node
        cfg_node = Node(None, None, None, line_number=None)
        sanitiser_tuple  = Sanitiser('escape', cfg_node)
        sanitiser = 'escape'

        result = list(test_engine.find_sanitiser_nodes(sanitiser, [sanitiser_tuple]))
        self.assert_length(result, expected_length=1)
        self.assertEqual(result[0], cfg_node)
        
        
