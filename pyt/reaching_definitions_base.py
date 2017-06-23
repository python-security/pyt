from .analysis_base import AnalysisBase
from .base_cfg import AssignmentNode
from .constraint_table import constraint_join
from .lattice import Lattice
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class ReachingDefinitionsAnalysisBase(AnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def __init__(self, cfg):
        super().__init__(cfg, None)

    def join(self, cfg_node):
        """Joins all constraints of the ingoing nodes and returns them.
        This represents the JOIN auxiliary definition from Schwartzbach."""
        if cfg_node.label.startswith('subp'):
            logger.debug("special len(cfg_node.ingoing) is %s", len(cfg_node.ingoing))
            logger.debug("special cfg_node.ingoing is %s", cfg_node.ingoing)
            logger.debug("special cfg_node.outgoing is %s", cfg_node.outgoing)
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
