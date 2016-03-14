import os
import sys
import unittest
from ast import parse
from collections import namedtuple

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
from fixed_point import fixpoint_iteration, swap_constraints

class FixedPointTestCase(unittest.TestCase):
    connection = namedtuple('connection', 'constraintset element')
    def setUp(self):
        tree = generate_ast('../example/example_inputs/example.py')
        self.cfg = CFG()
        self.cfg.create(tree)

    def assertInCfg(self, connections):
        ''' Assert that all connections in the connections list exists in the cfg,
        as well as all connections not in the list do not exist

        connections is a list of tuples where the node at index 0 of the tuple has to be in the new_constraintset of the node a index 1 of the tuple'''
        for connection in connections:
            self.assertIn(self.cfg.nodes[connection[0]], self.cfg.nodes[connection[1]].new_constraint, str(connection))

        nodes = len(self.cfg.nodes)
        
        for element in range(nodes):
            for sets in range(nodes):
                if (element, sets) not in connections:
                    self.assertNotIn(self.cfg.nodes[element], self.cfg.nodes[sets].new_constraint, str(connection))
        
    def test_fixpoint_algorithm_first_iteration(self):
        fixpoint_iteration(self.cfg)


        self.assertInCfg([(1,1),(2,2),(4,4),(6,6),(7,7),(9,9),(10,10)])
        
    def test_fixpoint_algorithm_second_iteration(self):
        fixpoint_iteration(self.cfg)
        swap_constraints(self.cfg)
        fixpoint_iteration(self.cfg)


        self.assertInCfg([(1,1),
                          (2,2),
                          (2,3),(10,3),
                          (4,4),
                          (4,5),
                          (6,6),
                          (6,7),(7,7),
                          (7,8),
                          (9,9),
                          (9,10),(10,10),
                          (10,11)])
        

    def test_fixpoint_algorithm_third_iteration(self):
        fixpoint_iteration(self.cfg)
        swap_constraints(self.cfg)
        fixpoint_iteration(self.cfg)
        swap_constraints(self.cfg)
        fixpoint_iteration(self.cfg)

        
        self.assertInCfg([(1,1),
                          (2,2),
                          (2,3),(9,3),(10,3),
                          (2,4),(4,4),(10,4),
                          (4,5),
                          (4,6),(6,6),
                          (4,7),(6,7),(7,7),
                          (6,8),(7,8),
                          (7,9),(9,9),
                          (9,10),(10,10),
                          (2,11),(9,11),(10,11)])
        
