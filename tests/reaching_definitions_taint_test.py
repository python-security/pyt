import sys
import os
from collections import namedtuple

from base_test_case import BaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from fixed_point import FixedPointAnalysis

class ReachingDefinitionsTaintTest(BaseTestCase):
    connection = namedtuple('connection', 'constraintset element')
    def setUp(self):
        self.cfg = None

    def assertInCfg(self, connections):
        ''' Assert that all connections in the connections list exists in the cfg,
        as well as all connections not in the list do not exist

        connections is a list of tuples where the node at index 0 of the tuple has to be in the new_constraintset of the node a index 1 of the tuple'''
        for connection in connections:
            self.assertIn(self.cfg.nodes[connection[0]], self.cfg.nodes[connection[1]].new_constraint, str(connection) + " expected to be connected")

        nodes = len(self.cfg.nodes)
        
        for element in range(nodes):
            for sets in range(nodes):
                if (element, sets) not in connections:
                    self.assertNotIn(self.cfg.nodes[element], self.cfg.nodes[sets].new_constraint, "(%s,%s)" % (element, sets)  +  " expected to be disconnected")

    def test_linear_program(self):
        self.cfg_create_from_file('../example/example_inputs/linear.py')
        self.analysis = FixedPointAnalysis(self.cfg, ReachingDefinitionsTaintAnalysis)
        self.analysis.fixpoint_runner()

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          (1,3), (2,3),
                          (1,4), (2,4)])

    def test_if_program(self):
        self.cfg_create_from_file('../example/example_inputs/if_program.py')
        self.analysis = FixedPointAnalysis(self.cfg, ReachingDefinitionsTaintAnalysis)
        self.analysis.fixpoint_runner()

        self.assertInCfg([(1,1),
                          (1,2),
                          (1,3), (3,3),
                          (1,4), (3,4),
                          (1,5), (3,5)])

    def constraints(self, list_of_constraints, node_number):
        for c in list_of_constraints:
            yield (c,node_number)

    def test_example(self):
        self.cfg_create_from_file('../example/example_inputs/example.py')
        self.analysis = FixedPointAnalysis(self.cfg, ReachingDefinitionsTaintAnalysis)
        self.analysis.fixpoint_runner()

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          *self.constraints([1,2,4,6,7,9,10], 3),
                          *self.constraints([1,2,4,6,7,9,10], 4),
                          *self.constraints([1,2,4,6,7,9,10], 5),
                          *self.constraints([1,2,4,6,7,9,10], 6),
                          *self.constraints([1,2,4,6,7,9], 7),
                          *self.constraints([1,2,4,6,7,9], 8),
                          *self.constraints([1,2,4,6,7,9], 9),
                          *self.constraints([1,2,4,6,7,9,10], 10),
                          *self.constraints([1,2,4,6,7,9,10], 11),
                          *self.constraints([1,2,4,6,7,9,10], 12)])

    def test_func_with_params(self):
        self.cfg_create_from_file('../example/example_inputs/function_with_params.py')
        self.analysis = FixedPointAnalysis(self.cfg, ReachingDefinitionsTaintAnalysis)
        self.analysis.fixpoint_runner()

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          (1,3), (2,3), (3,3),
                          (1,4), (2,4), (3,4), (4,4),
                          (1,5), (2,5), (3,5), (4,5),
                          *self.constraints([1,2,3,4,6], 6),
                          *self.constraints([1,2,3,4,6], 7),
                          *self.constraints([1,2,3,4,6], 8),
                          *self.constraints([2,3,4,6,9], 9),
                          *self.constraints([2,3,4,6,9], 10)])
