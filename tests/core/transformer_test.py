import ast
import unittest

from pyt.core.transformer import AsyncTransformer


class TransformerTest(unittest.TestCase):
    """Tests for the AsyncTransformer."""

    def test_async_removed_by_transformer(self):
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

        transformed = AsyncTransformer().visit(async_tree)
        self.assertIsInstance(transformed.body[0], ast.FunctionDef)

        self.assertEqual(ast.dump(transformed), ast.dump(sync_tree))
