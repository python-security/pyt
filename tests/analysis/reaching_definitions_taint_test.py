from .analysis_base_test_case import AnalysisBaseTestCase

from pyt.analysis.constraint_table import constraint_table


class ReachingDefinitionsTaintTest(AnalysisBaseTestCase):
    # Note: the numbers in the test represent the line numbers of the assignments in the program.
    def test_linear_program(self):
        lattice = self.run_analysis('examples/example_inputs/linear.py')

        EXPECTED = [
            "Label: Entry module:",
            "Label: ~call_1 = ret_input():  Label: ~call_1 = ret_input()",
            "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_input()",
            "Label: y = x - 1:  Label: y = x - 1, Label: x = ~call_1, Label: ~call_1 = ret_input()",
            """Label: ~call_2 = ret_print(x):  Label: ~call_2 = ret_print(x), Label: y = x - 1,
               Label: x = ~call_1, Label: ~call_1 = ret_input()""",
            """Label: Exit module:  Label: ~call_2 = ret_print(x), Label: y = x - 1, Label: x = ~call_1,
               Label: ~call_1 = ret_input()"""
        ]
        i = 0
        for k, v in constraint_table.items():
            row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
            self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
            i = i + 1

    def test_if_program(self):
        lattice = self.run_analysis('examples/example_inputs/if_program.py')

        EXPECTED = [
            "Label: Entry module:",
            "Label: ~call_1 = ret_input():  Label: ~call_1 = ret_input()",
            "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_input()",
            "Label: if x > 0::  Label: x = ~call_1, Label: ~call_1 = ret_input()",
            "Label: y = x + 1:  Label: y = x + 1, Label: x = ~call_1, Label: ~call_1 = ret_input()",
            """Label: ~call_2 = ret_print(x):  Label: ~call_2 = ret_print(x), Label: y = x + 1,
               Label: x = ~call_1, Label: ~call_1 = ret_input()""",
            """Label: Exit module:  Label: ~call_2 = ret_print(x), Label: y = x + 1, Label: x = ~call_1,
               Label: ~call_1 = ret_input()"""
        ]
        i = 0
        for k, v in constraint_table.items():
            row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
            self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
            i = i + 1

    def test_example(self):
        lattice = self.run_analysis('examples/example_inputs/example.py')

        EXPECTED = [
            "Label: Entry module:",
            "Label: ~call_1 = ret_input():  Label: ~call_1 = ret_input()",
            "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_input()",
            "Label: ~call_2 = ret_int(x):  Label: ~call_2 = ret_int(x), Label: x = ~call_1, Label: ~call_1 = ret_input()",
            "Label: x = ~call_2:  Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()",
            """Label: while x > 1::  Label: z = z - 1, Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2,
               Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: y = x / 2:  Label: z = z - 1, Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2,
               Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: if y > 3::  Label: z = z - 1, Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2,
               Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: x = x - y:  Label: z = z - 1, Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2,
               Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: z = x - 4:  Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2,
               Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: if z > 0::  Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2,
               Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: x = x / 2:  Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2, Label: x = ~call_2,
               Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: z = z - 1:  Label: z = z - 1, Label: x = x / 2, Label: z = x - 4, Label: x = x - y, Label: y = x / 2,
               Label: x = ~call_2, Label: ~call_2 = ret_int(x), Label: ~call_1 = ret_input()""",
            """Label: ~call_3 = ret_print(x):  Label: ~call_3 = ret_print(x), Label: z = z - 1, Label: x = x / 2, Label: z = x - 4,
               Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x),
               Label: ~call_1 = ret_input()""",
            """Label: Exit module:  Label: ~call_3 = ret_print(x), Label: z = z - 1, Label: x = x / 2, Label: z = x - 4,
               Label: x = x - y, Label: y = x / 2, Label: x = ~call_2, Label: ~call_2 = ret_int(x),
               Label: ~call_1 = ret_input()"""
        ]
        i = 0
        for k, v in constraint_table.items():
            row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
            self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
            i = i + 1

    def test_func_with_params(self):
        lattice = self.run_analysis('examples/example_inputs/function_with_params.py')

        self.assertInCfg([(1, 1),
                          (1, 2), (2, 2),
                          (1, 3), (2, 3), (3, 3),
                          (1, 4), (2, 4), (3, 4), (4, 4),
                          (1, 5), (2, 5), (3, 5), (4, 5),
                          *self.constraints([1, 2, 3, 4, 6], 6),
                          *self.constraints([1, 2, 3, 4, 6, 7], 7),
                          *self.constraints([1, 2, 3, 4, 6, 7], 8),
                          *self.constraints([2, 3, 4, 6, 7, 9], 9),
                          *self.constraints([2, 3, 4, 6, 7, 9], 10)], lattice)

    def test_while(self):
        lattice = self.run_analysis('examples/example_inputs/while.py')

        EXPECTED = [
            "Label: Entry module: ",
            "Label: ~call_2 = ret_input():  Label: ~call_2 = ret_input()",
            "Label: ~call_1 = ret_int(~call_2):  Label: ~call_1 = ret_int(~call_2), Label: ~call_2 = ret_input()",
            "Label: x = ~call_1:  Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2), Label: ~call_2 = ret_input()",
            """Label: while x < 10::  Label: x = x + 1, Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2),
               Label: ~call_2 = ret_input(""",
            """Label: x = x + 1:  Label: x = x + 1, Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2),
               Label: ~call_2 = ret_input()""",
            """Label: if x == 5::  Label: x = x + 1, Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2),
               Label: ~call_2 = ret_input()""",
            """Label: BreakNode:  Label: x = x + 1, Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2),
               Label: ~call_2 = ret_input()""",
            "Label: x = 6:  Label: x = 6, Label: ~call_1 = ret_int(~call_2), Label: ~call_2 = ret_input()",
            """Label: ~call_3 = ret_print(x):  Label: ~call_3 = ret_print(x), Label: x = 6, Label: x = x + 1,
               Label: x = ~call_1, Label: ~call_1 = ret_int(~call_2), Label: ~call_2 = ret_input()""",
            """Label: Exit module:  Label: ~call_3 = ret_print(x), Label: x = 6, Label: x = x + 1, Label: x = ~call_1,
               Label: ~call_1 = ret_int(~call_2), Label: ~call_2 = ret_input()"""
        ]
        i = 0
        for k, v in constraint_table.items():
            row = str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)])
            self.assertTrue(self.string_compare_alnum(row, EXPECTED[i]))
            i = i + 1
