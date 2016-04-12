import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
import flask_engine

class FlaskEngineTest(unittest.TestCase):
    def test_find_flask_functions(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/flask_function_and_normal_function.py')
        self.cfg.create(tree)

        flask_functions = list(flask_engine.find_flask_route_functions(self.cfg.functions))
        
        #self.assertEqual(len(flask_functions), 1)

        #self.assertEqual(flask_functions[0], 'flask_function')
                


        
