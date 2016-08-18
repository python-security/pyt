from cfg import AssignmentNode
from analysis_base import AnalysisBase

class ReachingDefinitionsTaintAnalysis(AnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def __init__(self, cfg):
        super(ReachingDefinitionsTaintAnalysis, self).__init__(cfg, None)
        
    def join(self, cfg_node):
        JOIN = set()
        for ingoing in cfg_node.ingoing:
            JOIN |= ingoing.old_constraint
        return JOIN

    def arrow(self, JOIN, _id):
        result = set()
        for cfg_node in JOIN:
            # if _id is not found in the LHS of cfg_node, the node will not be deleted
            if _id is not cfg_node.left_hand_side:
                result.add(cfg_node)
        return result

    def fixpointmethod(self, cfg_node):
        # Assignment: JOIN(v) arrow(id) join(v)
        if isinstance(cfg_node, AssignmentNode):
            JOIN = self.join(cfg_node)
            arrow_result = JOIN
            if not cfg_node.left_hand_side in cfg_node.right_hand_side_variables:
                arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)
            arrow_result.add(cfg_node)
            cfg_node.new_constraint = arrow_result

        else:
            # Default case join(v)
            cfg_node.new_constraint = self.join(cfg_node)

    def dep(self, q_1): # Useless to have this as a function atm
        """Represents the dep mapping from Schwartzbach."""
        for node in q_1.outgoing:
            yield node
