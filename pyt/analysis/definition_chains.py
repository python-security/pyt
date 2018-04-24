from collections import defaultdict

from .constraint_table import constraint_table
from ..core.node_types import AssignmentNode


def get_constraint_nodes(
    node,
    lattice
):
    for n in lattice.get_elements(constraint_table[node]):
        if n is not node:
            yield n


def build_def_use_chain(
    cfg_nodes,
    lattice
):
    def_use = defaultdict(list)
    # For every node
    for node in cfg_nodes:
        # That's a definition
        if isinstance(node, AssignmentNode):
            # Get the uses
            for variable in node.right_hand_side_variables:
                # Loop through most of the nodes before it
                for earlier_node in get_constraint_nodes(node, lattice):
                    # and add them to the 'uses list' of each earlier node, when applicable
                    # 'earlier node' here being a simplification
                    if variable in earlier_node.left_hand_side:
                        def_use[earlier_node].append(node)
    return def_use
