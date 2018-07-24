import ast
import random
from collections import namedtuple

from ..core.node_types import (
    AssignmentCallNode,
    BBorBInode,
    BreakNode,
    ControlFlowNode,
    RestoreNode
)


CALL_IDENTIFIER = '~'
ConnectStatements = namedtuple(
    'ConnectStatements',
    (
        'first_statement',
        'last_statements',
        'break_statements'
    )
)


def _get_inner_most_function_call(call_node):
    # Loop to inner most function call
    # e.g. return scrypt.inner in `foo = scrypt.outer(scrypt.inner(image_name))`
    old_call_node = None
    while call_node != old_call_node:
        old_call_node = call_node
        if isinstance(call_node, BBorBInode):
            call_node = call_node.inner_most_call
        else:
            try:
                # e.g. save_2_blah, even when there is a save_3_blah
                call_node = call_node.first_node
            except AttributeError:
                # No inner calls
                # Possible improvement: Make new node for RestoreNode's made in process_function
                #                       and make `self.inner_most_call = self`
                # So that we can duck type and not catch an exception when there are no inner calls.
                # This is what we do in BBorBInode
                pass

    return call_node


def _connect_control_flow_node(control_flow_node, next_node):
    """Connect a ControlFlowNode properly to the next_node."""
    for last in control_flow_node.last_nodes:
        if isinstance(next_node, ControlFlowNode):
            last.connect(next_node.test)  # connect to next if test case
        elif isinstance(next_node, AssignmentCallNode):
            call_node = next_node.call_node
            inner_most_call_node = _get_inner_most_function_call(call_node)
            last.connect(inner_most_call_node)
        else:
            last.connect(next_node)


def connect_nodes(nodes):
    """Connect the nodes in a list linearly."""
    for n, next_node in zip(nodes, nodes[1:]):
        if isinstance(n, ControlFlowNode):
            _connect_control_flow_node(n, next_node)
        elif isinstance(next_node, ControlFlowNode):
            n.connect(next_node.test)
        elif isinstance(next_node, RestoreNode):
            continue
        elif CALL_IDENTIFIER in next_node.label:
            continue
        else:
            n.connect(next_node)


def _get_names(node, result):
    """Recursively finds all names."""
    if isinstance(node, ast.Name):
        return node.id + result
    elif isinstance(node, ast.Subscript):
        return result
    elif isinstance(node, ast.Starred):
        return _get_names(node.value, result)
    else:
        return _get_names(node.value, result + '.' + node.attr)


def extract_left_hand_side(target):
    """Extract the left hand side variable from a target.

    Removes list indexes, stars and other left hand side elements.
    """
    left_hand_side = _get_names(target, '')

    left_hand_side.replace('*', '')
    if '[' in left_hand_side:
        index = left_hand_side.index('[')
        left_hand_side = target[:index]

    return left_hand_side


def get_first_node(
    node,
    node_not_to_step_past
):
    """
        This is a super hacky way of getting the first node after a statement.
        We do this because we visit a statement and keep on visiting and get something in return that is rarely the first node.
        So we loop and loop backwards until we hit the statement or there is nothing to step back to.
    """
    ingoing = None
    i = 0
    current_node = node
    while current_node.ingoing:
        # This is used because there may be multiple ingoing and loop will cause an infinite loop if we did [0]
        i = random.randrange(len(current_node.ingoing))
        # e.g. We don't want to step past the Except of an Except basic block
        if current_node.ingoing[i] == node_not_to_step_past:
            break
        ingoing = current_node.ingoing
        current_node = current_node.ingoing[i]
    if ingoing:
        return ingoing[i]
    return current_node


def get_first_statement(node_or_tuple):
    """Find the first statement of the provided object.

    Returns:
        The first element in the tuple if it is a tuple.
        The node if it is a node.
    """
    if isinstance(node_or_tuple, tuple):
        return node_or_tuple[0]
    else:
        return node_or_tuple


def get_last_statements(cfg_statements):
    """Retrieve the last statements from a cfg_statements list."""
    if isinstance(cfg_statements[-1], ControlFlowNode):
        return cfg_statements[-1].last_nodes
    else:
        return [cfg_statements[-1]]


def remove_breaks(last_statements):
    """Remove all break statements in last_statements."""
    return [n for n in last_statements if not isinstance(n, BreakNode)]
