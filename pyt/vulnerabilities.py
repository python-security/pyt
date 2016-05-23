"""Module for finding vulnerabilities based on a definitions file."""

import os
from collections import namedtuple
import ast
import logging

from cfg import CFG, generate_ast, Node, AssignmentNode
from vulnerability_log import Vulnerability, VulnerabilityLog, SanitisedVulnerability

logger = logging.getLogger(__name__)

Triggers = namedtuple('Triggers', 'sources sinks sanitiser_dict')
Sanitiser = namedtuple('Sanitiser', 'trigger_word cfg_node')
Definitions = namedtuple('Definitions', 'sources sinks')

default_trigger_word_file = os.path.join(os.path.dirname(__file__), 'trigger_definitions', 'flask_trigger_words.pyt')

SANITISER_SEPARATOR = '->'
SOURCES_KEYWORD = 'sources:'
SINKS_KEYWORD = 'sinks:'

class TriggerNode():
    def __init__(self, trigger_word, sanitisers, cfg_node, secondary_nodes=None):
        self.trigger_word = trigger_word
        self.sanitisers = sanitisers
        self.cfg_node = cfg_node
        self.secondary_nodes = secondary_nodes

    def append(self, cfg_node):
        if not cfg_node == self.cfg_node:
            if self.secondary_nodes and cfg_node not in self.secondary_nodes:
                self.secondary_nodes.append(cfg_node)
            elif not self.secondary_nodes:
                self.secondary_nodes = [cfg_node]

def parse_section(iterator):
    """Parse a section of a file. Stops at empty line.

    Args:
        iterator(File): file descriptor pointing at a definition file.

    Returns:
         Iterator of all definitions in the section.
    """
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
    """Parse the file for source and sink definitions.

    Returns:
       A definitions tuple with sources and sinks.
    """
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
    """Identify sources, sinks and sanitisers in a CFG.

    Args:
        cfg(CFG): CFG to find sources, sinks and sanitisers in.
        sources(tuple): list of sources, a source is a (source, sanitiser) tuple.
        sinks(tuple): list of sources, a sink is a (sink, sanitiser) tuple.

    Returns:
        Triggers tuple with sink and source nodes and a sanitiser node dict.
    """
    sources_in_file = find_triggers(cfg, sources)
    sinks_in_file = find_triggers(cfg, sinks)

    find_secondary_sources(cfg, sources_in_file)
       
    sanitiser_node_dict = build_sanitiser_node_dict(cfg, sinks_in_file)
    
    return Triggers(sources_in_file, sinks_in_file, sanitiser_node_dict)

def append_if_reassigned(source, node):
    assign_to_source = source.cfg_node.left_hand_side in node.right_hand_side_variables
    reassign_source = source.cfg_node.left_hand_side in node.left_hand_side and assign_to_source
    node_in_constraint = source.cfg_node in node.new_constraint
        
    if node_in_constraint and assign_to_source or reassign_source:
        if node.line_number:
            logger.debug('adding ' + str(node) + ' to secondary sources ')    
            source.append(node)

def append_if_reassigned_intermediate(source, intermediate, node):
    assign_to_source = intermediate.left_hand_side in node.right_hand_side_variables
    reassign_source = source.cfg_node.left_hand_side in node.left_hand_side and assign_to_source
    node_in_constraint = intermediate in node.new_constraint
        
    if node_in_constraint and assign_to_source or reassign_source:
        if node.line_number:
            logger.debug('adding ' + str(node) + ' to secondary sources ')
            source.append(node)

        
def find_secondary_sources(cfg, sources):
    for node in cfg.nodes:
        if isinstance(node, AssignmentNode):
            for source in sources:
                append_if_reassigned(source, node)
                if source.secondary_nodes:
                    for secondary in source.secondary_nodes:
                        append_if_reassigned_intermediate(source, secondary, node)

def find_triggers(cfg, trigger_words):
    """Find triggers from the trigger_word_list in the cfg.

    Args:
        cfg(CFG): the CFG to find triggers in.
        trigger_word_list(list[string]): list of trigger words to look for.

    Returns:
        List of found TriggerNodes
    """
    l = list()
    for node in cfg.nodes:
        l.extend(iter(label_contains(node, trigger_words)))
    return l
      
def label_contains(node, trigger_words):
    """Determine if node contains any of the trigger_words provided.

    Args:
        node(Node): CFG node to check.
        trigger_words(list[string]): list of trigger words to look for.

    Returns:
        Iterable of TriggerNodes found. Can be multiple because multiple trigger_words can be in one node.
    """
    for trigger_word_tuple in trigger_words:
        if trigger_word_tuple[0] in node.label:
            trigger_word = trigger_word_tuple[0]
            sanitisers = trigger_word_tuple[1]
            yield TriggerNode(trigger_word, sanitisers, node)

def build_sanitiser_node_dict(cfg, sinks_in_file):
    """Build a dict of string -> TriggerNode pairs, where the string is the sanitiser and the TriggerNode is a TriggerNode of the sanitiser.

    Args:
        cfg(CFG): cfg to traverse.
        sinks_in_file(list[TriggerNode]): list of TriggerNodes contains the sinks in the file

    Returns:
        A string -> TriggerNode dict.
    """
    sanitisers = list()
    for sink in sinks_in_file:
        sanitisers.extend(sink.sanitisers)

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
    """Find nodes containing a particular sanitiser.

    Args:
        sanitiser(string): sanitiser to look for.
        sanitisers_in_file(list[Node]): list of CFG nodes with the sanitiser.

    Returns:
        Iterable of sanitiser nodes.
    """
    for sanitiser_tuple  in sanitisers_in_file:
        if sanitiser == sanitiser_tuple.trigger_word:
            yield sanitiser_tuple.cfg_node

def is_sanitized(sink, sanitiser_dict):
    """Check if sink is sanitised by any santiser in the sanitiser_dict.

    Args:
        sink(TriggerNode): TriggerNode of the sink.
        sanitiser_dict(dict): dictionary of sink sanitiser pairs.

    Returns: 
        True of False
    """
    for sanitiser in sink.sanitisers:
        for cfg_node in sanitiser_dict[sanitiser]:
            if cfg_node in sink.cfg_node.new_constraint:
                return True
    return False

def get_sink_args(cfg_node):
    if type(cfg_node) == AssignmentNode:
        return get_sink_args(cfg_node.ast_node.value)
    elif isinstance(cfg_node, Node):
        return get_sink_args(cfg_node.ast_node)
    elif isinstance(cfg_node, ast.Call):
        args = list()

        for arg in cfg_node.args + cfg_node.keywords:
            if isinstance(arg, ast.Name):
                args.append(arg.id)
            elif isinstance(arg, ast.Str):
                args.append(arg.s)
            elif isinstance(arg, ast.Call):
                args.extend(get_sink_args(arg))
            elif isinstance(arg, ast.keyword):
                args.append(arg.value)
            else:
                raise Exception('Unexpected argument type:', type(arg))
        return args
    elif not cfg_node:
        return []
    else:
        raise Exception('Unexpected node type:', type(cfg_node))

            
            
def get_vulnerability(source, sink, triggers):
    """Get vulnerability between source and sink if it exists.

    Uses triggers to find sanitisers

    Args:
        source(TriggerNode): TriggerNode of the source.
        sink(TriggerNode): TriggerNode of the sink.
        triggers(Triggers): Triggers of the CFG.

    Returns:
        A Vulnerability if it exists, else None
    """
    source_in_sink = source.cfg_node in sink.cfg_node.new_constraint

    secondary_in_sink = []
    if source.secondary_nodes:
        secondary_in_sink = [secondary for secondary in source.secondary_nodes if secondary in sink.cfg_node.new_constraint]
    trigger_node_in_sink = source_in_sink or secondary_in_sink
    
    sink_args = get_sink_args(sink.cfg_node)
    source_lhs_in_sink_args = source.cfg_node.left_hand_side in sink_args
    secondary_nodes_in_sink_args = any(True for node in secondary_in_sink if node.left_hand_side in sink_args)
    lhs_in_sink_args = source_lhs_in_sink_args or secondary_nodes_in_sink_args

    logger.debug('Checking for vuln:')
    logger.debug('source ' + str(source.cfg_node.label))
    logger.debug('sink ' + str(sink.cfg_node.label))
                 
    if trigger_node_in_sink and lhs_in_sink_args:
        source_trigger_word = source.trigger_word
        sink_trigger_word = sink.trigger_word
        sink_is_sanitised = is_sanitized(sink, triggers.sanitiser_dict)

        if not sink_is_sanitised :
            return Vulnerability(source.cfg_node, source_trigger_word, sink.cfg_node, sink_trigger_word, source.secondary_nodes)
        elif sink_is_sanitised:
            return SanitisedVulnerability(source.cfg_node, source_trigger_word, sink.cfg_node, sink_trigger_word, sink.sanitisers, source.secondary_nodes)
    return None

def find_vulnerabilities_in_cfg(cfg, vulnerability_log, definitions):
    """Find vulnerabilities in a cfg.

    Args:
        cfg(CFG): The CFG look find vulnerabilities in.
        vulnerabilitiy_log: The log in which to place found vulnerabilities.
        definitions: Source and sink definitions.
    """
    triggers = identify_triggers(cfg, definitions.sources, definitions.sinks)
    for sink in triggers.sinks:
        for source in triggers.sources:
            vulnerability = get_vulnerability(source, sink, triggers)
            if vulnerability:
                vulnerability_log.append(vulnerability)

def find_vulnerabilities(cfg_list, trigger_word_file=default_trigger_word_file):
    """Find vulnerabilities in a list of CFGs from a trigger_word_file.

    Args:
        cfg_list (list): the list of CFGs to scan.
        trigger_word_file (string): file containing trigger words. Defaults to the flask trigger word file.

    Returns:
        A VulnerabilityLog with found vulnerabilities.
    """
    definitions = parse(trigger_word_file)
    
    vulnerability_log = VulnerabilityLog()
    for cfg in cfg_list:
        find_vulnerabilities_in_cfg(cfg, vulnerability_log, definitions)
    return vulnerability_log
   
