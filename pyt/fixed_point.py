import ast
from cfg import Node, AssignmentNode, CFG, generate_ast

def join(cfg_node):
    JOIN = set()
    for ingoing in cfg_node.ingoing:
        JOIN |= ingoing.old_constraint
    return JOIN

def arrow(JOIN, _id):
    result = set()
    for cfg_node in JOIN:
        if len(_id.intersection(cfg_node.left_hand_side)) == 0: # if there is no intersection _id is not found in the LHS of cfg_node, the node will therefore not be deleted
            result.add(cfg_node)
    return result
        
def fixpointmethod(cfg_node):
    # Assignment: JOIN(v) arrow(id) join(v)
    if isinstance(cfg_node, AssignmentNode):
        JOIN = join(cfg_node)
        arrow_result = arrow(JOIN, cfg_node.left_hand_side)
        arrow_result.add(cfg_node)
        cfg_node.new_constraint = arrow_result
           
    else:
        # Default case join(v)
        cfg_node.new_constraint = join(cfg_node)

def constraints_changed(cfg):
    for node in cfg.nodes:
        if node.old_constraint != node.new_constraint:
            return True
    return False

def swap_constraints(cfg):
    for node in cfg.nodes:
        node.old_constraint = node.new_constraint
        node.new_constraint = None

def fixpoint_runner(cfg):
    fixpoint_iteration(cfg)
    while constraints_changed(cfg):
        swap_constraints(cfg)
        fixpoint_iteration(cfg)
        
def fixpoint_iteration(cfg):
    for node in cfg.nodes:
        fixpointmethod(node)

    
if __name__ == '__main__':
    tree = generate_ast('../example/example_inputs/example.py')
    cfg = CFG()
    cfg.create(tree)
    
    fixpoint_runner(cfg)
