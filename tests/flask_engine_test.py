import os
import sys

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
from flask_engine import FlaskEngine
from base_test_case import BaseTestCase

class FlaskEngineTest(BaseTestCase):
    def test_find_flask_functions(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/flask_function_and_normal_function.py')
        self.cfg.create(tree)
        cfg_list = [self.cfg]

        flask = FlaskEngine(cfg_list)
        
        #self.assertEqual(len(flask_functions), 1)

        #self.assertEqual(flask_functions[0], 'flask_function')
