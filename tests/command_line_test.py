"""This just tests __main__.py"""
import sys
from contextlib import contextmanager
from io import StringIO

from .base_test_case import BaseTestCase
from pyt.__main__ import parse_args


@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err


class CommandLineTest(BaseTestCase):
    def test_no_args(self):
        with self.assertRaises(SystemExit):
            with capture_sys_output() as (_, stderr):
                parse_args([])

        EXPECTED = """usage: python -m pyt [-h] (-f FILEPATH | -gr GIT_REPOS) [-pr PROJECT_ROOT]
                     [-csv CSV_PATH] [-t TRIGGER_WORD_FILE]
                     [-m BLACKBOX_MAPPING_FILE] [-py2] [-l LOG_LEVEL]
                     [-a ADAPTOR] [-j] [-b BASELINE] [-trim | -i]
                     {github_search} ...\n""" + \
                     "python -m pyt: error: one of the arguments " + \
                     "-f/--filepath -gr/--git-repos is required\n"
        self.assertEqual(stderr.getvalue(), EXPECTED)
