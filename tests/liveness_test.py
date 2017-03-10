from .analysis_base_test_case import AnalysisBaseTestCase
from pyt.constraint_table import constraint_table
from pyt.liveness import LivenessAnalysis


class LivenessTest(AnalysisBaseTestCase):
    def test_example(self):
        lattice = self.run_analysis('example/example_inputs/example.py', LivenessAnalysis)

        x = 0b1   # 1
        y = 0b10  # 2
        z = 0b100 # 4

        lattice.el2bv['x'] = x
        lattice.el2bv['y'] = y
        lattice.el2bv['z'] = z

        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[0]]), [])
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[1]]), [])
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[2]]), ['x'])
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[3]]), ['x'])
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[4]]), ['x'])
        self.assertEqual(set(lattice.get_elements(constraint_table[self.cfg.nodes[5]])), set(['x','y']))
        self.assertEqual(set(lattice.get_elements(constraint_table[self.cfg.nodes[6]])), set(['x','y']))
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[7]]), ['x'])
        self.assertEqual(set(lattice.get_elements(constraint_table[self.cfg.nodes[8]])), set(['x','z']))
        self.assertEqual(set(lattice.get_elements(constraint_table[self.cfg.nodes[9]])), set(['x','z']))
        self.assertEqual(set(lattice.get_elements(constraint_table[self.cfg.nodes[10]])), set(['x','z']))
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[11]]), ['x'])
        self.assertEqual(lattice.get_elements(constraint_table[self.cfg.nodes[12]]), [])
        self.assertEqual(len(lattice.el2bv), 3)
