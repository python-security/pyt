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

.. image:: https://img.shields.io/badge/python-v3.6-blue.svg
    :target: https://pypi.org/project/python-taint/

Python Taint
============

Static analysis of Python web applications based on theoretical foundations (Control flow graphs, fixed point, dataflow analysis)

--------
Features
--------

* Detect command injection, SSRF, SQL injection, XSS, directory traveral etc.

* A lot of customisation possible

For a look at recent changes, please see the `changelog`_.

.. _changelog: https://github.com/python-security/pyt/blob/master/CHANGELOG.md

Example usage and output:

.. image:: https://raw.githubusercontent.com/KevinHock/rtdpyt/master/readme_static_files/pyt_example.png

Install
=======

.. code-block:: python

	pip install python-taint

PyT can also be installed from source. To do so, clone the repo, and then run:

.. code-block:: python

  python3 setup.py install

How It Works
============

Soon you will find a README.rst in every directory in the pyt folder, `start here`_.

.. _start here: https://github.com/python-security/pyt/tree/re_organize_code/pyt

Usage
=====

.. code-block::

  usage: python -m pyt [-h] [-f FILEPATH] [-a ADAPTOR] [-pr PROJECT_ROOT]
                       [-b BASELINE_JSON_FILE] [-j] [-m BLACKBOX_MAPPING_FILE]
                       [-t TRIGGER_WORD_FILE] [-o OUTPUT_FILE] [-trim] [-i]

  required arguments:
    -f FILEPATH, --filepath FILEPATH
                          Path to the file that should be analysed.

  optional arguments:
    -a ADAPTOR, --adaptor ADAPTOR
                          Choose a web framework adaptor: Flask(Default),
                          Django, Every or Pylons
    -pr PROJECT_ROOT, --project-root PROJECT_ROOT
                          Add project root, only important when the entry file
                          is not at the root of the project.
    -b BASELINE_JSON_FILE, --baseline BASELINE_JSON_FILE
                          Path of a baseline report to compare against (only
                          JSON-formatted files are accepted)
    -j, --json            Prints JSON instead of report.
    -m BLACKBOX_MAPPING_FILE, --blackbox-mapping-file BLACKBOX_MAPPING_FILE
                          Input blackbox mapping file.
    -t TRIGGER_WORD_FILE, --trigger-word-file TRIGGER_WORD_FILE
                          Input file with a list of sources and sinks
    -o OUTPUT_FILE, --output OUTPUT_FILE
                          write report to filename
    --ignore-nosec        do not skip lines with # nosec comments

  print arguments:
    -trim, --trim-reassigned-in
                          Trims the reassigned list to just the vulnerability
                          chain.
    -i, --interactive     Will ask you about each blackbox function call in
                          vulnerability chains.

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
