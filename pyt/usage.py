import argparse
import os
import sys

from .formatters import json, screen, text


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
        'targets', metavar='targets', nargs='+',
        help='source file(s) or directory(s) to be scanned',
        type=str
    )


def _add_optional_group(parser):
    optional_group = parser.add_argument_group('optional arguments')
    optional_group.add_argument(
        '-v', '--verbose',
        action='count',
        help='Increase logging verbosity. Can repeated e.g. -vvv',
    )
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
        '-t', '--trigger-word-file',
        help='Input file with a list of sources and sinks',
        type=str,
        default=default_trigger_word_file
    )
    optional_group.add_argument(
        '-m', '--blackbox-mapping-file',
        help='Input blackbox mapping file.',
        type=str,
        default=default_blackbox_mapping_file
    )
    optional_group.add_argument(
        '-i', '--interactive',
        help='Will ask you about each blackbox function call in vulnerability chains.',
        action='store_true',
        default=False
    )
    optional_group.add_argument(
        '-o', '--output',
        help='Write report to filename',
        dest='output_file',
        action='store',
        type=argparse.FileType('w'),
        default=sys.stdout,
    )
    optional_group.add_argument(
        '--ignore-nosec',
        dest='ignore_nosec',
        action='store_true',
        help='Do not skip lines with # nosec comments'
    )
    optional_group.add_argument(
        '-r', '--recursive',
        dest='recursive',
        action='store_true',
        help='Find and process files in subdirectories'
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
    optional_group.add_argument(
        '-u', '--only-unsanitised',
        help="Don't print sanitised vulnerabilities.",
        action='store_true',
        default=False,
    )
    parser.set_defaults(formatter=text)
    formatter_group = optional_group.add_mutually_exclusive_group()
    formatter_group.add_argument(
        '-j', '--json',
        help='Prints JSON instead of report.',
        action='store_const',
        const=json,
        dest='formatter',
    )
    formatter_group.add_argument(
        '-s', '--screen',
        help='Prints colorful report.',
        action='store_const',
        const=screen,
        dest='formatter',
    )


def parse_args(args):
    if len(args) == 0:
        args.append('-h')
    parser = argparse.ArgumentParser(prog='python -m pyt')

    # Hack to in order to list required args above optional
    parser._action_groups.pop()

    _add_required_group(parser)
    _add_optional_group(parser)

    args = parser.parse_args(args)
    if args.targets is None:
        parser.error('The targets argument is required')
    return args
