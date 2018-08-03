Web Frameworks
==============

This code determines which functions have their arguments marked at tainted, for example by default the framework adaptor is Flask, so

.. code-block:: python

    @app.route('/')
    def ito_en(image):

will have arguments marked as tainted, whereas 

.. code-block:: python

    def tea(request, param):

will not. (The ``--adaptor D`` option, for Django, would mark the 2nd functions' arguments as tainted and not the first.)

There are currently 4 options for framework route criteria, in the `framework_helper.py`_ file:

- `is_flask_route_function`_, the default, looks for a ``route`` decorator
- `is_django_view_function`_, ``-a D``, looks if the first argument is named ``request``
- `is_function_without_leading_`_, ``-a P``, looks if the function does not start with an underscore
- `is_function`_, ``-a E``, always returns True


.. _framework_helper.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_helper.py

.. _is\_django\_view\_function: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_helper.py#L7
.. _is\_flask\_route\_function: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_helper.py#L14
.. _is\_function\_without\_leading\_: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_helper.py#L28
.. _is\_function: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_helper.py#L23


How the Code Works
==================

`FrameworkAdaptor`_ is what `__main__.py`_ creates, it takes a framework_route_criteria that is chosen by the --adaptor cli argument. The framework_route_criteria is a function that takes an `ast.FunctionDef`_ and returns whether or not it is a route in the selected web framework.

We mark the arguments as tainted by `looping through them`_ and making them node type `TaintedNode`_, where we then `add them to the list of sources`_.


.. _FrameworkAdaptor: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_adaptor.py#L14
.. _\_\_main\_\_.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/__main__.py#L71-L85
.. _ast.FunctionDef: http://greentreesnakes.readthedocs.io/en/latest/nodes.html#FunctionDef

.. _looping through them: https://github.com/python-security/pyt/blob/re_organize_code/pyt/web_frameworks/framework_adaptor.py#L54
.. _TaintedNode: https://github.com/python-security/pyt/blob/re_organize_code/pyt/core/node_types.py#L178
.. _add them to the list of sources: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L51

Caveats
=======

This currently is not smart enough to understand `class-based views`_, so you will have to use ``-a P`` to mark most functions arguments as tainted, and trim false-positives yourself, this is easier with the ``--baseline`` and ``--json`` options.

.. _class-based views: http://flask.pocoo.org/docs/1.0/views/
