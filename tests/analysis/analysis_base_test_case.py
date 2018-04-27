from collections import namedtuple

from ..base_test_case import BaseTestCase

from pyt.analysis.constraint_table import (
    constraint_table,
    initialize_constraint_table
)
from pyt.analysis.fixed_point import FixedPointAnalysis
from pyt.analysis.lattice import Lattice


def clear_constraint_table():
    for key in list(constraint_table):
        del constraint_table[key]


class AnalysisBaseTestCase(BaseTestCase):
    connection = namedtuple(
        'connection',
        (
            'constraintset',
            'element'
        )
    )

    def setUp(self):
        self.cfg = None

    def assertInCfg(self, connections, lattice):
        """Assert that all connections in the connections list exists in the cfg,
        as well as all connections not in the list do not exist.

        Args:
            connections(list[tuples]): the node at index 0 of the tuple has
                                       to be in the new_constraint set of the node
                                       at index 1 of the tuple.
            lattice(Lattice): The lattice we're analysing.
        """
        for connection in connections:
            self.assertEqual(lattice.in_constraint(
                self.cfg.nodes[connection[0]],
                self.cfg.nodes[connection[1]]),
                True,
                str(connection) + " expected to be connected")
        nodes = len(self.cfg.nodes)

        for element in range(nodes):
            for sets in range(nodes):
                if (element, sets) not in connections:
                    self.assertEqual(
                        lattice.in_constraint(
                            self.cfg.nodes[element],
                            self.cfg.nodes[sets]
                        ),
                        False,
                        "(%s,%s)" % (self.cfg.nodes[element], self.cfg.nodes[sets]) + " expected to be disconnected"
                    )

    def constraints(self, list_of_constraints, node_number):
        for c in list_of_constraints:
            yield (c, node_number)

    def run_analysis(self, path):
        self.cfg_create_from_file(path)
        clear_constraint_table()
        initialize_constraint_table([self.cfg])
        self.analysis = FixedPointAnalysis(self.cfg)
        self.analysis.fixpoint_runner()
        return Lattice(self.cfg.nodes)

    def string_compare_alnum(self, output, expected_string):
        return (
            [char for char in output if char.isalnum()] ==
            [char for char in expected_string if char.isalnum()]
        )
