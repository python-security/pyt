"""Module for finding vulnerabilities based on a definitions file."""

import ast
from collections import namedtuple

from .base_cfg import (
    AssignmentCallNode,
    AssignmentNode,
    BBorBInode,
    RestoreNode,
    TaintedNode
)
from .lattice import Lattice
from .right_hand_side_visitor import RHSVisitor
from .trigger_definitions_parser import default_trigger_word_file, parse
from .vars_visitor import VarsVisitor
from .vulnerability_log import (
    SanitisedVulnerability,
    UnknownVulnerability,
    Vulnerability,
    VulnerabilityLog
)


Sanitiser = namedtuple('Sanitiser', 'trigger_word cfg_node')
Triggers = namedtuple('Triggers', 'sources sinks sanitiser_dict')


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

    def __repr__(self):
        output = 'TriggerNode('

        if self.trigger_word:
            output = output + 'trigger_word is ' + str(self.trigger_word) + ', '

        return (
            output +
            'sanitisers are ' + str(self.sanitisers) + ', '
            'cfg_node is ' + str(self.cfg_node) + ')\n'
        )


def identify_triggers(cfg, sources, sinks, lattice):
    """Identify sources, sinks and sanitisers in a CFG.

    Args:
        cfg(CFG): CFG to find sources, sinks and sanitisers in.
        sources(tuple): list of sources,
        a source is a (source, sanitiser) tuple.
        sinks(tuple): list of sources, a sink is a (sink, sanitiser) tuple.

    Returns:
        Triggers tuple with sink and source nodes and a sanitiser node dict.
    """
    assignment_nodes = filter_cfg_nodes(cfg, AssignmentNode)
    tainted_nodes = filter_cfg_nodes(cfg, TaintedNode)
    tainted_trigger_nodes = [TriggerNode('Framework function URL parameter', None,
                                         node) for node in tainted_nodes]
    sources_in_file = find_triggers(assignment_nodes, sources)
    sources_in_file.extend(tainted_trigger_nodes)

    find_secondary_sources(assignment_nodes, sources_in_file, lattice)

    sinks_in_file = find_triggers(cfg.nodes, sinks)

    sanitiser_node_dict = build_sanitiser_node_dict(cfg, sinks_in_file)

    return Triggers(sources_in_file, sinks_in_file, sanitiser_node_dict)


def filter_cfg_nodes(cfg, cfg_node_type):
    return [node for node in cfg.nodes if isinstance(node, cfg_node_type)]


def find_secondary_sources(assignment_nodes, sources, lattice):
    """
        Sets the secondary_nodes attribute of each source in the sources list.

        Args:
            assignment_nodes([AssignmentNode])
            sources([tuple])
    """
    for source in sources:
        source.secondary_nodes = find_assignments(assignment_nodes, source, lattice)


def find_assignments(assignment_nodes, source, lattice):
    old = list()

    # added in order to propagate reassignments of the source node
    new = [source.cfg_node]

    update_assignments(new, assignment_nodes, source.cfg_node, lattice)
    while new != old:
        old = new
        update_assignments(new, assignment_nodes, source.cfg_node, lattice)
    new.remove(source.cfg_node)  # remove source node from result
    return new


def update_assignments(assignment_list, assignment_nodes, source, lattice):
    for node in assignment_nodes:
        for other in assignment_list:
            if node not in assignment_list:
                append_if_reassigned(assignment_list, other, node, lattice)


def append_if_reassigned(assignment_list, secondary, node, lattice):
    try:
        reassigned = False
        # vv_result is necessary to know `image_name = image_name.replace('..', '')` is a reassignment.
        if isinstance(node, AssignmentCallNode) and secondary.left_hand_side in node.vv_result:
            reassigned = True
        elif secondary.left_hand_side in node.right_hand_side_variables:
            reassigned = True
        elif secondary.left_hand_side == node.left_hand_side:
            reassigned = True
        if reassigned and lattice.in_constraint(secondary, node):
            assignment_list.append(node)
    except AttributeError:
        print(secondary)
        print('EXCEPT' + secondary)
        exit(0)


def find_triggers(nodes, trigger_words):
    """Find triggers from the trigger_word_list in the nodes.

    Args:
        nodes(list[Node]): the nodes to find triggers in.
        trigger_word_list(list[string]): list of trigger words to look for.

    Returns:
        List of found TriggerNodes
    """
    trigger_nodes = list()
    for node in nodes:
        trigger_nodes.extend(iter(label_contains(node, trigger_words)))
    return trigger_nodes


def label_contains(node, trigger_words):
    """Determine if node contains any of the trigger_words provided.

    Args:
        node(Node): CFG node to check.
        trigger_words(list[string]): list of trigger words to look for.

    Returns:
        Iterable of TriggerNodes found. Can be multiple because multiple
        trigger_words can be in one node.
    """
    for trigger_word_tuple in trigger_words:
        if trigger_word_tuple[0] in node.label:
            trigger_word = trigger_word_tuple[0]
            sanitisers = trigger_word_tuple[1]
            yield TriggerNode(trigger_word, sanitisers, node)


def build_sanitiser_node_dict(cfg, sinks_in_file):
    """Build a dict of string -> TriggerNode pairs, where the string
       is the sanitiser and the TriggerNode is a TriggerNode of the sanitiser.

    Args:
        cfg(CFG): cfg to traverse.
        sinks_in_file(list[TriggerNode]): list of TriggerNodes containing
                                          the sinks in the file.

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
        sanitiser_node_dict[sanitiser] = list(find_sanitiser_nodes(sanitiser,
                                                                   sanitisers_in_file))
    return sanitiser_node_dict


def find_sanitiser_nodes(sanitiser, sanitisers_in_file):
    """Find nodes containing a particular sanitiser.

    Args:
        sanitiser(string): sanitiser to look for.
        sanitisers_in_file(list[Node]): list of CFG nodes with the sanitiser.

    Returns:
        Iterable of sanitiser nodes.
    """
    for sanitiser_tuple in sanitisers_in_file:
        if sanitiser == sanitiser_tuple.trigger_word:
            yield sanitiser_tuple.cfg_node


def is_sanitised(sink, sanitiser_dict, lattice):
    """Check if sink is sanitised by any santiser in the sanitiser_dict.

    Args:
        sink(TriggerNode): TriggerNode of the sink.
        sanitiser_dict(dict): dictionary of sink sanitiser pairs.

    Returns:
        True or False
    """
    for sanitiser in sink.sanitisers:
        for cfg_node in sanitiser_dict[sanitiser]:
            if lattice.in_constraint(cfg_node, sink.cfg_node):
                return True
    return False


class SinkArgsError(Exception):
    pass


def is_unknown(trimmed_reassignment_nodes, blackbox_assignments):
    """Check if vulnerability is unknown by seeing if a blackbox
        assignment is in trimmed_reassignment_nodes.

    Args:
        trimmed_reassignment_nodes(list[AssignmentNode]): reassignments leading to the vulnerability.
        blackbox_assignments(set[AssignmentNode]): set of blackbox assignments.

    Returns:
        AssignmentNode or None
    """
    for node in trimmed_reassignment_nodes:
        if node in blackbox_assignments:
            return node
    return None


def get_sink_args(cfg_node):
    if isinstance(cfg_node.ast_node, ast.Call):
        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(cfg_node.ast_node)
        return rhs_visitor.result
    elif isinstance(cfg_node.ast_node, ast.Assign):
        return cfg_node.right_hand_side_variables

    vv = VarsVisitor()
    other_results = list()
    if isinstance(cfg_node, BBorBInode):
        other_results = cfg_node.args
    else:
        vv.visit(cfg_node.ast_node)

    return vv.result + other_results


def get_vulnerability(source,
                      sink,
                      triggers,
                      lattice,
                      trim_reassigned_in,
                      blackbox_assignments):
    """Get vulnerability between source and sink if it exists.

    Uses triggers to find sanitisers.

    Args:
        source(TriggerNode): TriggerNode of the source.
        sink(TriggerNode): TriggerNode of the sink.
        triggers(Triggers): Triggers of the CFG.
        lattice(Lattice): The lattice we're analysing.
        trim_reassigned_in(bool): Whether or not the trim option is set.
        blackbox_assignments(set[AssignmentNode]): used in is_unknown.

    Returns:
        A Vulnerability if it exists, else None
    """
    source_in_sink = lattice.in_constraint(source.cfg_node, sink.cfg_node)

    secondary_nodes_in_sink = list()
    if source.secondary_nodes:
        secondary_nodes_in_sink = [secondary for secondary in source.secondary_nodes
                                   if lattice.in_constraint(secondary,
                                                            sink.cfg_node)]

    trigger_node_in_sink = source_in_sink or secondary_nodes_in_sink

    sink_args = get_sink_args(sink.cfg_node)

    secondary_node_in_sink_args = None
    if sink_args:
        for node in secondary_nodes_in_sink:
            if node.left_hand_side in sink_args:
                secondary_node_in_sink_args = node

    trimmed_reassignment_nodes = list()
    if secondary_node_in_sink_args:
        trimmed_reassignment_nodes.append(secondary_node_in_sink_args)
        node_in_the_vulnerability_chain = secondary_node_in_sink_args
        # Here is where we do backwards slicing to traceback which nodes led to the vulnerability
        for secondary in reversed(source.secondary_nodes):
            if lattice.in_constraint(secondary, sink.cfg_node):
                if secondary.left_hand_side in node_in_the_vulnerability_chain.right_hand_side_variables:
                    node_in_the_vulnerability_chain = secondary
                    trimmed_reassignment_nodes.insert(0, node_in_the_vulnerability_chain)

    source_lhs_in_sink_args = source.cfg_node.left_hand_side in sink_args\
                              if sink_args else None

    lhs_in_sink_args = source_lhs_in_sink_args or secondary_node_in_sink_args

    if trigger_node_in_sink and lhs_in_sink_args:
        source_trigger_word = source.trigger_word
        sink_trigger_word = sink.trigger_word
        sink_is_sanitised = is_sanitised(
            sink,
            triggers.sanitiser_dict,
            lattice
        )
        blackbox_assignment_in_chain = is_unknown(
            trimmed_reassignment_nodes,
            blackbox_assignments
        )
        reassignment_nodes = source.secondary_nodes
        if trim_reassigned_in:
            reassignment_nodes = trimmed_reassignment_nodes
        if sink_is_sanitised:
            return SanitisedVulnerability(
                source.cfg_node, source_trigger_word,
                sink.cfg_node, sink_trigger_word,
                sink.sanitisers,
                reassignment_nodes
            )
        elif blackbox_assignment_in_chain:
            return UnknownVulnerability(
                source.cfg_node, source_trigger_word,
                sink.cfg_node, sink_trigger_word,
                blackbox_assignment_in_chain,
                reassignment_nodes
            )
        else:
            return Vulnerability(
                source.cfg_node, source_trigger_word,
                sink.cfg_node, sink_trigger_word,
                reassignment_nodes
            )
    return None


def find_vulnerabilities_in_cfg(cfg, vulnerability_log, definitions, lattice, trim_reassigned_in):
    """Find vulnerabilities in a cfg.

    Args:
        cfg(CFG): The CFG to find vulnerabilities in.
        vulnerability_log(vulnerability_log.VulnerabilityLog): The log in which to place found vulnerabilities.
        definitions(trigger_definitions_parser.Definitions): Source and sink definitions.
        lattice(Lattice): The lattice we're analysing.
        trim_reassigned_in(bool): Whether or not the trim option is set.
    """
    triggers = identify_triggers(cfg, definitions.sources, definitions.sinks, lattice)
    for sink in triggers.sinks:
        for source in triggers.sources:
            vulnerability = get_vulnerability(
                source,
                sink,
                triggers,
                lattice,
                trim_reassigned_in,
                cfg.blackbox_assignments
            )
            if vulnerability:
                vulnerability_log.append(vulnerability)


def find_vulnerabilities(cfg_list,
                         analysis_type,
                         trim_reassigned_in=False,
                         trigger_word_file=default_trigger_word_file):
    """Find vulnerabilities in a list of CFGs from a trigger_word_file.

    Args:
        cfg_list (list[CFG]): the list of CFGs to scan.
        trigger_word_file (string): file containing trigger words.
        Defaults to the flask trigger word file.

    Returns:
        A VulnerabilityLog with found vulnerabilities.
    """
    definitions = parse(trigger_word_file)
    vulnerability_log = VulnerabilityLog()

    for cfg in cfg_list:
        find_vulnerabilities_in_cfg(
            cfg,
            vulnerability_log,
            definitions,
            Lattice(cfg.nodes, analysis_type),
            trim_reassigned_in
        )
    return vulnerability_log
