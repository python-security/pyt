from cfg import AssignmentNode
from analysis_base import AnalysisBase
from constraint_table import constraint_table, constraint_join
from lattice import Lattice


class ReachingDefinitionsTaintAnalysis(AnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def __init__(self, cfg):
        super(ReachingDefinitionsTaintAnalysis, self).__init__(cfg, None)

    def join(self, cfg_node):
        """Joins all constraints of the ingoing nodes and returns them.
        This represents the JOIN auxiliary definition from Schwartzbach."""
        return constraint_join(cfg_node.ingoing)

    def arrow(self, JOIN, _id):
        """Removes all assignments from JOIN that has _id on the left hand side.
        This represents the arrow id definition from Schwartzbach."""
        r = JOIN
        for node in self.lattice.get_elements(JOIN):
            if node.left_hand_side == _id.left_hand_side:
                r = r ^ self.lattice.el2bv[node]
        return r

    def fixpointmethod(self, cfg_node):
        JOIN = self.join(cfg_node)
        # Assignment check
        if isinstance(cfg_node, AssignmentNode):
            arrow_result = JOIN

            # Reassignment check:
            if cfg_node.left_hand_side not in\
               cfg_node.right_hand_side_variables:
                arrow_result = self.arrow(JOIN, cfg_node)

            arrow_result = arrow_result | self.lattice.el2bv[cfg_node]
            constraint_table[cfg_node] = arrow_result
        # Default case:
        else:
            constraint_table[cfg_node] = JOIN

    def dep(self, q_1):
        """Represents the dep mapping from Schwartzbach."""
        for node in q_1.outgoing:
            yield node

    def get_lattice_elements(cfg_nodes):
        """Returns all assignment nodes as they are the only lattice elements
        in the reaching definitions analysis.
        This is a static method which is overwritten from the base class.
        """
        for node in cfg_nodes:
            if isinstance(node, AssignmentNode):
                yield node

    def equal(self, value, other):
        return value == other

    def build_lattice(self, cfg):
        self.lattice = Lattice(cfg.nodes, ReachingDefinitionsTaintAnalysis)
