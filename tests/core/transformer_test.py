import ast
import unittest

from pyt.core.transformer import PytTransformer


class TransformerTest(unittest.TestCase):
    """Tests for the AsyncTransformer."""

    def test_async_removed_by_transformer(self):
        self.maxDiff = 99999
        async_tree = ast.parse("\n".join([
            "async def a():",
            "   async for b in c():",
            "       await b()",
            "   async with d() as e:",
            "       pass",
            "   return await y()"
        ]))
        self.assertIsInstance(async_tree.body[0], ast.AsyncFunctionDef)
        self.assertIsInstance(async_tree.body[0].body[-1], ast.Return)
        self.assertIsInstance(async_tree.body[0].body[-1].value, ast.Await)

        sync_tree = ast.parse("\n".join([
            "def a():",
            "   for b in c():",
            "       b()",
            "   with d() as e:",
            "       pass",
            "   return y()"
        ]))
        self.assertIsInstance(sync_tree.body[0], ast.FunctionDef)

        transformed = PytTransformer().visit(async_tree)
        self.assertIsInstance(transformed.body[0], ast.FunctionDef)

        self.assertEqual(ast.dump(transformed), ast.dump(sync_tree))

    def test_chained_function(self):
        chained_tree = ast.parse("\n".join([
            "def a():",
            "   b = c.d(e).f(g).h(i).j(k)",
        ]))

        separated_tree = ast.parse("\n".join([
            "def a():",
            "   __chain_tmp_3 = c.d(e)",
            "   __chain_tmp_2 = __chain_tmp_3.f(g)",
            "   __chain_tmp_1 = __chain_tmp_2.h(i)",
            "   b = __chain_tmp_1.j(k)",
        ]))

        transformed = PytTransformer().visit(chained_tree)
        self.assertEqual(ast.dump(transformed), ast.dump(separated_tree))

    def test_if_exp(self):
        complex_if_exp_tree = ast.parse("\n".join([
            "def a():",
            "   b = c if d.e(f) else g if h else i if j.k(l) else m",
        ]))

        separated_tree = ast.parse("\n".join([
            "def a():",
            "   __if_exp_0 = d.e(f)",
            "   __if_exp_1 = j.k(l)",
            "   b = c if __if_exp_0 else g if h else i if __if_exp_1 else m",
        ]))

        transformed = PytTransformer().visit(complex_if_exp_tree)
        self.assertEqual(ast.dump(transformed), ast.dump(separated_tree))
