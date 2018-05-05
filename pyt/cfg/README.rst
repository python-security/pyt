`make_cfg`_ is what `__main__.py`_ calls, it takes the `Abstract Syntax Tree`_, creates an `ExprVisitor`_ and returns a `Control Flow Graph`_.

.. _make_cfg: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/make_cfg.py#L22-L38
.. _\_\_main\_\_.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/__main__.py#L33-L106
.. _Abstract Syntax Tree: https://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _Control Flow Graph: https://en.wikipedia.org/wiki/Control_flow_graph

`stmt_visitor.py`_ and `expr_visitor.py`_ mirror the `abstract grammar`_ of Python. Statements can contain expressions, but not the other way around. This is why `ExprVisitor`_ inherits from `StmtVisitor`_, which inherits from `ast.NodeVisitor`_; from the standard library.

.. _StmtVisitor: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/stmt_visitor.py#L55
.. _ExprVisitor: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/expr_visitor.py#L33

This is how `ast.NodeVisitor`_ works:

.. code-block:: python

  def visit(self, node):
    """Visit a node."""
    method = 'visit_' + node.__class__.__name__
    visitor = getattr(self, method, self.generic_visit)
    return visitor(node)


So as you'll see, there is a `visit\_` function for almost every AST node type. We keep track of all the nodes while we visit by adding them to self.nodes, connecting them via `ingoing and outgoing node attributes`_.

.. _ingoing and outgoing node attributes: https://github.com/python-security/pyt/blob/re_organize_code/pyt/core/node_types.py#L27-L48

The two most illustrative functions are `stmt_star_handler`_ and expr_star_handler. expr_star_handler has not been merged to master so let's talk about `stmt_star_handler`_.


Handling an if: statement 
=========================

Example code

.. code-block:: python

  if some_condition:
      x = 5

This is the relevant part of the `abstract grammar`_

.. code-block:: python

  If(expr test, stmt* body, stmt* orelse)
  # Note: stmt* means any number of statements. 


Upon visiting an if: statement we will enter `visit_If`_ in `stmt_visitor.py`_. Since we know that the test is just one expression, we can just call self.visit() on it. The body could be an infinite number of statements, so we use the `stmt_star_handler`_ function.

`stmt_star_handler`_ returns a namedtuple (`ConnectStatements`_) with the first statement, last_statements and break_statements of all of the statements that were in the body of the node. `stmt_star_handler`_ takes care of connecting each statement in the body to the next one.

We then connect the test node to the first node in the body (if some_condition -> x = 5) and return a namedtuple (`ControlFlowNode`_) with the test, last_statements and break_statements.


.. _visit\_If: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/stmt_visitor.py#L208-L232

.. _ConnectStatements: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/stmt_visitor_helper.py#L15

.. _ControlFlowNode: https://github.com/python-security/pyt/blob/re_organize_code/pyt/core/node_types.py#L7

.. _stmt\_visitor.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/stmt_visitor.py

.. _expr\_visitor.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/expr_visitor.py

.. _stmt_star_handler: https://github.com/python-security/pyt/blob/re_organize_code/pyt/cfg/stmt_visitor.py#L60-L121


.. code-block:: python

  def visit_If(self, node):
      test = self.append_node(IfNode(
          node.test,
          node,
          path=self.filenames[-1]
      ))

      body_connect_stmts = self.stmt_star_handler(node.body)
      # ...
      test.connect(body_connect_stmts.first_statement)

      if node.orelse:
          # ...
      else:
          # if there is no orelse, test needs an edge to the next_node
          body_connect_stmts.last_statements.append(test)

      last_statements = remove_breaks(body_connect_stmts.last_statements)

      return ControlFlowNode(
          test,
          last_statements,
          break_statements=body_connect_stmts.break_statements
      )


.. code-block:: python

  def stmt_star_handler(
      self,
      stmts
  ):
      """Handle stmt* expressions in an AST node.
      Links all statements together in a list of statements.
      Accounts for statements with multiple last nodes.
      """
      break_nodes = list()
      cfg_statements = list()

      first_node = None
      node_not_to_step_past = self.nodes[-1]

      for stmt in stmts:
          node = self.visit(stmt)

          if isinstance(node, ControlFlowNode):
              break_nodes.extend(node.break_statements)
          elif isinstance(node, BreakNode):
              break_nodes.append(node)

          cfg_statements.append(node)
          if not first_node:
              if isinstance(node, ControlFlowNode):
                  first_node = node.test
              else:
                  first_node = get_first_node(
                      node,
                      node_not_to_step_past
                  )

      connect_nodes(cfg_statements)

      if first_node:
          first_statement = first_node
      else:
          first_statement = get_first_statement(cfg_statements[0])

      last_statements = get_last_statements(cfg_statements)

      return ConnectStatements(
          first_statement=first_statement,
          last_statements=last_statements,
          break_statements=break_nodes
      )


.. _ast.NodeVisitor: https://docs.python.org/3/library/ast.html#ast.NodeVisitor
.. _abstract grammar: https://docs.python.org/3/library/ast.html#abstract-grammar

References
==========

For more information on AST nodes, see the `Green Tree Snakes`_ documentation.

.. _Green Tree Snakes: https://greentreesnakes.readthedocs.io/en/latest/nodes.html
