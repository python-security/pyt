import ast
import argparse

from cfg import Node, AssignmentNode, CFG, generate_ast
from reaching_definitions import reaching_definitions_analysis
from liveness import liveness_analysis

class fixed_point_analysis(object):

    def __init__(self, cfg, analysis):
        '''Fixed point analysis

        analysis must be a dataflow analysis containing a 'fixpointmethod' method that analyzes one CFG node'''
        self.analysis = analysis(cfg)
        self.cfg = cfg
    
    def constraints_changed(self):
        return any(node.old_constraint != node.new_constraint for node in self.cfg.nodes)
        
    def swap_constraints(self):
        for node in self.cfg.nodes:
            node.old_constraint = node.new_constraint
            node.new_constraint = None
            
    def fixpoint_runner(self):
        self.fixpoint_iteration()
        while self.constraints_changed():
            self.swap_constraints()
            self.fixpoint_iteration()
        
    def fixpoint_iteration(self):
        for node in self.cfg.nodes:
            self.analysis.fixpointmethod(node)
            

def analyse(cfg_list, *, analysis_type):
    for cfg in cfg_list:
        analysis = fixed_point_analysis(cfg, analysis_type)
        analysis.fixpoint_runner()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('filename', help='Filename of the file that should be analysed.', type=str)
    parser.add_argument('-l', '--liveness', help='Toggle liveness analysis.', action='store_true')
    parser.add_argument('-r', '--reaching', help='Toggle reaching definitions analysis', action='store_true')

    args = parser.parse_args()

    tree = generate_ast(args.filename)
    cfg = CFG()
    cfg.create(tree)

    def run_analysis(cfg, analysis_type):
        analysis = fixed_point_analysis(cfg, analysis_type)
        analysis.fixpoint_runner()
        for cfg_node in cfg.nodes:
            print(cfg_node)
            print(cfg_node.new_constraint)

    if args.liveness:
        run_analysis(cfg, liveness_analysis)
    if args.reaching:
        run_analysis(cfg, reaching_definitions_analysis)

