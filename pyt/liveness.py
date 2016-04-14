from cfg import AssignmentNode
from copy import deepcopy
import ast

from vars_visitor import VarsVisitor

class liveness_analysis(object):
    variables = dict()

    def __init__(self, cfg):
        self.annotate_cfg(cfg)
    
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
            JOIN.update(self.variables[cfg_node])  # set union
            
            cfg_node.new_constraint = JOIN

        # if for Assignment case: Join(v) \ {id} u vars(E).
        elif isinstance(cfg_node, AssignmentNode): 
            JOIN = self.join(cfg_node)

            JOIN.discard(cfg_node.ast_node.targets[0].id)  # set difference
            JOIN.update(self.variables[cfg_node])  # set union
 
            cfg_node.new_constraint = JOIN

        # if for entry and exit cases: {}.
        elif cfg_node.ast_type == "ENTRY" or cfg_node.ast_type == "EXIT":
            pass
        # else for other cases.
        else:
            cfg_node.new_constraint = self.join(cfg_node)

    def annotate_cfg(self, cfg):
        for node in cfg.nodes:
            if node.ast_node:
                variables_visitor = VarsVisitor()
                variables_visitor.visit(node.ast_node)
                self.variables[node] = variables_visitor.result
