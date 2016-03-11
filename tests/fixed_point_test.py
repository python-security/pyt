import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
from fixed_point import fixpoint_iteration

class FixedPointTestCase(unittest.TestCase):
    def setUp(self):
        tree = generate_ast('../example/example_inputs/example.py')
        self.cfg = CFG()
        self.cfg.create(tree)
        
    def test_fixpoint_algorithm_first_iteration(self):

        fixpoint_iteration(self.cfg)


        self.assertIn(self.cfg.nodes[1], self.cfg.nodes[1].new_constraint)
        self.assertIn(self.cfg.nodes[2], self.cfg.nodes[2].new_constraint)
        self.assertIn(self.cfg.nodes[4], self.cfg.nodes[4].new_constraint)
        self.assertIn(self.cfg.nodes[6], self.cfg.nodes[6].new_constraint)
        self.assertIn(self.cfg.nodes[7], self.cfg.nodes[7].new_constraint)
        self.assertIn(self.cfg.nodes[9], self.cfg.nodes[9].new_constraint)
        self.assertIn(self.cfg.nodes[10], self.cfg.nodes[10].new_constraint)

        for empty in [3,5,8,11,12]:
            self.assertEqual(self.cfg.nodes[empty].new_constraint, set())

        for empty in [3,5,8,11,12]:
            self.assertEqual(cfg.nodes[empty].new_constraint, set())
