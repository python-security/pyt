import ast
from cfg import Node, AssignmentNode, CFG, generate_ast
from reaching_definitions import reaching_definitions_analysis

class fixed_point_analysis(object):

    def __init__(self, analysis):
        '''Fixed point analysis

        analysis must be a dataflow analysis containing a 'fixpointmethod' method that analyzes one CFG node'''
        self.analysis = analysis()
    
    def constraints_changed(cfg):
        for node in cfg.nodes:
            if node.old_constraint != node.new_constraint:
                return True
            return False

    def swap_constraints(self, cfg):
        for node in cfg.nodes:
            node.old_constraint = node.new_constraint
            node.new_constraint = None
            
    def fixpoint_runner(self, cfg):
        fixpoint_iteration(cfg)
        while constraints_changed(cfg):
            swap_constraints(cfg)
            fixpoint_iteration(cfg)
        
    def fixpoint_iteration(self, cfg):
        for node in cfg.nodes:
            self.analysis.fixpointmethod(node)
            
    
if __name__ == '__main__':
    analysis = fixed_point_analysis(reaching_definitions_analysis)
    tree = generate_ast('../example/example_inputs/example.py')
    cfg = CFG()
    cfg.create(tree)
    
    analysis.fixpoint_runner(cfg)
