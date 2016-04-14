import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog


SourcesAndSinks = namedtuple('SourcesAndSinks', 'sources sinks')
SinkOrSourceNode = namedtuple('SinkOrSourceNode', 'trigger_word cfg_node')
default_trigger_word_file = os.path.join('pyt', 'trigger_definitions', 'flask_trigger_words.pyt')

class Engine(object):

    def __init__(self, cfg_list, trigger_word_file=default_trigger_word_file):
        self.trigger_word_file = trigger_word_file
        self.cfg_list = cfg_list
        self.sources = list()
        self.sanitizers = list()
        self.sinks = list()
        self.sources_in_file = None
        self.sinks_in_file = None
        self.run()

    def run(self):
        raise NotImplementedError('Should be implemented.')

    def parse_sources_and_sinks(self):
        file_data = ''
        path = os.path.join(os.getcwd(), self.trigger_word_file)
        with open(path, 'r') as fd:
            is_source = None
            for line in fd:
                if 'sources:' in line:
                    is_source = True
                elif 'sinks:' in line:
                    is_source = False
                elif is_source:
                    self.sources.append(line.rstrip())
                elif not is_source:
                    self.sinks.append(line.rstrip())

    def label_contains(self, node, trigger_word_list):
        for trigger_word in trigger_word_list:
            if trigger_word in node.label:
                yield SinkOrSourceNode(trigger_word, node)
            
    def find_sources(self, cfg):
        l = list()
        for node in cfg.nodes:
            l.extend(iter(self.label_contains(node, self.sources)))
        return l
            
    def find_sinks(self, cfg):
        l = list()
        for node in cfg.nodes:
            l.extend(iter(self.label_contains(node, self.sinks)))
        return l

    def identify_sources_and_sinks(self, cfg):
        sources_in_file = self.find_sources(cfg)
        sinks_in_file = self.find_sinks(cfg)
        return SourcesAndSinks(sources_in_file, sinks_in_file)

    def find_vulnerabilities(self):
        self.parse_sources_and_sinks()
        vulnerability_log = VulnerabilityLog()
        for cfg in self.cfg_list:
            sources_and_sinks = self.identify_sources_and_sinks(cfg)
            for sink in sources_and_sinks.sinks:
                for source in sources_and_sinks.sources:
                    if source.cfg_node in sink.cfg_node.new_constraint:
                        vulnerability_log.append(Vulnerability(source.cfg_node, source.trigger_word, sink.cfg_node, sink.trigger_word))
        return vulnerability_log
   
