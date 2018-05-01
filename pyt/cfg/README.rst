make_cfg is what __main__ calls, it takes the Abstract Syntax Tree, creates an ExprVisitor and return a Control Flow Graph.

Statements can contain expressions, but not the other way around. This is why ExprVisitor inherits from StmtVisitor, (which inherits from `ast.NodeVisitor`_ from the standard library.)


.. code-block:: python

  def visit(self, node):
    """Visit a node."""
    method = 'visit_' + node.__class__.__name__
    visitor = getattr(self, method, self.generic_visit)
    return visitor(node)


There is a `visit\_` function for almost every AST node type.

We keep track of all the nodes while we visit by adding them to self.nodes, connecting them via `ingoing` and `outgoing` node attributes.

The two most illustrative functions are stmt_star_handler and expr_star_handler.

Upon visiting an If statement we will enter visit_If, which will call stmt_star_handler, that returns a namedtuple ControlFlowNode with the first statement, last_statements and break_statements.

.. code-block:: python

  def visit_If(self, node):
      test = self.append_node(IfNode(
          node.test,
          node,
          path=self.filenames[-1]
      ))

      body_connect_stmts = self.stmt_star_handler(node.body)
      if isinstance(body_connect_stmts, IgnoredNode):
          body_connect_stmts = ConnectStatements(
              first_statement=test,
              last_statements=[],
              break_statements=[]
          )
      test.connect(body_connect_stmts.first_statement)

      if node.orelse:
          orelse_last_nodes = self.handle_or_else(node.orelse, test)
          body_connect_stmts.last_statements.extend(orelse_last_nodes)
      else:
          body_connect_stmts.last_statements.append(test)  # if there is no orelse, test needs an edge to the next_node

      last_statements = remove_breaks(body_connect_stmts.last_statements)

      return ControlFlowNode(
          test,
          last_statements,
          break_statements=body_connect_stmts.break_statements
      )


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
