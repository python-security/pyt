import ast

from .base_cfg import AssignmentNode, EntryOrExitNode
from .constraint_table import constraint_table
from .lattice import Lattice
from .reaching_definitions import ReachingDefinitionsAnalysis
from .vars_visitor import VarsVisitor


def get_vars(node):
    vv = VarsVisitor()
    if isinstance(node.ast_node, (ast.If, ast.While)):
        vv.visit(node.ast_node.test)
    elif isinstance(node.ast_node, (ast.ClassDef, ast.FunctionDef)):
        return set()
    else:
        try:
            vv.visit(node.ast_node)
        except AttributeError:  # If no ast_node
            vv.result = set()
    vv.result = set(vv.result)

    # Filter out lvars:
    for var in vv.result:
        try:
            if var in node.right_hand_side_variables:
                yield var
        except AttributeError:
            yield var


def get_constraint_nodes(node, lattice):
    for n in lattice.get_elements(constraint_table[node]):
        if n is not node:
            yield n


# TKTK: Clean up use-def too
def build_use_def_chain(cfg_nodes):
    use_def = dict()
    lattice = Lattice(cfg_nodes, ReachingDefinitionsAnalysis)

    for node in cfg_nodes:
        definitions = list()
        for constraint_node in get_constraint_nodes(node, lattice):
            for var in get_vars(node):
                if var in constraint_node.left_hand_side:
                    definitions.append((var, constraint_node))
        use_def[node] = definitions

    return use_def


def get_uses(node):
    if isinstance(node, AssignmentNode):
        # TKTK: Merge in master, then remove this `if`
        result = list()
        if isinstance(node.right_hand_side_variables, str):
            result.append(node.right_hand_side_variables)
        else:
            for var in node.right_hand_side_variables:
                if var not in node.left_hand_side:
                    result.append(var)
        return result
    elif isinstance(node, EntryOrExitNode):
        return []
    else:
        raise


def build_def_use_chain(cfg_nodes):
    def_use = dict()
    lattice = Lattice(cfg_nodes, ReachingDefinitionsAnalysis)

    # For every node
    for node in cfg_nodes:
        # Make an empty list for each def
        if isinstance(node, AssignmentNode):
            def_use[node] = list()
        # Get its uses
        for variable in get_uses(node):
            # Loop through all the nodes before it
            for earlier_node in get_constraint_nodes(node, lattice):
                # and add to the 'uses list' of each earlier node, when applicable
                if variable in earlier_node.left_hand_side:
                    def_use[earlier_node].append(node)

    return def_use
