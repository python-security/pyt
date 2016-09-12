import sys
import os

from analysis_base_test_case import AnalysisBaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from liveness import LivenessAnalysis
from constraint_table import constraint_table

class LivenessTest(AnalysisBaseTestCase):
    def test_example(self):
        lattice = self.run_analysis('../example/example_inputs/example.py', LivenessAnalysis)

        x = 0b1
        y = 0b10
        z = 0b100

        lattice.el2bv['x'] = x
        lattice.el2bv['y'] = y
        lattice.el2bv['z'] = z

        self.assertEqual(constraint_table[self.cfg.nodes[0]], 0)
        self.assertEqual(constraint_table[self.cfg.nodes[1]], 0)
        self.assertEqual(constraint_table[self.cfg.nodes[2]], x)
        self.assertEqual(constraint_table[self.cfg.nodes[3]], x)
        self.assertEqual(constraint_table[self.cfg.nodes[4]], x)
        self.assertEqual(constraint_table[self.cfg.nodes[5]], x | y)
        self.assertEqual(constraint_table[self.cfg.nodes[6]], x | y)
        self.assertEqual(constraint_table[self.cfg.nodes[7]], x)
        self.assertEqual(constraint_table[self.cfg.nodes[8]], x | z)
        self.assertEqual(constraint_table[self.cfg.nodes[9]], x | z)
        self.assertEqual(constraint_table[self.cfg.nodes[10]], x | z)
        self.assertEqual(constraint_table[self.cfg.nodes[11]], x)
        self.assertEqual(constraint_table[self.cfg.nodes[12]], 0)

        self.assertEqual(len(lattice.el2bv), 3)
