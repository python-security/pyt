from .base_cfg import AssignmentNode
from .constraint_table import constraint_table
from .reaching_definitions_base import ReachingDefinitionsAnalysisBase


class ReachingDefinitionsAnalysis(ReachingDefinitionsAnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def fixpointmethod(self, cfg_node):
        JOIN = self.join(cfg_node)
        # Assignment check
        if isinstance(cfg_node, AssignmentNode):
            arrow_result = JOIN
            # Get previous assignments of cfg_node.left_hand_side and remove them from JOIN
            arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)
            arrow_result = arrow_result | self.lattice.el2bv[cfg_node]
            constraint_table[cfg_node] = arrow_result
        # Default case
        else:
            constraint_table[cfg_node] = JOIN
