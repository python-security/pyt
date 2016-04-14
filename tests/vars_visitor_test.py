import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from vars_visitor import VarsVisitor


class VarsVisitorTestCase(unittest.TestCase):
    '''Baseclass for VarsVisitor tests'''

    def perform_vars_on_expression(self, expr):
        obj = parse(expr)
        vars = VarsVisitor()
        vars.visit(obj)

        return vars

class VarsVisitorTest(VarsVisitorTestCase):
    def test_assign_var_and_num(self):
        vars = self.perform_vars_on_expression('a = 1')
        self.assertEqual(vars.result,[])

    def test_assign_var_and_var(self):
        vars = self.perform_vars_on_expression('a = x')
        self.assertEqual(vars.result,['x'])

    def test_call(self):
        vars = self.perform_vars_on_expression('print(x)')
        self.assertEqual(vars.result,['x'])

    def test_keyword_vararg(self):
        vars = self.perform_vars_on_expression('print(arg = x)')
        self.assertEqual(vars.result,['x'])

    def test_keyword_numarg(self):
        vars = self.perform_vars_on_expression('print(arg = 1)')
        self.assertEqual(vars.result,[])
