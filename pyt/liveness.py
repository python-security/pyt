from cfg import AssignmentNode
from copy import deepcopy
import ast

from vars_visitor import VarsVisitor
from analysis_base import AnalysisBase

class LivenessAnalysis(AnalysisBase):
    '''Liveness analysis rules implemented.'''

    def __init__(self, cfg):
        super(LivenessAnalysis, self).__init__(cfg, VarsVisitor)
    
    def join(self, cfg_node):
        JOIN = set()
        for outgoing in cfg_node.outgoing:
            if outgoing.old_constraint:
                JOIN |= outgoing.old_constraint
        return JOIN
    
    def fixpointmethod(self, cfg_node):
        # if for Condition and call case: Join(v) u vars(E).
        if cfg_node.ast_type == ast.Compare.__name__ or cfg_node.ast_type == ast.Call.__name__:
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
