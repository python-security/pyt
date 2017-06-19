from .analysis_base import AnalysisBase
from .base_cfg import AssignmentNode
from .constraint_table import constraint_join
from .lattice import Lattice


class ReachingDefinitionsAnalysisBase(AnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def __init__(self, cfg):
        super().__init__(cfg, None)

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

    def fixpointmethod(self, cfg_node):
        raise NotImplementedError()

    def dep(self, q_1):
        """Represents the dep mapping from Schwartzbach."""
        for node in q_1.outgoing:
            yield node

    def get_lattice_elements(cfg_nodes):
        """Returns all assignment nodes as they are the only lattice elements
        in the reaching definitions analysis.
        This is a static method which is overwritten from the base class."""
        for node in cfg_nodes:
            if isinstance(node, AssignmentNode):
                yield node

    def equal(self, value, other):
        return value == other

    def build_lattice(self, cfg):
        self.lattice = Lattice(cfg.nodes, ReachingDefinitionsAnalysisBase)
