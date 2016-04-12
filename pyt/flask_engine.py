import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog

sources = ["input"]
sanitizers = []
sinks = ["eval"]

sources_in_file = None
sinks_in_file = None

SourcesAndSinks = namedtuple('SourcesAndSinks', 'sources sinks')
SinkOrSourceNode = namedtuple('SinkOrSourceNode', 'trigger_word cfg_node')

def parse_sources_and_sinks(self, definition_file):
    pass

def label_contains(node, trigger_word_list):
    for trigger_word in trigger_word_list:
        if trigger_word in node.label:
            yield SinkOrSourceNode(trigger_word, node)
                    
def find_sources(cfg):
    l = list()
    for node in cfg.nodes:
        l.extend(iter(label_contains(node, sources)))
    return l
            
def find_sinks(cfg):
    l = list()
    for node in cfg.nodes:
        l.extend(iter(label_contains(node, sinks)))
    return l

def identify_sources_and_sinks(cfg):
    
    sources_in_file = find_sources(cfg)
    sinks_in_file = find_sinks(cfg)
    
    return SourcesAndSinks(sources_in_file, sinks_in_file)

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
        for sink in sources_and_sinks.sinks:
            for source in sources_and_sinks.sources:
                if source.cfg_node in sink.cfg_node.new_constraint:
                    vulnerability_log.append(Vulnerability(source.cfg_node, source.trigger_word, sink.cfg_node, sink.trigger_word))
    return vulnerability_log
   
