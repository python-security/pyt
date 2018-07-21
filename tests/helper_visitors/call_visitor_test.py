import ast
import unittest

from pyt.helper_visitors import CallVisitor


class CallVisitorTest(unittest.TestCase):
    def get_results(self, call_name, expr):
        tree = ast.parse(expr)
        return CallVisitor.get_call_visit_results(trigger_str=call_name, node=tree)

    def test_basic(self):
        call_args = self.get_results('func', 'func(a, b, x=c)')
        self.assertEqual(call_args.args, [{'a'}, {'b'}])
        self.assertEqual(call_args.kwargs, {'x': {'c'}})
        self.assertEqual(call_args.unknown_args, set())
        self.assertEqual(call_args.unknown_kwargs, set())

    def test_visits_each_argument_recursively(self):
        call_args = self.get_results('func', 'func(a + b, f(123), g(h(c=d)), e=i(123))')
        self.assertEqual(call_args.args, [{'a', 'b'}, set(), {'d'}])
        self.assertEqual(call_args.kwargs, {'e': set()})
        self.assertEqual(call_args.unknown_args, set())
        self.assertEqual(call_args.unknown_kwargs, set())

    def test_merge_when_function_called_inside_own_arguments(self):
        call_args = self.get_results('func', 'func(a + func(b, c, x=d), e)')
        self.assertEqual(call_args.args, [{'a', 'b', 'c', 'd'}, {'c', 'e'}])
        self.assertEqual(call_args.kwargs, {'x': {'d'}})
        self.assertEqual(call_args.unknown_args, set())
        self.assertEqual(call_args.unknown_kwargs, set())

    def test_star_args_kwargs(self):
        call_args = self.get_results('func', 'func(a, b, *c, *d, x=e, **f, **g)')
        self.assertEqual(call_args.args, [{'a'}, {'b'}])
        self.assertEqual(call_args.kwargs, {'x': {'e'}})
        self.assertEqual(call_args.unknown_args, {'c', 'd'})
        self.assertEqual(call_args.unknown_kwargs, {'f', 'g'})

    def test_call_inside_comprehension(self):
        call_args = self.get_results('func', '[row for row in db.func(a, b)]')
        self.assertEqual(call_args.args, [{'a'}, {'b'}])
        self.assertEqual(call_args.kwargs, {})
        self.assertEqual(call_args.unknown_args, set())
        self.assertEqual(call_args.unknown_kwargs, set())

    def test_call_inside_comprehension_2(self):
        call_args = self.get_results('func', '[func(a, b) for b in c]')
        self.assertEqual(call_args.args, [{'a'}, {'b'}])
        self.assertEqual(call_args.kwargs, {})
        self.assertEqual(call_args.unknown_args, set())
        self.assertEqual(call_args.unknown_kwargs, set())
