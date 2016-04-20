import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog


Triggers = namedtuple('Triggers', 'sources sinks sanitizer_dict')
TriggerNode = namedtuple('TriggerNode', 'trigger_word_tuple cfg_node')
default_trigger_word_file = os.path.join(os.path.dirname(__file__), 'trigger_definitions', 'flask_trigger_words.pyt')

SANITISER_SEPARATOR = '->'
SOURCES_KEYWORD = 'sources:'
SINKS_KEYWORD = 'sinks:'

class Engine(object):
    """An engine that should be used as base class to specify how to find all sources and sinks."""

    def __init__(self, cfg_list, trigger_word_file=default_trigger_word_file):
        self.trigger_word_file = trigger_word_file
        
        if self.trigger_word_file != default_trigger_word_file:
            self.trigger_word_file = os.path.join(os.getcwd(), self.trigger_word_file)            
        self.cfg_list = cfg_list
        self.sources = list()
        self.sanitisers = list()
        self.sinks = list()
        self.sources_in_file = None
        self.sinks_in_file = None
        self.sanitisers_in_file = None
        self.run()

    def run(self):
        raise NotImplementedError('Should be implemented.')

    def parse_section(self, iterator):
        try:
            line = next(iterator).rstrip()
            while line:
                if line.rstrip():
                    if SANITISER_SEPARATOR in line:
                        line = line.split(SANITISER_SEPARATOR)
                        sink = line[0]
                        sanitisers = list(map(str.strip, line[1].split(',')))
                        yield (sink, sanitisers)
                    else:
                        yield (line, list())
                line = next(iterator).rstrip()
        except StopIteration:
            return
        
    def parse_sources_and_sinks(self):
        with open(self.trigger_word_file, 'r') as fd:
            for line in fd:
                line = line.rstrip()
                if line == SOURCES_KEYWORD:
                    self.sources = list(self.parse_section(fd))
                elif line == SINKS_KEYWORD:
                    self.sinks = list(self.parse_section(fd))
        
    def identify_triggers(self, cfg):
        sources_in_file = self.find_triggers(cfg, self.sources)
        sinks_in_file = self.find_triggers(cfg, self.sinks)
        
        sanitiser_node_dict = self.build_sanitiser_node_dict(cfg, sinks_in_file)
    
        return Triggers(sources_in_file, sinks_in_file, sanitiser_node_dict)

    def find_triggers(self, cfg, trigger_word_list):
        l = list()
        for node in cfg.nodes:
            l.extend(iter(self.label_contains(node, trigger_word_list)))
        return l
      
    def label_contains(self, node, trigger_word_list):
        for trigger_word_tuple in trigger_word_list:
            if trigger_word_tuple[0] in node.label:
                yield TriggerNode(trigger_word_tuple, node)
            
    def build_sanitiser_node_dict(self, cfg, sinks_in_file):
        sanitisers = list()
        for sink in sinks_in_file:
            sanitisers.extend(sink[1])

        sanitiser_in_file = self.find_triggers(cfg, sanitisers)
            
        sanitiser_node_dict = dict()
        for sanitiser in sanitisers:
            sanitiser_node_dict[sanitiser] = self.find_sanitiser_nodes(sanitiser, sanitisers_in_file)

        return sanitiser_node_dict

    def find_sanitiser_nodes(self, sanitiser, sanitisers_in_file):
        for node in sanitisers_in_file:
            if node.trigger_word_tuple[0] == sanitiser:
                yield node.cfg_node

    def is_unsanitized(self, source, sink, sanitiser_dict):
        for sanitiser in sink.trigger_word_tuple[1]:
            cfg_node = sanitiser_dict[sanitiser]
            if not cfg_node in sink.new_constraint:
                return True
        return False
              
    def find_vulnerabilities(self):
        self.parse_sources_and_sinks()
        vulnerability_log = VulnerabilityLog()
        for cfg in self.cfg_list:
            triggers = self.identify_triggers(cfg)
            
            for sink in triggers.sinks:
                for source in triggers.sources:
                    if source.cfg_node in sink.cfg_node.new_constraint:
                        if self.is_unsanitized(source, sink, triggers.sanitiser_dict):
                           vulnerability_log.append(Vulnerability(source.cfg_node, source.trigger_word, sink.cfg_node, sink.trigger_word))

        return vulnerability_log
   
