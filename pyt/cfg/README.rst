These modules mirror the `abstract grammar`_ of Python.

.. _abstract grammar: https://docs.python.org/3/library/ast.html#abstract-grammar


Dive into the raw ast NodeVisitor code.


Statements can contain expressions, but not the other way around,
so it was natural to have ExprVisitor inherit from StmtVisitor.


TODO: stmt_star_handler and expr_star_handler explanations and walk throughs.


For more information on AST nodes, see the `Green Tree Snakes`_ documentation.

.. _Green Tree Snakes: https://greentreesnakes.readthedocs.io/en/latest/nodes.html
