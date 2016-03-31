import os
from cfg import CFG, generate_ast, Node

from reaching_definitions import reaching_definitions_analysis
from fixed_point import fixed_point_analysis
from vulnerability_log import Vulnerability, VulnerabilityLog

sources = ["input"]
sinks = ["eval"]

class flask_engine(object):
    def analyze_file(self):
        file = "../example/vulnerable_code/simple_vulnerability.py"
        
        self.cfg = CFG()
        tree = generate_ast(file)
        self.cfg.create(tree)
        
        self.analysis = fixed_point_analysis(reaching_definitions_analysis)
        self.analysis.fixpoint_runner(self.cfg)
        print(repr(self.cfg))
        
    def label_contains(self, node, word_list):
        return any(word in node.label for word in word_list)
            
            
    def find_sources(self):
        for node in self.cfg.nodes:
            if self.label_contains(node, sources):
                yield node
            
    def find_sinks(self):
        for node in self.cfg.nodes:
            if self.label_contains(node,sinks):
                yield node            

    def run(self):
        self.analyze_file()
        sources_in_file = self.find_sources()
        sinks_in_file = self.find_sinks()
        
        vulnerability_log = VulnerabilityLog()
        
        for sink in sinks_in_file:            
            for source in sources_in_file:
                if source in sink.new_constraint:
                    vulnerability_log.append(Vulnerability(source, sink, "crazy"))

        vulnerability_log.print_report()

f = flask_engine()
f.run()

