"""Module implements liveness analysis."""
from cfg import AssignmentNode
from copy import deepcopy
from ast import NodeVisitor, Compare, Call

from analysis_base import AnalysisBase

class LivenessAnalysis(AnalysisBase):
    """Implement liveness analysis rules."""

    def __init__(self, cfg):
        """Initialize using parent with the given cfg."""
        super(LivenessAnalysis, self).__init__(cfg, VarsVisitor)
    
    def join(self, cfg_node):
        """Join outgoing old constraints and return them as a set."""
        JOIN = set()
        for outgoing in cfg_node.outgoing:
            if outgoing.old_constraint:
                JOIN |= outgoing.old_constraint
        return JOIN
    
    def fixpointmethod(self, cfg_node):
        """Setting the constraints of the given cfg node obeying the liveness analysis rules."""
        # if for Condition and call case: Join(v) u vars(E).
        if cfg_node.ast_type == Compare.__name__ or cfg_node.ast_type == Call.__name__:
            JOIN = self.join(cfg_node)            
            JOIN.update(self.annotated_cfg_nodes[cfg_node])  # set union
            
            cfg_node.new_constraint = JOIN

        # if for Assignment case: Join(v) \ {id} u vars(E).
        elif isinstance(cfg_node, AssignmentNode): 
            JOIN = self.join(cfg_node)

            JOIN.discard(cfg_node.ast_node.targets[0].id)  # set difference
            JOIN.update(self.annotated_cfg_nodes[cfg_node])  # set union
 
            cfg_node.new_constraint = JOIN

        # if for entry and exit cases: {}.
        elif cfg_node.ast_type == "ENTRY" or cfg_node.ast_type == "EXIT":
            pass
        # else for other cases.
        else:
            cfg_node.new_constraint = self.join(cfg_node)


class VarsVisitor(NodeVisitor):
    """Class that finds all variables needed for the liveness analysis."""

    def __init__(self):
        """Initialise list of results."""
        self.result = list()

    def visit_Name(self, node):
        self.result.append(node.id)

    #  Condition and call rule
    def visit_Call(self, node):
        for arg in node.args:
            self.visit(arg)
        for keyword in node.keywords:
            self.visit(keyword)
            
    def visit_keyword(self, node):
        self.visit(node.value)

    def visit_Compare(self, node):
        self.generic_visit(node)

    #  Assignment rule                
    def visit_Assign(self, node): 
        self.visit(node.value)
