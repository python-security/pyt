`__main__.py`_ is where all the high-level steps happen.

.. _\_\_main\_\_.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/__main__.py

Step 1
    Parse command line arguments.

    `parse_args`_ in `usage.py`_

    .. _parse_args: https://github.com/python-security/pyt/blob/re_organize_code/pyt/usage.py#L113
    .. _usage.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/usage.py


Step 2
    Generate the Abstract Syntax Tree (AST).

    Essentially done in these lines of code with the `ast`_ module:

    .. code-block:: python

        import ast
        ast.parse(f.read())

    `generate_ast`_ in `ast_helper.py`_

    .. _ast: https://docs.python.org/3/library/ast.html
    .. _generate_ast: https://github.com/python-security/pyt/blob/re_organize_code/pyt/core/ast_helper.py#L24
    .. _ast_helper.py: https://github.com/python-security/pyt/blob/re_organize_code/pyt/core/ast_helper.py


Step 3
    Pass the AST to create a `Control Flow Graph (CFG)`_

    .. _Control Flow Graph (CFG): https://github.com/python-security/pyt/tree/re_organize_code/pyt/cfg

Step 4
    Pass the CFG to a `Framework Adaptor`_, which will mark the arguments of certain functions as tainted sources.

    .. _Framework Adaptor: https://github.com/python-security/pyt/tree/re_organize_code/pyt/web_frameworks

Step 5
    Perform `(modified-)reaching definitions analysis`_, to know where definitions reach.

    .. _\(modified\-\)reaching definitions analysis: https://github.com/python-security/pyt/tree/re_organize_code/pyt/analysis

Step 6
    `Find vulnerabilities`_, by seeing where sources reach, and how.

    .. _Find vulnerabilities: https://github.com/python-security/pyt/tree/re_organize_code/pyt/vulnerabilities

Step 7
    `Remove already known vulnerabilities`_ if a `baseline`_ (JSON file of a previous run of PyT) is provided.

    .. _Remove already known vulnerabilities: https://github.com/python-security/pyt/blob/re_organize_code/pyt/vulnerabilities/vulnerability_helper.py#L194
    .. _baseline: https://github.com/python-security/pyt/blob/re_organize_code/pyt/usage.py#L54

Step 8
    Output the results in either `text or JSON form`_, to stdout or the `output file`_.

    .. _text or JSON form: https://github.com/python-security/pyt/tree/re_organize_code/pyt/formatters
    .. _output file: https://github.com/python-security/pyt/blob/re_organize_code/pyt/usage.py#L80
