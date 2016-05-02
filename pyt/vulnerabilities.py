import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog


Triggers = namedtuple('Triggers', 'sources sinks sanitiser_dict')
TriggerNode = namedtuple('TriggerNode', 'trigger_word_tuple cfg_node')
TriggerWordTuple = namedtuple('TriggerWordTuple', 'trigger_word sanitisers')
Sanitiser = namedtuple('Sanitiser', 'trigger_word cfg_node')
Definitions = namedtuple('Definitions', 'sources sinks')

default_trigger_word_file = os.path.join(os.path.dirname(__file__), 'trigger_definitions', 'flask_trigger_words.pyt')

SANITISER_SEPARATOR = '->'
SOURCES_KEYWORD = 'sources:'
SINKS_KEYWORD = 'sinks:'

def parse_section(iterator):
    try:
        line = next(iterator).rstrip()
        while line:
            if line.rstrip():
                if SANITISER_SEPARATOR in line:
                    line = line.split(SANITISER_SEPARATOR)
                    sink = line[0].rstrip()
                    sanitisers = list(map(str.strip, line[1].split(',')))
                    yield (sink, sanitisers)
                else:
                    yield (line, list())
            line = next(iterator).rstrip()
    except StopIteration:
        return
        
def parse(trigger_word_file=default_trigger_word_file):
    sources = list()
    sinks = list()
    with open(trigger_word_file, 'r') as fd:
        for line in fd:
            line = line.rstrip()
            if line == SOURCES_KEYWORD:
                sources = list(parse_section(fd))
            elif line == SINKS_KEYWORD:
                sinks = list(parse_section(fd))
    return Definitions(sources, sinks)
        
def identify_triggers(cfg, sources, sinks):
    sources_in_file = find_triggers(cfg, sources)
    sinks_in_file = find_triggers(cfg, sinks)
    
    sanitiser_node_dict = build_sanitiser_node_dict(cfg, sinks_in_file)
    
    return Triggers(sources_in_file, sinks_in_file, sanitiser_node_dict)

def find_triggers(cfg, trigger_word_list):
    l = list()
    for node in cfg.nodes:
        l.extend(iter(label_contains(node, trigger_word_list)))
    return l
      
def label_contains(node, trigger_words):
    for trigger_word_tuple in trigger_words:
        if trigger_word_tuple[0] in node.label:
            trigger_word = trigger_word_tuple[0]
            sanitisers = trigger_word_tuple[1]
            yield TriggerNode(TriggerWordTuple(trigger_word, sanitisers), node)

def build_sanitiser_node_dict(cfg, sinks_in_file):
    sanitisers = list()
    for sink in sinks_in_file:
        sanitisers.extend(sink.trigger_word_tuple.sanitisers)

    sanitisers_in_file = list()
    for sanitiser in sanitisers:
        for cfg_node in cfg.nodes:
            if sanitiser in cfg_node.label:
                sanitisers_in_file.append(Sanitiser(sanitiser, cfg_node))

    sanitiser_node_dict = dict()
    for sanitiser in sanitisers:
        sanitiser_node_dict[sanitiser] = list(find_sanitiser_nodes(sanitiser, sanitisers_in_file))
    return sanitiser_node_dict

def find_sanitiser_nodes(sanitiser, sanitisers_in_file):
    for sanitiser_tuple  in sanitisers_in_file:
        if sanitiser == sanitiser_tuple.trigger_word:
            yield sanitiser_tuple.cfg_node

def is_sanitized(sink, sanitiser_dict):
    for sanitiser in sink.trigger_word_tuple.sanitisers:
        for cfg_node in sanitiser_dict[sanitiser]:
            if cfg_node in sink.cfg_node.new_constraint:
                return True
    return False

def get_vulnerability(source, sink, triggers):
    if source.cfg_node in sink.cfg_node.new_constraint:
        source_trigger_word = source.trigger_word_tuple.trigger_word
        sink_trigger_word = sink.trigger_word_tuple.trigger_word
        if not is_sanitized(sink, triggers.sanitiser_dict):
            return Vulnerability(source.cfg_node, source_trigger_word, sink.cfg_node, sink_trigger_word)
        elif is_sanitized(sink, triggers.sanitiser_dict):
            return SanitisedVulnerability(source.cfg_node, source_trigger_word, sink.cfg_node, sink_trigger_word, sink.trigger_word_tuple.sanitisers)
    return None

def find_vulnerabilities(cfg_list, trigger_word_file=default_trigger_word_file):
    definitions = parse(trigger_word_file)
    vulnerability_log = VulnerabilityLog()
    for cfg in cfg_list:
        triggers = identify_triggers(cfg, definitions.sources, definitions.sinks)
        for sink in triggers.sinks:
            for source in triggers.sources:
                vulnerability = get_vulnerability(source, sink, triggers)
                if vulnerability:
                    vulnerability_log.append(vulnerability)
    return vulnerability_log
   
