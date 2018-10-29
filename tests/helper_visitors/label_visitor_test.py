import ast
import unittest

from pyt.helper_visitors import LabelVisitor


class LabelVisitorTestCase(unittest.TestCase):
    """Baseclass for LabelVisitor tests"""

    def perform_labeling_on_expression(self, expr):
        obj = ast.parse(expr)
        label = LabelVisitor()
        label.visit(obj)

        return label


class LabelVisitorTest(LabelVisitorTestCase):
    def test_assign(self):
        label = self.perform_labeling_on_expression('a = 1')
        self.assertEqual(label.result, 'a = 1')

    def test_augassign(self):
        label = self.perform_labeling_on_expression('a +=2')
        self.assertEqual(label.result, 'a += 2')

    def test_compare_simple(self):
        label = self.perform_labeling_on_expression('a > b')
        self.assertEqual(label.result, 'a > b')

    def test_compare_multi(self):
        label = self.perform_labeling_on_expression('a > b > c')
        self.assertEqual(label.result, 'a > b > c')

    def test_binop(self):
        label = self.perform_labeling_on_expression('a / b')
        self.assertEqual(label.result, 'a / b')

    def test_call_no_arg(self):
        label = self.perform_labeling_on_expression('range()')
        self.assertEqual(label.result, 'range()')

    def test_call_single_arg(self):
        label = self.perform_labeling_on_expression('range(5)')
        self.assertEqual(label.result, 'range(5)')

    def test_call_multi_arg(self):
        label = self.perform_labeling_on_expression('range(1, 5)')
        self.assertEqual(label.result, 'range(1, 5)')

    def test_tuple_one_element(self):
        label = self.perform_labeling_on_expression('(1)')
        self.assertEqual(label.result, '1')

    def test_tuple_two_elements(self):
        label = self.perform_labeling_on_expression('(1, 2)')
        self.assertEqual(label.result, '(1, 2)')

    def test_empty_tuple(self):
        label = self.perform_labeling_on_expression('()')
        self.assertEqual(label.result, '()')

    def test_empty_list(self):
        label = self.perform_labeling_on_expression('[]')
        self.assertEqual(label.result, '[]')

    def test_list_one_element(self):
        label = self.perform_labeling_on_expression('[1]')
        self.assertEqual(label.result, '[1]')

    def test_list_two_elements(self):
        label = self.perform_labeling_on_expression('[1, 2]')
        self.assertEqual(label.result, '[1, 2]')

    def test_joined_str(self):
        label = self.perform_labeling_on_expression('f"a{f(b)}{c}d"')
        self.assertEqual(label.result, 'f\'a{f(b)}{c}d\'')

    def test_joined_str_with_format_spec(self):
        label = self.perform_labeling_on_expression('f"a{b!s:.{length}}"')
        self.assertEqual(label.result, 'f\'a{b!s:.{length}}\'')

    def test_starred(self):
        label = self.perform_labeling_on_expression('[a, *b] = *c, d')
        self.assertEqual(label.result, '[a, *b] = (*c, d)')

    def test_if_exp(self):
        label = self.perform_labeling_on_expression('a = b if c else d')
        self.assertEqual(label.result, 'a = (c) ? (b) : (d)')
