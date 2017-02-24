import os
import sys
import unittest
from collections import namedtuple

from base_test_case import BaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from constraint_table import initialize_constraint_table
from fixed_point import FixedPointAnalysis
from lattice import Lattice


class AnalysisBaseTestCase(BaseTestCase):
    connection = namedtuple('connection', 'constraintset element')
    def setUp(self):
        self.cfg = None

    def assertInCfg(self, connections, lattice):
        ''' Assert that all connections in the connections list exists in the cfg,
        as well as all connections not in the list do not exist

        connections is a list of tuples where the node at index 0 of the tuple has to be in the new_constraintset of the node a index 1 of the tuple'''
        for connection in connections:
            self.assertEqual(lattice.in_constraint(self.cfg.nodes[connection[0]], self.cfg.nodes[connection[1]]), True, str(connection) + " expected to be connected")
        nodes = len(self.cfg.nodes)

        for element in range(nodes):
            for sets in range(nodes):
                if (element, sets) not in connections:
                    self.assertEqual(lattice.in_constraint(self.cfg.nodes[element], self.cfg.nodes[sets]), False,  "(%s,%s)" % (self.cfg.nodes[element], self.cfg.nodes[sets])  +  " expected to be disconnected")

    def constraints(self, list_of_constraints, node_number):
        for c in list_of_constraints:
            yield (c,node_number)

    def run_analysis(self, path, analysis_type):
        self.cfg_create_from_file(path)
        initialize_constraint_table([self.cfg])
        self.analysis = FixedPointAnalysis(self.cfg, analysis_type)
        self.analysis.fixpoint_runner()
        return Lattice(self.cfg.nodes, analysis_type)
