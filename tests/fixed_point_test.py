import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
from fixed_point import fixpoint_iteration

class FixedPointTestCase(unittest.TestCase):
    def test_fixpoint_algorithm(self):
        tree = generate_ast('../example/example_inputs/example.py')
        cfg = CFG()
        cfg.create(tree)
        fixpoint_iteration(cfg)


        self.assertIn(cfg.nodes[1], cfg.nodes[1].new_constraint)
        self.assertIn(cfg.nodes[2], cfg.nodes[2].new_constraint)
        self.assertIn(cfg.nodes[4], cfg.nodes[4].new_constraint)
        self.assertIn(cfg.nodes[6], cfg.nodes[6].new_constraint)
        self.assertIn(cfg.nodes[7], cfg.nodes[7].new_constraint)
        self.assertIn(cfg.nodes[9], cfg.nodes[9].new_constraint)
        self.assertIn(cfg.nodes[10], cfg.nodes[10].new_constraint)

        for empty in [3,5,8,11,12]:
            self.assertEqual(cfg.nodes[empty].new_constraint, set())
