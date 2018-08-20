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
	✨🍰✨

PyT can also be installed from source. To do so, clone the repo, and then run:

.. code-block:: python

  python3 setup.py install

How it Works
============

Soon you will find a `README.rst`_ in every directory in the ``pyt/`` folder, `start here`_.

.. _README.rst: https://github.com/python-security/pyt/tree/master/pyt
.. _start here: https://github.com/python-security/pyt/tree/master/pyt


How to Use
============

1. Choose a web framework

`The -a option determines which functions will have their arguments tainted`_, by default it is Flask.

2. (optional) Customize source and sink information

Use the ``-t`` option to specify sources and sinks, by default `this file is used`_.

3. (optional) Customize which library functions propagate taint

For functions from builtins or libraries, e.g. ``url_for`` or ``os.path.join``, use the ``-m`` option to specify whether or not they return tainted values given tainted inputs, by `default this file is used`_.

.. _The -a option determines which functions will have their arguments tainted: https://github.com/python-security/pyt/tree/master/pyt/web_frameworks#web-frameworks
.. _this file is used: https://github.com/python-security/pyt/blob/master/pyt/vulnerability_definitions/all_trigger_words.pyt
.. _default this file is used: https://github.com/python-security/pyt/blob/master/pyt/vulnerability_definitions/blackbox_mapping.json


Usage
=====

.. code-block::

  usage: python -m pyt [-h] [-a ADAPTOR] [-pr PROJECT_ROOT]
                       [-b BASELINE_JSON_FILE] [-j] [-t TRIGGER_WORD_FILE]
                       [-m BLACKBOX_MAPPING_FILE] [-i] [-o OUTPUT_FILE]
                       [--ignore-nosec] [-r] [-x EXCLUDED_PATHS]
                       [--dont-prepend-root] [--no-local-imports]
                       targets [targets ...]

  required arguments:
    targets               source file(s) or directory(s) to be scanned

  important optional arguments:
    -a ADAPTOR, --adaptor ADAPTOR
                          Choose a web framework adaptor: Flask(Default),
                          Django, Every or Pylons

    -t TRIGGER_WORD_FILE, --trigger-word-file TRIGGER_WORD_FILE
                          Input file with a list of sources and sinks

    -m BLACKBOX_MAPPING_FILE, --blackbox-mapping-file BLACKBOX_MAPPING_FILE
                              Input blackbox mapping file

  optional arguments:
    -pr PROJECT_ROOT, --project-root PROJECT_ROOT
                          Add project root, only important when the entry file
                          is not at the root of the project.

    -b BASELINE_JSON_FILE, --baseline BASELINE_JSON_FILE
                          Path of a baseline report to compare against (only
                          JSON-formatted files are accepted)

    -j, --json            Prints JSON instead of report.

    -i, --interactive     Will ask you about each blackbox function call in
                          vulnerability chains.

    -o OUTPUT_FILE, --output OUTPUT_FILE
                          Write report to filename

    --ignore-nosec        Do not skip lines with # nosec comments

    -r, --recursive       Find and process files in subdirectories

    -x EXCLUDED_PATHS, --exclude EXCLUDED_PATHS
                          Separate files with commas

    --dont-prepend-root   In project root e.g. /app, imports are not prepended
                          with app.*

    --no-local-imports    If set, absolute imports must be relative to the
                          project root. If not set, modules in the same
                          directory can be imported just by their names.

Usage from Source
=================

Using it like a user ``python3 -m pyt examples/vulnerable_code/XSS_call.py``

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

In the future, just type ``source ~/a_folder/bin/activate`` to start developing.
