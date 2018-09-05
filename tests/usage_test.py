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

        EXPECTED = """usage: python -m pyt [-h] [-v] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-t TRIGGER_WORD_FILE]
                     [-m BLACKBOX_MAPPING_FILE] [-i] [-o OUTPUT_FILE]
                     [--ignore-nosec] [-r] [-x EXCLUDED_PATHS]
                     [--dont-prepend-root] [--no-local-imports] [-u] [-j | -s]
                     targets [targets ...]

required arguments:
  targets               source file(s) or directory(s) to be scanned

optional arguments:
  -v, --verbose         Increase logging verbosity. Can repeated e.g. -vvv
  -a ADAPTOR, --adaptor ADAPTOR
                        Choose a web framework adaptor: Flask(Default),
                        Django, Every or Pylons
  -pr PROJECT_ROOT, --project-root PROJECT_ROOT
                        Add project root, only important when the entry file
                        is not at the root of the project.
  -b BASELINE_JSON_FILE, --baseline BASELINE_JSON_FILE
                        Path of a baseline report to compare against (only
                        JSON-formatted files are accepted)
  -t TRIGGER_WORD_FILE, --trigger-word-file TRIGGER_WORD_FILE
                        Input file with a list of sources and sinks
  -m BLACKBOX_MAPPING_FILE, --blackbox-mapping-file BLACKBOX_MAPPING_FILE
                        Input blackbox mapping file.
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
  -u, --only-unsanitised
                        Don't print sanitised vulnerabilities.
  -j, --json            Prints JSON instead of report.
  -s, --screen          Prints colorful report.\n"""

        self.assertEqual(stdout.getvalue(), EXPECTED)

    def test_valid_args_but_no_targets(self):
        with self.assertRaises(SystemExit):
            with capture_sys_output() as (_, stderr):
                parse_args(['-j'])

        EXPECTED = """usage: python -m pyt [-h] [-v] [-a ADAPTOR] [-pr PROJECT_ROOT]
                     [-b BASELINE_JSON_FILE] [-t TRIGGER_WORD_FILE]
                     [-m BLACKBOX_MAPPING_FILE] [-i] [-o OUTPUT_FILE]
                     [--ignore-nosec] [-r] [-x EXCLUDED_PATHS]
                     [--dont-prepend-root] [--no-local-imports] [-u] [-j | -s]
                     targets [targets ...]
python -m pyt: error: the following arguments are required: targets\n"""

        self.assertEqual(stderr.getvalue(), EXPECTED)

#     def test_using_both_mutually_exclusive_args(self):
#         with self.assertRaises(SystemExit):
#             with capture_sys_output() as (_, stderr):
#                 parse_args(['-f', 'foo.py', '-trim', '--interactive'])

#         EXPECTED = """usage: python -m pyt [-h] [-f FILEPATH] [-a ADAPTOR] [-pr PROJECT_ROOT]
#                      [-b BASELINE_JSON_FILE] [-j] [-m BLACKBOX_MAPPING_FILE]
#                      [-t TRIGGER_WORD_FILE] [-o OUTPUT_FILE] [-trim] [-i]
# python -m pyt: error: argument -i/--interactive: not allowed with argument -trim/--trim-reassigned-in\n"""

#         self.assertEqual(stderr.getvalue(), EXPECTED)

    def test_normal_usage(self):
        with capture_sys_output() as (stdout, stderr):
            parse_args(['foo.py'])

        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(stderr.getvalue(), '')
