This code is responsible for answering two questions:


Where do definitions reach?
===========================

Traditionally `reaching definitions`_, a classic dataflow-analysis,
has been used to answer this question. To understand reaching definitions,
watch this `wonderful YouTube video`_ and come back here.
We use reaching definitions, with one small modification,
a `reassignment check`_.


.. code-block:: python

    # Reassignment check
    if cfg_node.left_hand_side not in cfg_node.right_hand_side_variables:
        # Get previous assignments of cfg_node.left_hand_side and remove them from JOIN
        arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)

As an example,

.. code-block:: python

    image_name = request.args.get('image_name')
    image_name = os.path.join(base_dir, image_name)
    send_file(image_name)

we still want to know that something from a request reached `send_file`.


.. _reaching definitions: https://en.wikipedia.org/wiki/Reaching_definition
.. _reassignment check: https://github.com/python-security/pyt/blob/re_organize_code/pyt/analysis/reaching_definitions_taint.py#L23-L26
.. _wonderful YouTube video: https://www.youtube.com/watch?v=NVBQSR_HdL0


How does a definition reach?
============================

After we know that a definition reaches a use that we are interested in,
we make what use called `definition-use chains`_ to figure out how the definition
reaches the use. This is necessary because there may be more than one path from
the definition to the use. Here is the code from `definition_chains.py`_:

.. code-block:: python

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

.. _definition-use chains: https://en.wikipedia.org/wiki/Use-define_chain
.. _definition_chains.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/analysis/definition_chains.py#L16-L33


Additional details
==================

This folder probably will not change at all for the lifetime of the project,
unless we were to implement more advanced analyses like `solving string
constraints`_ or doing `alias analysis`_. Right now and in the foreseeable
future there are more pressing concerns, like handling web frameworks
and handling all AST node types in the `CFG construction`_.

Stefan and Bruno like the `Schwartzbach notes`_, as you will see in some comments.
But looking these two algorithms up will yield countless results, my favorite is
this `amazing guy from YouTube`_.


.. _solving string constraints: https://zyh1121.github.io/z3str3Docs/inputLanguage.html
.. _alias analysis: https://www3.cs.stonybrook.edu/~liu/papers/Alias-DLS10.pdf
.. _CFG construction: https://github.com/python-security/pyt/tree/re_organize_code/pyt/cfg
.. _Schwartzbach notes: http://lara.epfl.ch/w/_media/sav08:schwartzbach.pdf
.. _amazing guy from YouTube: https://www.youtube.com/watch?v=NVBQSR_HdL0
