from .base_cfg import AssignmentNode
from .constraint_table import constraint_table
from .reaching_definitions_base import ReachingDefinitionsAnalysisBase
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class ReachingDefinitionsTaintAnalysis(ReachingDefinitionsAnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def fixpointmethod(self, cfg_node):
        JOIN = self.join(cfg_node)
        # Assignment check
        if isinstance(cfg_node, AssignmentNode):
            arrow_result = JOIN

            # vv_result is necessary to know `image_name = image_name.replace('..', '')` is a reassignment.
            if cfg_node.vv_result:
                logger.debug("So cfg_node.vv_result is a thing, for cfg_node %s", cfg_node)
                if cfg_node.left_hand_side not in cfg_node.vv_result:
                    # Get previous assignments of cfg_node.left_hand_side and remove them from JOIN
                    arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)
            # Other reassignment check
            elif cfg_node.left_hand_side not in cfg_node.right_hand_side_variables:
                # Get previous assignments of cfg_node.left_hand_side and remove them from JOIN
                arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)

            arrow_result = arrow_result | self.lattice.el2bv[cfg_node]
            constraint_table[cfg_node] = arrow_result
        # Default case
        else:
            constraint_table[cfg_node] = JOIN
