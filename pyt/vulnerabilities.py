"""Module for finding vulnerabilities based on a definitions file."""

import ast
import json
from collections import namedtuple

from .argument_helpers import UImode
from .definition_chains import build_def_use_chain
from .lattice import Lattice
from .node_types import (
    AssignmentNode,
    BBorBInode,
    IfNode,
    TaintedNode
)
from .right_hand_side_visitor import RHSVisitor
from .trigger_definitions_parser import parse
from .vars_visitor import VarsVisitor
from .vulnerability_helper import (
    vuln_factory,
    VulnerabilityType
)


Sanitiser = namedtuple(
    'Sanitiser',
    (
        'trigger_word',
        'cfg_node'
    )
)
Triggers = namedtuple(
    'Triggers',
    (
        'sources',
        'sinks',
        'sanitiser_dict'
    )
)


class TriggerNode():
    def __init__(self, trigger_word, sanitisers, cfg_node, secondary_nodes=[]):
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
            output = '{} trigger_word is {}, '.format(
                output,
                self.trigger_word
            )

        return (
            output +
            'sanitisers are {}, '.format(self.sanitisers) +
            'cfg_node is {})\n'.format(self.cfg_node)
        )


def identify_triggers(
    cfg,
    sources,
    sinks,
    lattice
):
    """Identify sources, sinks and sanitisers in a CFG.

    Args:
        cfg(CFG): CFG to find sources, sinks and sanitisers in.
        sources(tuple): list of sources, a source is a (source, sanitiser) tuple.
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


def filter_cfg_nodes(
    cfg,
    cfg_node_type
):
    return [node for node in cfg.nodes if isinstance(node, cfg_node_type)]


def find_secondary_sources(
    assignment_nodes,
    sources,
    lattice
):
    """
        Sets the secondary_nodes attribute of each source in the sources list.

        Args:
            assignment_nodes([AssignmentNode])
            sources([tuple])
            lattice(Lattice): the lattice we're analysing.
    """
    for source in sources:
        source.secondary_nodes = find_assignments(assignment_nodes, source, lattice)


def find_assignments(
    assignment_nodes,
    source,
    lattice
):
    old = list()
    # propagate reassignments of the source node
    new = [source.cfg_node]

    while new != old:
        update_assignments(new, assignment_nodes, source.cfg_node, lattice)
        old = new

    # remove source node from result
    del new[0]

    return new


def update_assignments(
    assignment_list,
    assignment_nodes,
    source,
    lattice
):
    for node in assignment_nodes:
        for other in assignment_list:
            if node not in assignment_list and lattice.in_constraint(other, node):
                append_node_if_reassigned(assignment_list, other, node)


def append_node_if_reassigned(
    assignment_list,
    secondary,
    node
):
    if (
        secondary.left_hand_side in node.right_hand_side_variables or
        secondary.left_hand_side == node.left_hand_side
    ):
        assignment_list.append(node)


def find_triggers(
    nodes,
    trigger_words
):
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


def label_contains(
    node,
    trigger_words
):
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


def build_sanitiser_node_dict(
    cfg,
    sinks_in_file
):
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
        sanitiser_node_dict[sanitiser] = list(find_sanitiser_nodes(
            sanitiser,
            sanitisers_in_file
        ))
    return sanitiser_node_dict


def find_sanitiser_nodes(
    sanitiser,
    sanitisers_in_file
):
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


def get_sink_args(cfg_node):
    if isinstance(cfg_node.ast_node, ast.Call):
        rhs_visitor = RHSVisitor()
        rhs_visitor.visit(cfg_node.ast_node)
        return rhs_visitor.result
    elif isinstance(cfg_node.ast_node, ast.Assign):
        return cfg_node.right_hand_side_variables
    elif isinstance(cfg_node, BBorBInode):
        return cfg_node.args
    else:
        vv = VarsVisitor()
        vv.visit(cfg_node.ast_node)
        return vv.result


def get_vulnerability_chains(
    current_node,
    sink,
    def_use,
    chain=[]
):
    """Traverses the def-use graph to find all paths from source to sink that cause a vulnerability.

    Args:
        current_node()
        sink()
        def_use(dict):
        chain(list(Node)): A path of nodes between source and sink.
    """
    for use in def_use[current_node]:
        if use == sink:
            yield chain
        else:
            vuln_chain = list(chain)
            vuln_chain.append(use)
            yield from get_vulnerability_chains(
                use,
                sink,
                def_use,
                vuln_chain
            )


def how_vulnerable(
    chain,
    blackbox_mapping,
    sanitiser_nodes,
    potential_sanitiser,
    blackbox_assignments,
    ui_mode,
    vuln_deets
):
    """Iterates through the chain of nodes and checks the blackbox nodes against the blackbox mapping and sanitiser dictionary.

    Note: potential_sanitiser is the only hack here, it is because we do not take p-use's into account yet.
    e.g. we can only say potentially instead of definitely sanitised in the path_traversal_sanitised_2.py test.

    Args:
        chain(list(Node)): A path of nodes between source and sink.
        blackbox_mapping(dict): A map of blackbox functions containing whether or not they propagate taint.
        sanitiser_nodes(set): A set of nodes that are sanitisers for the sink.
        potential_sanitiser(Node): An if or elif node that can potentially cause sanitisation.
        blackbox_assignments(set[AssignmentNode]): set of blackbox assignments, includes the ReturnNode's of BBorBInode's.
        ui_mode(UImode): determines if we interact with the user when we don't already have a blackbox mapping available.
        vuln_deets(dict): vulnerability details.

    Returns:
        A VulnerabilityType depending on how vulnerable the chain is.
    """
    for i, current_node in enumerate(chain):
        if current_node in sanitiser_nodes:
            vuln_deets['sanitiser'] = current_node
            vuln_deets['confident'] = True
            return VulnerabilityType.SANITISED

        if isinstance(current_node, BBorBInode):
            if current_node.func_name in blackbox_mapping['propagates']:
                continue
            elif current_node.func_name in blackbox_mapping['does_not_propagate']:
                return VulnerabilityType.FALSE
            elif ui_mode == UImode.INTERACTIVE:
                user_says = input(
                    'Is the return value of {} with tainted argument "{}" vulnerable? (Y/n)'.format(
                        current_node.label,
                        chain[i - 1].left_hand_side
                    )
                ).lower()
                if user_says.startswith('n'):
                    blackbox_mapping['does_not_propagate'].append(current_node.func_name)
                    return VulnerabilityType.FALSE
                blackbox_mapping['propagates'].append(current_node.func_name)
            else:
                vuln_deets['unknown_assignment'] = current_node
                return VulnerabilityType.UNKNOWN

    if potential_sanitiser:
        vuln_deets['sanitiser'] = potential_sanitiser
        vuln_deets['confident'] = False
        return VulnerabilityType.SANITISED

    return VulnerabilityType.TRUE


def get_tainted_node_in_sink_args(
    sink_args,
    nodes_in_constaint
):
    if not sink_args:
        return None
    # Starts with the node closest to the sink
    for node in nodes_in_constaint:
        if node.left_hand_side in sink_args:
            return node


def get_vulnerability(
    source,
    sink,
    triggers,
    lattice,
    cfg,
    ui_mode,
    blackbox_mapping
):
    """Get vulnerability between source and sink if it exists.

    Uses triggers to find sanitisers.

    Note: When a secondary node is in_constraint with the sink
              but not the source, the secondary is a save_N_LHS
              node made in process_function in expr_visitor.

    Args:
        source(TriggerNode): TriggerNode of the source.
        sink(TriggerNode): TriggerNode of the sink.
        triggers(Triggers): Triggers of the CFG.
        lattice(Lattice): the lattice we're analysing.
        cfg(CFG): .blackbox_assignments used in is_unknown, .nodes used in build_def_use_chain
        ui_mode(UImode): determines if we interact with the user or trim the nodes in the output, if at all.
        blackbox_mapping(dict): A map of blackbox functions containing whether or not they propagate taint.

    Returns:
        A Vulnerability if it exists, else None
    """
    nodes_in_constaint = [secondary for secondary in reversed(source.secondary_nodes)
                          if lattice.in_constraint(secondary,
                                                   sink.cfg_node)]
    nodes_in_constaint.append(source.cfg_node)

    sink_args = get_sink_args(sink.cfg_node)
    tainted_node_in_sink_arg = get_tainted_node_in_sink_args(
        sink_args,
        nodes_in_constaint
    )

    if tainted_node_in_sink_arg:
        vuln_deets = {
            'source': source.cfg_node,
            'source_trigger_word': source.trigger_word,
            'sink': sink.cfg_node,
            'sink_trigger_word': sink.trigger_word,
            'reassignment_nodes': source.secondary_nodes
        }

        sanitiser_nodes = set()
        potential_sanitiser = None
        if sink.sanitisers:
            for sanitiser in sink.sanitisers:
                for cfg_node in triggers.sanitiser_dict[sanitiser]:
                    if isinstance(cfg_node, AssignmentNode):
                        sanitiser_nodes.add(cfg_node)
                    elif isinstance(cfg_node, IfNode):
                        potential_sanitiser = cfg_node

        def_use = build_def_use_chain(cfg.nodes)
        for chain in get_vulnerability_chains(
            source.cfg_node,
            sink.cfg_node,
            def_use
        ):
            vulnerability_type = how_vulnerable(
                chain,
                blackbox_mapping,
                sanitiser_nodes,
                potential_sanitiser,
                cfg.blackbox_assignments,
                ui_mode,
                vuln_deets
            )
            if vulnerability_type == VulnerabilityType.FALSE:
                continue

            if ui_mode != UImode.NORMAL:
                vuln_deets['reassignment_nodes'] = chain

            return vuln_factory(vulnerability_type)(**vuln_deets)

    return None


def find_vulnerabilities_in_cfg(
    cfg,
    definitions,
    lattice,
    ui_mode,
    blackbox_mapping,
    vulnerabilities_list
):
    """Find vulnerabilities in a cfg.

    Args:
        cfg(CFG): The CFG to find vulnerabilities in.
        definitions(trigger_definitions_parser.Definitions): Source and sink definitions.
        lattice(Lattice): the lattice we're analysing.
        ui_mode(UImode): determines if we interact with the user or trim the nodes in the output, if at all.
        blackbox_mapping(dict): A map of blackbox functions containing whether or not they propagate taint.
        vulnerabilities_list(list): That we append to when we find vulnerabilities.
    """
    triggers = identify_triggers(
        cfg,
        definitions.sources,
        definitions.sinks,
        lattice
    )
    for sink in triggers.sinks:
        for source in triggers.sources:
            vulnerability = get_vulnerability(
                source,
                sink,
                triggers,
                lattice,
                cfg,
                ui_mode,
                blackbox_mapping
            )
            if vulnerability:
                vulnerabilities_list.append(vulnerability)


def find_vulnerabilities(
    cfg_list,
    analysis_type,
    ui_mode,
    vulnerability_files
):
    """Find vulnerabilities in a list of CFGs from a trigger_word_file.

    Args:
        cfg_list(list[CFG]): the list of CFGs to scan.
        analysis_type(AnalysisBase): analysis object used to create lattice.
        ui_mode(UImode): determines if we interact with the user or trim the nodes in the output, if at all.
        vulnerability_files(VulnerabilityFiles): contains trigger words and blackbox_mapping files

    Returns:
        A list of vulnerabilities.
    """
    vulnerabilities = list()
    definitions = parse(vulnerability_files.triggers)

    with open(vulnerability_files.blackbox_mapping) as infile:
        blackbox_mapping = json.load(infile)
    for cfg in cfg_list:
        find_vulnerabilities_in_cfg(
            cfg,
            definitions,
            Lattice(cfg.nodes, analysis_type),
            ui_mode,
            blackbox_mapping,
            vulnerabilities
        )
    with open(vulnerability_files.blackbox_mapping, 'w') as outfile:
        json.dump(blackbox_mapping, outfile, indent=4)

    return vulnerabilities
