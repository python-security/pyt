from collections import namedtuple

from ..core.node_types import (
    ConnectToExitNode,
    ControlFlowNode,
    IfExpNode
)


CALL_IDENTIFIER = '~'
BUILTINS = (
    'get',
    'Flask',
    'run',
    'replace',
    'read',
    'set_cookie',
    'make_response',
    'SQLAlchemy',
    'Column',
    'execute',
    'sessionmaker',
    'Session',
    'filter',
    'call',
    'render_template',
    'redirect',
    'url_for',
    'flash',
    'jsonify'
)
SavedVariable = namedtuple(
    'SavedVariable',
    (
        'LHS',
        'RHS'
    )
)

# Mainly used in expr_star_handler
# Or after stmt_star_handler returns an IgnoredNode, like in visit_Call and visit_Try
ConnectExpressions = namedtuple(
    'ConnectExpressions',
    (
        'first_expression',
        'last_expressions'
    )
)


def return_connection_handler(nodes, exit_node):
    """Connect all return statements to the Exit node."""
    for function_body_node in nodes:
        if isinstance(function_body_node, ConnectToExitNode):
            if exit_node not in function_body_node.outgoing:
                function_body_node.connect(exit_node)


def get_last_expressions(expressions):
    """Retrieve the last expressions from a list of expressions."""
    # if isinstance(expressions[-1], IfExpNode):
    #     raise
    #     return expressions[-1].last_nodes
    # Combine me with get_last_statements
    # Combine me with get_last_statements
    # Combine me with get_last_statements
    # Combine me with get_last_statements
    if isinstance(expressions[-1], ControlFlowNode):
        return expressions[-1].last_nodes
    else:
        return [expressions[-1]]



def _connect_control_flow_node(control_flow_node, next_node):
    """Connect a ControlFlowNode properly to the next_node."""
    for last in control_flow_node.last_nodes:
        if isinstance(next_node, ControlFlowNode):
            last.connect(next_node.test)  # connect to next if test case
        else:
            last.connect(next_node)


def connect_nodes(nodes):
    """Connect the nodes in a list linearly."""
    for n, next_node in zip(nodes, nodes[1:]):
        if isinstance(n, ControlFlowNode):
            print('_connect_control_flow_node')
            _connect_control_flow_node(n, next_node)
        elif isinstance(next_node, ControlFlowNode):
            print('n.connect(next_node.test)')
            n.connect(next_node.test)
        # elif isinstance(next_node, RestoreNode):
        #     print('72')
        #     raise
        #     # I should connect, not continue
        #     continue
        # elif CALL_IDENTIFIER in next_node.label:
        #     print('hi')
        #     continue
        else:
            print('n.connect(next_node)')
            n.connect(next_node)
