from .analysis_base_test_case import AnalysisBaseTestCase
from pyt.constraint_table import constraint_table
from pyt.reaching_definitions import ReachingDefinitionsAnalysis


class ReachingDefinitionsTest(AnalysisBaseTestCase):
    def test_linear_program(self):
        constraint_table = {}
        lattice = self.run_analysis('examples/example_inputs/linear.py', ReachingDefinitionsAnalysis)

        EXPECTED = [
                    "Label: Entry module: ",
                    "Label: ~call_1 = ret_input():  Label: ~call_1 = ret_input()",
                    "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_input()",
                    "Label: y = x - 1:  Label: y = x - 1, Label: x = ~call_1, Label: ~call_1 = ret_input()",
                    "Label: ~call_2 = ret_print(x):  Label: ~call_2 = ret_print(x), Label: y = x - 1, Label: x = ~call_1, Label: ~call_1 = ret_input()",
                    "Label: Exit module:  Label: ~call_2 = ret_print(x), Label: y = x - 1, Label: x = ~call_1, Label: ~call_1 = ret_input()",
                   ]
        i = 0
        for k, v in constraint_table.items():
          row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
          self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
          i = i + 1

    def test_example(self):
        constraint_table = {}
        lattice = self.run_analysis('examples/example_inputs/example.py', ReachingDefinitionsAnalysis)

        EXPECTED = [
                    "Label: Entry module: ",
                    "Label: ~call_1 = ret_input():  Label: ~call_1 = ret_input()",
                    "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_input()",
                    "Label: ~call_2 = ret_int(x):  Label: ~call_2 = ret_int(x), Label: x = ~call_1, Label: ~call_1 = ret_input()",
                    "Label: x = ~call_2:  Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: while x > 1::  Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: y = x / 2:  Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: if y > 3::  Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: x = x - y:  Label: z = z - 1, Label: x = x - y, Label: y = x / 2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: z = x - 4:  Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: if z > 0::  Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: x = x / 2:  Label: x = x / 2, Label: z = x - 4, Label: y = x / 2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: z = z - 1:  Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: ~call_3 = ret_print(x):  Label: ~call_3 = ret_print(x), Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                    "Label: Exit module:  Label: ~call_3 = ret_print(x), Label: z = z - 1, Label: x = x / 2, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
                   ]
        i = 0
        for k, v in constraint_table.items():
          row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
          self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
          i = i + 1
