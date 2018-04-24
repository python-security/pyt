.. image:: https://img.shields.io/badge/python-v3.6-blue.svg
    :target: https://pypi.org/project/python-taint/

.. image:: https://travis-ci.org/python-security/pyt.svg?branch=master
    :target: https://travis-ci.org/python-security/pyt

.. image:: https://readthedocs.org/projects/pyt/badge/?version=latest
    :target: http://pyt.readthedocs.io/en/latest/?badge=latest

.. image:: https://codeclimate.com/github/python-security/pyt/badges/coverage.svg
    :target: https://codeclimate.com/github/python-security/pyt/coverage

.. image:: https://badge.fury.io/py/python-taint.svg
    :target: https://badge.fury.io/py/python-taint

.. image:: https://img.shields.io/badge/PRs-welcome-ff69b4.svg
    :target: https://github.com/python-security/pyt/issues?q=is%3Aopen+is%3Aissue+label%3Agood-first-issue

Python Taint
============

Static analysis of Python web applications based on theoretical foundations (Control flow graphs, fixed point, dataflow analysis)

--------
Features
--------

* Detect Command injection

* Detect SQL injection

* Detect XSS

* Detect directory traversal

* Get a control flow graph

* Get a def-use and/or a use-def chain

* Search GitHub and analyse hits with PyT

* A lot of customisation possible

Example usage and output:

.. image:: https://raw.githubusercontent.com/KevinHock/rtdpyt/master/readme_static_files/pyt_example.png

Install
=======

       1. git clone https://github.com/python-security/pyt.git
       2. cd pyt/
       3. python3 setup.py install
       4. pyt -h


Usage from Source
=================

Using it like a user ``python3 -m pyt -f example/vulnerable_code/XSS_call.py save -du``

Running the tests ``python3 -m tests``

Running an individual test file ``python3 -m unittest tests.import_test``

Running an individual test ``python3 -m unittest tests.import_test.ImportTest.test_import``


Contributions
=============

Join our slack group: https://pyt-dev.slack.com/ - ask for invite: mr.thalmann@gmail.com

`Guidelines`_

.. _Guidelines: https://github.com/python-security/pyt/blob/master/CONTRIBUTIONS.md


Virtual env setup guide
=======================

Create a directory to hold the virtual env and project

``mkdir ~/a_folder``

``cd ~/a_folder``

Clone the project into the directory

``git clone https://github.com/python-security/pyt.git``

Create the virtual environment

``python3 -m venv ~/a_folder/``

Check that you have the right versions

``python3 --version`` sample output ``Python 3.6.0``

``pip --version`` sample output ``pip 9.0.1 from /Users/kevinhock/a_folder/lib/python3.6/site-packages (python 3.6)``

Change to project directory

``cd pyt``

Install dependencies

``pip install -r requirements.txt``

``pip list`` sample output ::

    gitdb (0.6.4)
    GitPython (2.0.8)
    graphviz (0.4.10)
    pip (9.0.1)
    requests (2.10.0)
    setuptools (28.8.0)
    smmap (0.9.0)

In the future, just type ``source ~/a_folder/bin/activate`` to start developing.
