import os
import sys

sys.path.insert(1, os.path.abspath('../pyt'))
from engine import Engine
from base_test_case import BaseTestCase

class EngineTest(BaseTestCase):
    def run_empty(self):
        return
    
    def test_parser(self):
        Engine.run = self.run_empty
        test_engine = Engine([], trigger_word_file=os.path.join(os.getcwd().replace('tests','pyt'), 'trigger_definitions', 'test_triggers.pyt'))
        
        
        test_engine.parse_sources_and_sinks()

        self.assert_length(test_engine.sources, expected_length=1)
        self.assert_length(test_engine.sinks, expected_length=3)
        self.assert_length(test_engine.sinks[0][1], expected_length=1)
        self.assert_length(test_engine.sinks[1][1], expected_length=3)


