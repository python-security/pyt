import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog


Triggers = namedtuple('Triggers', 'sources sinks sanitisers')
TriggerNode = namedtuple('TriggerNode', 'trigger_word cfg_node')
default_trigger_word_file = os.path.join(os.path.dirname(__file__), 'trigger_definitions', 'flask_trigger_words.pyt')

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
                    yield line
                line = next(iterator).rstrip()
        except StopIteration:
            return
    
    def parse_sources_and_sinks(self):
        with open(self.trigger_word_file, 'r') as fd:
            for line in fd:
                line = line.rstrip()
                if line == 'sources:':
                    self.sources = list(self.parse_section(fd))
                elif line == 'sinks:':
                    self.sinks = list(self.parse_section(fd))
                elif line == 'sanitisers:':
                    self.sanitisers = list(self.parse_section(fd))
            
    def label_contains(self, node, trigger_word_list):
        for trigger_word in trigger_word_list:
            if trigger_word in node.label:
                yield TriggerNode(trigger_word, node)
            
    def find_triggers(self, cfg, trigger_word_list):
        l = list()
        for node in cfg.nodes:
            l.extend(iter(self.label_contains(node, trigger_word_list)))
        return l

    def identify_triggers(self, cfg):
        sources_in_file = self.find_triggers(cfg, self.sources)
        sinks_in_file = self.find_triggers(cfg, self.sinks)
        sanitisers_in_file = self.find_triggers(cfg, self.sanitisers)
        
        return Triggers(sources_in_file, sinks_in_file, sanitisers_in_file)

    def find_vulnerabilities(self):
        self.parse_sources_and_sinks()
        vulnerability_log = VulnerabilityLog()
        for cfg in self.cfg_list:
            sources_and_sinks = self.identify_triggers(cfg)
            for sink in sources_and_sinks.sinks:
                for source in sources_and_sinks.sources:
                    if source.cfg_node in sink.cfg_node.new_constraint:
                        if not any(sanitiser in sink.cfg_node.new_constraint for sanitiser in sources_and_sinks.sanitisers):
                            vulnerability_log.append(Vulnerability(source.cfg_node, source.trigger_word, sink.cfg_node, sink.trigger_word))
        return vulnerability_log
   
