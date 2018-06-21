from ..base_test_case import BaseTestCase


class CFGBaseTestCase(BaseTestCase):

    def assertInCfg(self, connections):
        """Asserts that all connections in the connections list exists in the cfg,
        as well as that all connections not in the list do not exist.

        Args:
            connections(list[tuple]): the node at index 0 of the tuple has
                                      to be in the new_constraint set of the node
                                      at index 1 of the tuple.
        """
        for connection in connections:
            self.assertIn(
                self.cfg.nodes[connection[0]],
                self.cfg.nodes[connection[1]].outgoing,
                str(connection) + " expected to be connected"
            )
            self.assertIn(
                self.cfg.nodes[connection[1]],
                self.cfg.nodes[connection[0]].ingoing,
                str(connection) + " expected to be connected"
            )

        nodes = len(self.cfg.nodes)

        for element in range(nodes):
            for sets in range(nodes):
                if not (element, sets) in connections:
                    self.assertNotIn(
                        self.cfg.nodes[element],
                        self.cfg.nodes[sets].outgoing,
                        "(%s <- %s)" % (element, sets) + " expected to be disconnected"
                    )
                    self.assertNotIn(
                        self.cfg.nodes[sets],
                        self.cfg.nodes[element].ingoing,
                        "(%s <- %s)" % (sets, element) + " expected to be disconnected"
                    )

    def assertLineNumber(self, node, line_number):
        self.assertEqual(node.line_number, line_number)

    def cfg_list_to_dict(self, list):
        """This method converts the CFG list to a dict, making it easier to find nodes to test.
        This method assumes that no nodes in the code have the same label.
        """
        return {x.label: x for x in list}
