import ast
from cfg import Node, AssignmentNode

def join(fixpoint_constraint, cfg_node):
    s = set()
    for ingoing in cfg_node.ingoing(node):
        cfg_node.old_constraint.join(ingoing.constraint)
    return s


def arrow(constraint_set, var):
    for node in constraint_set:
        if isinstance(node, AssignmentNode):
            if var in node.left_hand_side:
                constraint_set.remove(left_hand_side)
        
def fixpointmethod(old_fixpoint_constraint, node):
    if isinstance(node.ast_type, AssignmentNode):
        j = join(node)
        arrow(j, node.left_hand_side)
        return j.join(node)
           
    elif node.ast_type == "START":
        return set()

    elif node.ast_type == "EXIT":
        return set()

    else:
        return FixpointConstraint(old_fixpoint_constraint.old_fixpoint,
                                  join(fixpoint_constraint, node),
                                  node)




fixpoint = list()

def fixpoint_runner(cfg):
    fixpoint = list()
    for x in range(len(cfg.nodes)):
        fixpoint.append(None)

    temp_fixpoint = fixpoint
    fixpoint = fixpoint_iteration(cfg)
    
    while temp_fixpoint is not fixpoint:
        temp_fixpoint = fixpoint
        fixpoint = fixpoint_iteration(cfg)
        
def fixpoint_iteration(cfg):
    fixpoint = list()
    for x in range(len(cfg.nodes)):
        fixpoint.append(None)
    
    for i, cfg_node in enumerate(cfg.nodes):
        fixpoint[i] = fixpointmethod(node)
    return fixpoint

