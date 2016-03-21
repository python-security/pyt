import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from left_hand_side_vars_visitor import LHSVarsVisitor


class VarsVisitorTestCase(unittest.TestCase):
    '''Baseclass for VarsVisitor tests'''

    def perform_vars_on_expression(self, expr):
        obj = parse(expr)
        vars = LHSVarsVisitor()
        vars.visit(obj)

        return vars

class LHSVarsVisitorTest(VarsVisitorTestCase):
    def test_assign_var_and_num(self):
        vars = self.perform_vars_on_expression('a = 1')
        self.assertEqual(vars.result, 'a')

    def test_assign_var_and_var(self):
        vars = self.perform_vars_on_expression('a = x')
        self.assertEqual(vars.result, 'a')

    def test_aug_assign(self):
        vars = self.perform_vars_on_expression('a += x')
        self.assertEqual(vars.result, 'a')

    def test_call(self):
        vars = self.perform_vars_on_expression('print(x)')
        self.assertEqual(vars.result, None)

    def test_keyword_vararg(self):
        vars = self.perform_vars_on_expression('print("test")')
        self.assertEqual(vars.result, None)

    def test_keyword_numarg(self):
        vars = self.perform_vars_on_expression('print("test2")')
        self.assertEqual(vars.result, None)

    def test_starred(self):
        vars = self.perform_vars_on_expression('x, *y = 1, 2, 3')
        self.assertEqual(vars.result, {'x','y'})
        
    def test_subscript(self):
        vars = self.perform_vars_on_expression('x[1] = 4')
        self.assertEqual(vars.result, 'x')
