This directory contains miscellaneous code that is imported from different parts of the codebase.


`ast_helper.py`_ contains 



- `generate_ast`_ to read any file and generate an AST from it, this is called from `__main__.py`_ and `stmt_visitor.py`_ when importing a module.

- `get_call_names`_ used in `vars_visitor.py`_ when visiting a Subscript, and `framework_helper.py`_ on function decorators in `is_flask_route_function`_

- `get_call_names_as_string`_ used in `expr_visitor.py`_ to create ret_function_name as RHS and yield_function_name as LHS, and in stmt_visitor.py when connecting a function to a loop.

- `Arguments`_ used in `expr_visitor.py`_ when processing the arguments of a user defined function and `framework_adaptor.py`_ to taint function definition arguments.


.. _ast\_helper.py: https://github.com/python-security/pyt/blob/master/pyt/core/ast_helper.py
.. _generate\_ast: https://github.com/python-security/pyt/blob/61ce4751531b01e968698aa537d58b68eb606f01/pyt/core/ast_helper.py#L24-L44

.. _get\_call\_names\_as\_string: https://github.com/python-security/pyt/blob/61ce4751531b01e968698aa537d58b68eb606f01/pyt/core/ast_helper.py#L70-L72
.. _get\_call\_names: https://github.com/python-security/pyt/blob/61ce4751531b01e968698aa537d58b68eb606f01/pyt/core/ast_helper.py#L75-L75




`module_definitions.py`_ contains TODO

`node_types.py`_ contains all the different node types created in `expr_visitor.py`_ and `stmt_visitor.py`_

`project_handler.py`_  contains TODO

.. _module_definitions.py: https://github.com/python-security/pyt/blob/master/pyt/core/module_definitions.py

.. _node_types.py: https://github.com/python-security/pyt/blob/master/pyt/core/node_types.py

.. _project_handler.py: https://github.com/python-security/pyt/blob/master/pyt/core/project_handler.py


.. _\_\_main\_\_.py: https://github.com/python-security/pyt/blob/master/pyt/__main__.py
.. _stmt\_visitor.py: https://github.com/python-security/pyt/blob/master/pyt/cfg/stmt_visitor.py
.. _expr\_visitor.py: https://github.com/python-security/pyt/blob/master/pyt/cfg/expr_visitor.py
.. _framework\_adaptor.py: https://github.com/python-security/pyt/tree/master/pyt/web_frameworks
.. _framework\_helper.py: https://github.com/python-security/pyt/tree/master/pyt/web_frameworks
.. _is\_flask\_route_function: https://github.com/python-security/pyt/tree/master/pyt/web_frameworks
.. _vars\_visitor.py: https://github.com/python-security/pyt/tree/master/pyt/helper_visitors
