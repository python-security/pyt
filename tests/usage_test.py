"""This just tests usage.py"""
import sys
from contextlib import contextmanager
from io import StringIO

from .base_test_case import BaseTestCase
from pyt.usage import parse_args


@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err


class UsageTest(BaseTestCase):
    def test_no_args(self):
        with self.assertRaises(SystemExit):
            with capture_sys_output() as (stdout, _):
                parse_args([])

        self.maxDiff = None

        EXPECTED = """usage: python -m pyt [-h] [-f FILEPATH] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-j] [-m BLACKBOX_MAPPING_FILE]
                     [-t TRIGGER_WORD_FILE] [-trim] [-i]

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

print arguments:
  -trim, --trim-reassigned-in
                        Trims the reassigned list to just the vulnerability
                        chain.
  -i, --interactive     Will ask you about each blackbox function call in
                        vulnerability chains.\n"""

        self.assertEqual(stdout.getvalue(), EXPECTED)

    def test_valid_args_but_no_filepath(self):
        with self.assertRaises(SystemExit):
            with capture_sys_output() as (_, stderr):
                parse_args(['-j'])

        EXPECTED = """usage: python -m pyt [-h] [-f FILEPATH] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-j] [-m BLACKBOX_MAPPING_FILE]
                     [-t TRIGGER_WORD_FILE] [-trim] [-i]
python -m pyt: error: The -f/--filepath argument is required\n"""

        self.assertEqual(stderr.getvalue(), EXPECTED)

    def test_using_both_mutually_exclusive_args(self):
        with self.assertRaises(SystemExit):
            with capture_sys_output() as (_, stderr):
                parse_args(['-f', 'foo.py', '-trim', '--interactive'])

        EXPECTED = """usage: python -m pyt [-h] [-f FILEPATH] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-j] [-m BLACKBOX_MAPPING_FILE]
                     [-t TRIGGER_WORD_FILE] [-trim] [-i]
python -m pyt: error: argument -i/--interactive: not allowed with argument -trim/--trim-reassigned-in\n"""

        self.assertEqual(stderr.getvalue(), EXPECTED)

    def test_normal_usage(self):
        with capture_sys_output() as (stdout, stderr):
            parse_args(['-f', 'foo.py'])

        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(stderr.getvalue(), '')
