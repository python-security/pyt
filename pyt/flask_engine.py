import os
from cfg import CFG, generate_ast, Node

from vulnerability_log import Vulnerability, VulnerabilityLog

sources = ["input"]
sanitizers = []
sinks = ["eval"]

sources_in_file = None
sinks_in_file = None

def parse_sources_and_sinks(self, definition_file):
    pass

def label_contains(node, word_list):
    return any(word in node.label for word in word_list)
                    
def find_sources(cfg):
    for node in cfg.nodes:
        if label_contains(node, sources):
            yield node
            
def find_sinks(cfg):
    for node in cfg.nodes:
        if label_contains(node,sinks):
            yield node            

def identify_sources_and_sinks(cfg):
    
    sources_in_file = find_sources(cfg)
    sinks_in_file = find_sinks(cfg)
    
    return (sources_in_file, sinks_in_file)

def find_flask_route_functions(functions):
    for func in functions.items():
        if is_flask_route_function(func[1]):
            yield func[1]

def is_flask_route_function(function):
    return any(decorator for decorator in function.decorator_list if decorator.func.value.id == 'app' and decorator.func.attr == 'route')

def find_vulnerabilities(cfg_list):
    vulnerability_log = VulnerabilityLog()
    for cfg in cfg_list:
        sources_and_sinks = identify_sources_and_sinks(cfg)
        for sink in sources_and_sinks[1]:
            for source in sources_and_sinks[0]:
                if source in sink.new_constraint:
                    vulnerability_log.append(Vulnerability(source, sink, 'Custom message - what to write here?'))
    return vulnerability_log
   
