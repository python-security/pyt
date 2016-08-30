from cfg import AssignmentNode
from analysis_base import AnalysisBase

class ReachingDefinitionsTaintAnalysis(AnalysisBase):
    """Reaching definitions analysis rules implemented."""

    def __init__(self, cfg, lattice):
        super(ReachingDefinitionsTaintAnalysis, self).__init__(cfg, None)
        self.lattice = lattice

    def get_assignment_nodes(self, iterable):
        for node in iterable:
            if isinstance(node, AssignmentNode):
                yield node

    def join(self, cfg_node):
        #if isinstance(cfg_node, AssignmentNode):
         #   return self.lattice.join([cfg_node], self.get_assignment_nodes(cfg_node.ingoing))
        #else:
        return self.lattice.constraint_join(cfg_node.ingoing)

    def arrow(self, JOIN, _id):
        r = JOIN
        for node in self.lattice.get_elements(JOIN):
            if node.left_hand_side == _id.left_hand_side:
                r = r ^ self.lattice.d[node]
        return r

    def fixpointmethod(self, cfg_node):
        JOIN = self.join(cfg_node)
        if isinstance(cfg_node, AssignmentNode):
            arrow_result = JOIN

            if not cfg_node.left_hand_side in cfg_node.right_hand_side_variables:
                arrow_result = self.arrow(JOIN, cfg_node)

            arrow_result = arrow_result | self.lattice.d[cfg_node]
            self.lattice.table[cfg_node] = arrow_result
        else:
            self.lattice.table[cfg_node] = JOIN

    def dep(self, q_1): # Useless to have this as a function atm
        """Represents the dep mapping from Schwartzbach."""
        for node in q_1.outgoing:
            yield node
