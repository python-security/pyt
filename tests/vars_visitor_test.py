import ast
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('../pyt'))
from vars_visitor import VarsVisitor


class VarsVisitorTestCase(unittest.TestCase):
    '''Baseclass for VarsVisitor tests'''

    def perform_vars_on_expression(self, expr):
        obj = ast.parse(expr)
        vars = VarsVisitor()
        vars.visit(obj)

        return vars


class VarsVisitorTest(VarsVisitorTestCase):
    def test_assign_var_and_num(self):
        vars = self.perform_vars_on_expression('a = 1')
        self.assertEqual(vars.result, ['a'])

    def test_assign_var_and_var(self):
        vars = self.perform_vars_on_expression('a = x')
        self.assertEqual(vars.result, ['a', 'x'])

    def test_call1(self):
        vars = self.perform_vars_on_expression('print(x)')
        self.assertEqual(vars.result, ['x'])

    def test_call2(self):
        vars = self.perform_vars_on_expression('s.print(x)')
        self.assertEqual(vars.result, ['s', 'x'])

    def test_call3(self):
        vars = self.perform_vars_on_expression('obj.print.attr(y).s(x)')
        self.assertEqual(vars.result, ['obj', 'y', 'x'])

    def test_call4(self):
        vars = self.perform_vars_on_expression('obj.print.attr(y.f).s(x)')
        self.assertEqual(vars.result, ['obj', 'y', 'x'])

    def test_call5(self):
        vars = self.perform_vars_on_expression("resp = make_response(html.replace('{{ param }}', param))")
        self.assertEqual(vars.result, ['resp', 'html', 'param'])

    def test_keyword_vararg(self):
        vars = self.perform_vars_on_expression('print(arg = x)')
        self.assertEqual(vars.result, ['x'])

    def test_keyword_numarg(self):
        vars = self.perform_vars_on_expression('print(arg = 1)')
        self.assertEqual(vars.result, [])

    def test_subscript(self):
        vars = self.perform_vars_on_expression('l[a] = x + y')
        self.assertEqual(vars.result, ['l', 'a', 'x', 'y'])
