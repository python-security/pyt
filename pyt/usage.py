import argparse
import os
import sys


default_blackbox_mapping_file = os.path.join(
    os.path.dirname(__file__),
    'vulnerability_definitions',
    'blackbox_mapping.json'
)


default_trigger_word_file = os.path.join(
    os.path.dirname(__file__),
    'vulnerability_definitions',
    'all_trigger_words.pyt'
)


def _add_required_group(parser):
    required_group = parser.add_argument_group('required arguments')
    required_group.add_argument(
        'targets', metavar='targets', type=str, nargs='+',
        help='source file(s) or directory(s) to be tested'
    )


def _add_optional_group(parser):
    optional_group = parser.add_argument_group('optional arguments')

    optional_group.add_argument(
        '-a', '--adaptor',
        help='Choose a web framework adaptor: '
             'Flask(Default), Django, Every or Pylons',
        type=str
    )
    optional_group.add_argument(
        '-pr', '--project-root',
        help='Add project root, only important when the entry '
             'file is not at the root of the project.',
        type=str
    )
    optional_group.add_argument(
        '-b', '--baseline',
        help='Path of a baseline report to compare against '
             '(only JSON-formatted files are accepted)',
        type=str,
        default=False,
        metavar='BASELINE_JSON_FILE',
    )
    optional_group.add_argument(
        '-j', '--json',
        help='Prints JSON instead of report.',
        action='store_true',
        default=False
    )
    optional_group.add_argument(
        '-m', '--blackbox-mapping-file',
        help='Input blackbox mapping file.',
        type=str,
        default=default_blackbox_mapping_file
    )
    optional_group.add_argument(
        '-t', '--trigger-word-file',
        help='Input file with a list of sources and sinks',
        type=str,
        default=default_trigger_word_file
    )
    optional_group.add_argument(
        '-o', '--output',
        help='write report to filename',
        dest='output_file',
        action='store',
        type=argparse.FileType('w'),
        default=sys.stdout,
    )
    optional_group.add_argument(
        '--ignore-nosec',
        dest='ignore_nosec',
        action='store_true',
        help='do not skip lines with # nosec comments'
    )
    optional_group.add_argument(
        '-r', '--recursive', dest='recursive',
        action='store_true', help='find and process files in subdirectories'
    )
    optional_group.add_argument(
        '-x', '--exclude',
        dest='excluded_paths',
        action='store',
        default='',
        help='Separate files with commas'
    )
    optional_group.add_argument(
        '--dont-prepend-root',
        help="In project root e.g. /app, imports are not prepended with app.*",
        action='store_false',
        default=True,
        dest='prepend_module_root'
    )
    optional_group.add_argument(
        '--no-local-imports',
        help='If set, absolute imports must be relative to the project root. '
             'If not set, modules in the same directory can be imported just by their names.',
        action='store_false',
        default=True,
        dest='allow_local_imports'
    )


def _add_print_group(parser):
    print_group = parser.add_argument_group('print arguments')
    print_group.add_argument(
        '-trim', '--trim-reassigned-in',
        help='Trims the reassigned list to just the vulnerability chain.',
        action='store_true',
        default=True
    )
    print_group.add_argument(
        '-i', '--interactive',
        help='Will ask you about each blackbox function call in vulnerability chains.',
        action='store_true',
        default=False
    )


def _check_required_and_mutually_exclusive_args(parser, args):
    if args.targets is None:
        parser.error('The targets argument is required')


def parse_args(args):
    if len(args) == 0:
        args.append('-h')
    parser = argparse.ArgumentParser(prog='python -m pyt')
    parser._action_groups.pop()
    _add_required_group(parser)
    _add_optional_group(parser)
    _add_print_group(parser)

    args = parser.parse_args(args)
    _check_required_and_mutually_exclusive_args(
        parser,
        args
    )
    return args
