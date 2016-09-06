import sys
import os

from analysis_base_test_case import AnalysisBaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from reaching_definitions import ReachingDefinitionsAnalysis


class ReachingDefinitionsTest(AnalysisBaseTestCase):
    def test_linear_program(self):
        lattice = self.run_analysis('../example/example_inputs/linear.py', ReachingDefinitionsAnalysis)

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          (1,3), (2,3),
                          (1,4), (2,4)], lattice)

    def test_example(self):
        lattice = self.run_analysis('../example/example_inputs/example.py', ReachingDefinitionsAnalysis)

        self.assertInCfg([(1,1),
                          (2,2),
                          *self.constraints([2,4,6,9,10], 3),
                          *self.constraints([2,4,6,9,10], 4),
                          *self.constraints([2,4,6,9,10], 5),
                          *self.constraints([4,6,10], 6),
                          *self.constraints([2,4,6,7,9], 7),
                          *self.constraints([2,4,6,7,9], 8),
                          *self.constraints([4,7,9], 9),
                          *self.constraints([2,4,6,9,10], 10),
                          *self.constraints([2,4,6,9,10], 11),
                          *self.constraints([2,4,6,9,10], 12)], lattice)

                    
