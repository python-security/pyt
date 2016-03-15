import ast
from cfg import Node, AssignmentNode, CFG, generate_ast


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
