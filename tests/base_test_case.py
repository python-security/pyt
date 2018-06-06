"""A module that contains a base class that has helper methods for testing PyT."""
import unittest

from pyt.cfg import make_cfg
from pyt.core.ast_helper import generate_ast
from pyt.core.module_definitions import project_definitions


class BaseTestCase(unittest.TestCase):
    """A base class that has helper methods for testing PyT."""

    def assert_length(self, _list, *, expected_length):
        actual_length = len(_list)
        self.assertEqual(expected_length, actual_length)

    def cfg_create_from_file(
        self,
        filename,
        project_modules=list(),
        local_modules=list()
    ):
        project_definitions.clear()
        tree = generate_ast(filename)
        self.cfg = make_cfg(
            tree,
            project_modules,
            local_modules,
            filename
        )
