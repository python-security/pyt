import ast
import unittest

from pyt.helper_visitors import VarsVisitor


class VarsVisitorTestCase(unittest.TestCase):
    """Baseclass for VarsVisitor tests"""

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
        self.assertEqual(vars.result, ['resp', 'ret_replace'])

    def test_call6(self):
        vars = self.perform_vars_on_expression("resp = f(kw=g(a, b))")
        self.assertEqual(vars.result, ['resp', 'ret_g'])

    def test_call7(self):
        vars = self.perform_vars_on_expression("resp = make_response(html.replace.bar('{{ param }}', param))")
        self.assertEqual(vars.result, ['resp', 'ret_bar'])

    def test_curried_function(self):
        # Curried functions aren't supported really, but we now at least have a defined behaviour.
        vars = self.perform_vars_on_expression('f(g.h(a)(b))')
        self.assertCountEqual(vars.result, ['ret_h', 'b'])
        vars = self.perform_vars_on_expression('f(g(a)(b)(c)(d, e=f))')
        self.assertCountEqual(vars.result, ['ret_g', 'b', 'c', 'd', 'f'])

    def test_keyword_vararg(self):
        vars = self.perform_vars_on_expression('print(arg = x)')
        self.assertEqual(vars.result, ['x'])

    def test_keyword_numarg(self):
        vars = self.perform_vars_on_expression('print(arg = 1)')
        self.assertEqual(vars.result, [])

    def test_subscript(self):
        vars = self.perform_vars_on_expression('l[a] = x + y')
        self.assertEqual(vars.result, ['l', 'a', 'x', 'y'])

    def test_visit_boolop(self):
        # AND operator
        var1 = self.perform_vars_on_expression('b = x and y')
        self.assertEqual(var1.result, ['b', 'x', 'y'])

        # OR operator
        var2 = self.perform_vars_on_expression('b = x or y')
        self.assertEqual(var2.result, ['b', 'x', 'y'])

    def test_visit_unaryop(self):
        vars = self.perform_vars_on_expression('a = not b')
        self.assertEqual(vars.result, ['a', 'b'])

    def test_visit_lambda(self):
        vars = self.perform_vars_on_expression('f = lambda x: x + 2')
        self.assertEqual(vars.result, ['f', 'x'])

    def test_visit_set(self):
        vars = self.perform_vars_on_expression('{a, b, c}')
        self.assertEqual(vars.result, ['a', 'b', 'c'])

    def test_visit_tuple(self):
        vars = self.perform_vars_on_expression('(a, b, c)')
        self.assertEqual(vars.result, ['a', 'b', 'c'])

    def test_visit_list(self):
        vars = self.perform_vars_on_expression('[a, b, c]')
        self.assertEqual(vars.result, ['a', 'b', 'c'])

    def test_visit_yield(self):
        var1 = self.perform_vars_on_expression('yield exp')
        self.assertEqual(var1.result, ['exp'])

        var2 = self.perform_vars_on_expression('yield from exp')
        self.assertEqual(var2.result, ['exp'])

    def test_visit_listcomp(self):
        vars = self.perform_vars_on_expression(
            '[item for item in coll if cond]')
        self.assertEqual(vars.result, ['item', 'item', 'coll', 'cond'])

    def test_visit_setcomp(self):
        vars = self.perform_vars_on_expression('{a for b in d}')
        self.assertEqual(vars.result, ['a', 'b', 'd'])

    def test_visit_dictcomp(self):
        vars = self.perform_vars_on_expression('{k1: v1 for (k2, v2) in d}')
        self.assertEqual(vars.result, ['k1', 'v1', 'k2', 'v2', 'd'])

    def test_visit_compare(self):
        vars = self.perform_vars_on_expression('a == b')
        self.assertEqual(vars.result, ['a', 'b'])

    def test_visit_starred(self):
        vars = self.perform_vars_on_expression('*m = t')
        self.assertEqual(vars.result, ['m', 't'])

    def test_visit_ifexp(self):
        vars = self.perform_vars_on_expression('res if test else orelse')
        self.assertEqual(vars.result, ['test', 'res', 'orelse'])

    def test_visit_subscript(self):
        # simple slice
        vars = self.perform_vars_on_expression('foo.bar[lower:upper:step]')
        self.assertEqual(vars.result, ['foo', 'foo', 'lower', 'upper', 'step'])

        # extended slice
        vars = self.perform_vars_on_expression('foo[item1:item2, item3]')
        self.assertEqual(vars.result, ['foo', 'item1', 'item2', 'item3'])

    def test_visit_await(self):
        vars = self.perform_vars_on_expression("""
            async def bar():
                await foo()
        """.lstrip())
        self.assertEqual(vars.result, [])

    def test_visit_dict(self):
        vars = self.perform_vars_on_expression('a = {k1: v1, k2: v2, **d1, **d2}')
        self.assertEqual(vars.result, ['a', 'k1', 'k2', 'v1', 'v2', 'd1', 'd2'])
