# PyT - Python Taint

Static analysis of Python web applications based on theoretical foundations (Control flow graphs, fixed point, dataflow analysis)

Features planned:
- Detect Command injection
- Detect SQL injection
- Detect XSS
- Detect directory traversal

Using it like a user:
`python3 pyt.py -f ../example/vulnerable_code/XSS_call.py save -du`

Work in progress

[![Build Status](https://travis-ci.org/python-security/pyt.svg?branch=master)](https://travis-ci.org/python-security/pyt)
