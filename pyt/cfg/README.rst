make_cfg is what __main__ calls, it takes the Abstract Syntax Tree, creates an ExprVisitor and return a Control Flow Graph.

Statements can contain expressions, but not 
ExprVisitor inherits from StmtVisitor, which inherits from `ast.NodeVisitor`_ from the standard library. 

https://github.com/python/cpython/blob/f2c1aa1661edb3e14ff8b7b9995f93e303c8acbb/Lib/ast.py#L249-L253

There is a `visit\_` function for almost every AST node type.

We keep track of all the nodes while we visit by adding them to self.nodes, 

The two most illustrative functions are stmt_star_handler

Upon visiting an If statement we will enter visit_If, which will call stmt_star_handler, that returns a namedtuple ControlFlowNode with the first statement, last_statements and break_statements.

In visit_call we will call expr_star_handler on the arguments, that returns a named_tuple with the 

We create the control flow graph of the program we are analyzing. 

These modules mirror the `abstract grammar`_ of Python.

.. _ast.NodeVisitor: https://docs.python.org/3/library/ast.html#ast.NodeVisitor
.. _abstract grammar: https://docs.python.org/3/library/ast.html#abstract-grammar


Dive into the raw ast NodeVisitor code.


Statements can contain expressions, but not the other way around,
so it was natural to have ExprVisitor inherit from StmtVisitor.


TODO: stmt_star_handler and expr_star_handler explanations and walk throughs.


For more information on AST nodes, see the `Green Tree Snakes`_ documentation.

.. _Green Tree Snakes: https://greentreesnakes.readthedocs.io/en/latest/nodes.html
