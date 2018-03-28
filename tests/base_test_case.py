"""A module that contains a base class that has helper methods for testing PyT."""
import unittest

from pyt.ast_helper import generate_ast
from pyt.expr_visitor import interprocedural
from pyt.module_definitions import project_definitions


class BaseTestCase(unittest.TestCase):
    """A base class that has helper methods for testing PyT."""

    def assertInCfg(self, connections):
        """Asserts that all connections in the connections list exists in the cfg,
        as well as that all connections not in the list do not exist.

        Args:
            connections(list[tuple]): the node at index 0 of the tuple has
                                      to be in the new_constraint set of the node
                                      at index 1 of the tuple.
        """
        for connection in connections:
            self.assertIn(self.cfg.nodes[connection[0]], self.cfg.nodes[connection[1]].outgoing, str(connection) + " expected to be connected")
            self.assertIn(self.cfg.nodes[connection[1]], self.cfg.nodes[connection[0]].ingoing, str(connection) + " expected to be connected")

        nodes = len(self.cfg.nodes)

        for element in range(nodes):
            for sets in range(nodes):
                if not (element, sets) in connections:
                    self.assertNotIn(self.cfg.nodes[element], self.cfg.nodes[sets].outgoing, "(%s <- %s)" % (element, sets)  +  " expected to be disconnected")
                    self.assertNotIn(self.cfg.nodes[sets], self.cfg.nodes[element].ingoing, "(%s <- %s)" % (sets, element)  +  " expected to be disconnected")

    def assertConnected(self, node, successor):
        """Asserts that a node is connected to its successor.
        This means that node has successor in its outgoing and
        successor has node in its ingoing."""

        self.assertIn(successor, node.outgoing,
                       '\n%s was NOT found in the outgoing list of %s containing: ' % (successor.label, node.label) + '[' + ', '.join([x.label for x in node.outgoing]) + ']')

        self.assertIn(node, successor.ingoing,
                       '\n%s was NOT found in the ingoing list of %s containing: ' % (node.label, successor.label) + '[' + ', '.join([x.label for x in successor.ingoing]) + ']')

    def assertNotConnected(self, node, successor):
        """Asserts that a node is not connected to its successor.
        This means that node does not the successor in its outgoing and
        successor does not have the node in its ingoing."""

        self.assertNotIn(successor, node.outgoing,
                       '\n%s was mistakenly found in the outgoing list of %s containing: ' % (successor.label, node.label) + '[' + ', '.join([x.label for x in node.outgoing]) + ']')

        self.assertNotIn(node, successor.ingoing,
                         '\n%s was mistakenly found in the ingoing list of %s containing: ' % (node.label, successor.label) + '[' + ', '.join([x.label for x in successor.ingoing]) + ']')

    def assertLineNumber(self, node, line_number):
        self.assertEqual(node.line_number, line_number)

    def cfg_list_to_dict(self, list):
        """This method converts the CFG list to a dict, making it easier to find nodes to test.
        This method assumes that no nodes in the code have the same label"""
        return {x.label: x for x in list}

    def assert_length(self, _list, *, expected_length):
        actual_length = len(_list)
        self.assertEqual(expected_length, actual_length)

    def cfg_create_from_file(self, filename, project_modules=list(), local_modules=list()):
        project_definitions.clear()
        tree = generate_ast(filename)
        self.cfg = interprocedural(tree, project_modules, local_modules, filename)

    def string_compare_alpha(self, output, expected_string):
        return [char for char in output if char.isalpha()] \
                == \
               [char for char in expected_string if char.isalpha()]

    def string_compare_alnum(self, output, expected_string):
        return [char for char in output if char.isalnum()] \
                == \
               [char for char in expected_string if char.isalnum()]
