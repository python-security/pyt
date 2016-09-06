import sys
import os
from collections import namedtuple, OrderedDict

from analysis_base_test_case import AnalysisBaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis


class ReachingDefinitionsTaintTest(AnalysisBaseTestCase):
    def test_linear_program(self):
        lattice = self.run_analysis('../example/example_inputs/linear.py', ReachingDefinitionsTaintAnalysis)

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          (1,3), (2,3),
                          (1,4), (2,4)], lattice)


    def test_if_program(self):
        lattice = self.run_analysis('../example/example_inputs/if_program.py', ReachingDefinitionsTaintAnalysis)

        self.assertInCfg([(1,1),
                          (1,2),
                          (1,3), (3,3),
                          (1,4), (3,4),
                          (1,5), (3,5)], lattice)

    def test_example(self):
        lattice = self.run_analysis('../example/example_inputs/example.py', ReachingDefinitionsTaintAnalysis)

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
                          *self.constraints([1,2,4,6,7,9,10], 12)], lattice)

    def test_func_with_params(self):
        lattice = self.run_analysis('../example/example_inputs/function_with_params.py', ReachingDefinitionsTaintAnalysis)

        self.assertInCfg([(1,1),
                          (1,2), (2,2),
                          (1,3), (2,3), (3,3),
                          (1,4), (2,4), (3,4), (4,4),
                          (1,5), (2,5), (3,5), (4,5),
                          *self.constraints([1,2,3,4,6], 6),
                          *self.constraints([1,2,3,4,6], 7),
                          *self.constraints([1,2,3,4,6], 8),
                          *self.constraints([2,3,4,6,9], 9),
                          *self.constraints([2,3,4,6,9], 10)], lattice)

    def test_while(self):
        lattice = self.run_analysis('../example/example_inputs/while.py', ReachingDefinitionsTaintAnalysis)

        self.assertInCfg([(1,1),
                          (1,2), (3,2),
                          (1,3), (3,3),
                          (1,4), (3,4),
                          (1,5), (3,5),
                          (6,6),
                          (1,7), (3,7), (6,7),
                          (1,8), (3,8), (6,8)], lattice)

    def test_join(self):
        pass
