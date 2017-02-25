[![Build Status](https://travis-ci.org/python-security/pyt.svg?branch=master)](https://travis-ci.org/python-security/pyt)

# PyT - Python Taint

Static analysis of Python web applications based on theoretical foundations (Control flow graphs, fixed point, dataflow analysis)

Features planned:
- Detect Command injection
- Detect SQL injection
- Detect XSS
- Detect directory traversal

Using it like a user:
`python -m pyt -f example/vulnerable_code/XSS_call.py save -du`

Running the tests: `python -m tests`

Work in progress

## Virtual env setup guide

Create a directory to hold the virtual env and project

`mkdir ~/pyt`

`cd ~/pyt`

Clone the project into the directory

`git clone https://github.com/python-security/pyt.git`

Create the virtual environment

`python3 -m venv ~/pyt/`

Check that you have the right versions

`python --version` sample output `Python 3.6.0`

`pip --version` sample output `pip 9.0.1 from /Users/kevinhock/pyt/lib/python3.6/site-packages (python 3.6)`

Change to project directory

`cd pyt`

Install dependencies

`pip install -r requirements.txt`

`pip list` sample output
```
gitdb (0.6.4)

GitPython (2.0.8)

graphviz (0.4.10)

pip (9.0.1)

requests (2.10.0)

setuptools (28.8.0)

smmap (0.9.0)
```

In the future, just type `source ~/pyt/bin/activate` to start developing.
