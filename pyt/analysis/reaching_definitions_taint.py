from .constraint_table import (
    constraint_join,
    constraint_table
)
from ..core.node_types import AssignmentNode
from .lattice import Lattice


class ReachingDefinitionsTaintAnalysis():
    def __init__(self, cfg):
        self.cfg = cfg
        self.lattice = Lattice(cfg.nodes)

    def fixpointmethod(self, cfg_node):
        """The most important part of PyT, where we perform
        the variant of reaching definitions to find where sources reach.
        """
        JOIN = self.join(cfg_node)
        # Assignment check
        if isinstance(cfg_node, AssignmentNode):
            arrow_result = JOIN

            # Reassignment check
            if cfg_node.left_hand_side not in cfg_node.right_hand_side_variables:
                # Get previous assignments of cfg_node.left_hand_side and remove them from JOIN
                arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)

            arrow_result = arrow_result | self.lattice.el2bv[cfg_node]
            constraint_table[cfg_node] = arrow_result
        # Default case
        else:
            constraint_table[cfg_node] = JOIN

    def join(self, cfg_node):
        """Joins all constraints of the ingoing nodes and returns them.
        This represents the JOIN auxiliary definition from Schwartzbach."""
        return constraint_join(cfg_node.ingoing)

    def arrow(self, JOIN, _id):
        """Removes all previous assignments from JOIN that have the same left hand side.
        This represents the arrow id definition from Schwartzbach."""
        r = JOIN
        for node in self.lattice.get_elements(JOIN):
            if node.left_hand_side == _id:
                r = r ^ self.lattice.el2bv[node]
        return r

    def dep(self, q_1):
        """Represents the dep mapping from Schwartzbach."""
        for node in q_1.outgoing:
            yield node
