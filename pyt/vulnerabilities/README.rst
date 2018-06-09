`find_vulnerabilities`_ is what `__main__.py`_ calls, it takes a list of `CFGs`_ and returns a list of vulnerabilities.


The first thing we do is `find all sources and sinks in the file`_, and then `loop through each pair of source and sink to see if a source reaches a sink`_.

Once we obtain def-use chains, we `find all of the paths from source to sink`_.



After we get each vulnerability chain, we see `how_vulnerable`_ it is

There are a few different `vulnerability types`_ used in `how_vulnerable`_.

.. _find_vulnerabilities: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L467-L502
.. _\_\_main\_\_.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/__main__.py#L33-L106
.. _CFGs: https://github.com/python-security/pyt/tree/re_organize_code/pyt/cfg

.. _loop through each pair of source and sink to see if a source reaches a sink: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L452-L464
.. _find all sources and sinks in the file: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L29-L59

.. _find all of the paths from source to sink: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L397-L405

.. _vulnerability types: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerability_helper.py#L8-L12

.. _how_vulnerable: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerabilities.py#L266-L323


Types of Vulnerabilities
========================

Regular
and example code and output

Sanitised

.. code-block:: python
    File: examples/vulnerable_code/XSS_sanitised.py
     > User input at line 7, source "request.args.get(":
    	 ~call_1 = ret_request.args.get('param', 'not set')
    Reassigned in:
    	File: examples/vulnerable_code/XSS_sanitised.py
    	 > Line 7: param = ~call_1
    	File: examples/vulnerable_code/XSS_sanitised.py
    	 > Line 9: ~call_2 = ret_Markup.escape(param)
    	File: examples/vulnerable_code/XSS_sanitised.py
    	 > Line 9: param = ~call_2
    File: examples/vulnerable_code/XSS_sanitised.py
     > reaches line 12, sink "replace(":
    	~call_5 = ret_html.replace('{{ param }}', param)
    This vulnerability is sanitised by:  Label: ~call_2 = ret_Markup.escape(param)

and example code and output

Unknown
and example code and output


How we find secondary nodes

How we find sources/sinks

How def-use chains are used
