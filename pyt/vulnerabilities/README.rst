Coming soon.

The first thing we do is `find all sources and sinks in the file`_, and then `loop through each pair of source and sink to see if a source reaches a sink`_.

Once we obtain def-use chains, we `find all of the paths from source to sink`_.



After we get each vulnerability chain, we see `how_vulnerable`_ it is

There are a few different `vulnerability types`_ used in `how_vulnerable`_.

.. _loop through each pair of source and sink to see if a source reaches a sink: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L452-L464
.. _find all sources and sinks in the file: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L29-L59

.. _find all of the paths from source to sink: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L397-L405

.. _vulnerability types: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerability_helper.py#L8-L12

.. _how_vulnerable: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L266-L323


Regular
Sanitised
Unknown


How we find secondary nodes

How we find sources/sinks

How def-use chains are used
