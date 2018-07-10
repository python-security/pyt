from collections import namedtuple

from ..core.node_types import (
    ConnectToExitNode,
    ControlFlowExpr
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

class ConnectedExpressions():
    """Only created in expr_star_handler."""
    def __init__(
        self,
        first_expression=None,
        all_expressions=[],
        last_expressions=[],
        variables=[],
        visual_variables=[]
    ):
        """
        Args:
            first_expression(node):
                Used to connect the previous node to the first expression.
            all_expressions(list):
                Useful for e.g. visit_BoolOp where all expressions
                can be returned when the operand is `or`.
            last_expressions(list):
                Useful for e.g. visit_BoolOp where only the last expression
                can be returned when the operand is `and`.
            variables(list):
                Used to return e.g. [foo, bar] for `foo or bar`.
            visual_variables(list):
                Useful for e.g. hard-coded strings that are otherwise ignored.
                Also for returning string representations of expressions
                e.g. `foo or bar`
        """
        self.first_expression = first_expression
        self.all_expressions = all_expressions
        self.last_expressions = last_expressions
        self.variables = variables
        self.visual_variables = visual_variables



def return_connection_handler(nodes, exit_node):
    """Connect all return statements to the Exit node."""
    for function_body_node in nodes:
        if isinstance(function_body_node, ConnectToExitNode):
            if exit_node not in function_body_node.outgoing:
                function_body_node.connect(exit_node)


def get_last_expressions(expressions):
    """Retrieve the last expressions from a list of expressions."""
    if isinstance(expressions[-1], ControlFlowExpr):
        last_expressions = list()
        for expr in expressions[-1].last_expressions:
            last_expressions.extend(get_last_expressions([expr]))
        return last_expressions
    else:
        return [expressions[-1]]


def _connect_control_flow_node(control_flow_node, next_node):
    """Connect a ControlFlowExpr properly to the next_node."""
    for last in control_flow_node.last_expressions:
        if isinstance(next_node, ControlFlowExpr):
            last.connect(next_node.test)  # connect to next if test case
        else:
            last.connect(next_node)


def connect_expressions(nodes):
    """Connect the nodes in a list linearly."""
    for n, next_node in zip(nodes, nodes[1:]):
        if isinstance(n, ControlFlowExpr):
            print('_connect_control_flow_node')
            # todo
            raise
            _connect_control_flow_node(n, next_node)
        # e.g. (request.args.get('The') or 'French' and request.args.get('Laundry'))
        elif isinstance(next_node, ControlFlowExpr):
            # import ipdb
            # ipdb.set_trace()
            # print('n.connect(next_node.test)')
            print('connecting all of n with all of last_expressions')
            # todo: decide this
            raise
            for expr in next_node.last_expressions:
                n.connect(expr)
            # or this
            # n.connect(next_node.test)
        else:
            print('n.connect(next_node)')
            n.connect(next_node)
