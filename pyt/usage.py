import argparse
import os
from datetime import (
    date,
    datetime
)


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


def valid_date(s):
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(s, date_format).date()
    except ValueError:
        msg = "Not a valid date: '{0}'. Format: {1}".format(s, date_format)
        raise argparse.ArgumentTypeError(msg)


def _add_entry_group(parser):
    entry_group = parser.add_mutually_exclusive_group(required=True)
    entry_group.add_argument(
        '-f', '--filepath',
        help='Path to the file that should be analysed.',
        type=str
    )
    entry_group.add_argument(
        '-gr', '--git-repos',
        help='Takes a CSV file of git_url, path per entry.',
        type=str,
        metavar='CSV_FILE'
    )


def _add_regular_arguments(parser):
    parser.add_argument(
        '-r', '--root-directory',
        help='Add project root, this is important when the entry '
             'file is not at the root of the project.',
        type=str,
        metavar='DIR_TO_ANALYZE'
    )
    parser.add_argument(
        '-a', '--adaptor',
        help='Choose a web framework adaptor: '
             'Flask(Default), Django, Every or Pylons',
        type=str
    )
    parser.add_argument(
        '-b', '--baseline',
        help='Path of a baseline report to compare against '
             '(only JSON-formatted files are accepted)',
        type=str,
        default=False,
        metavar='BASELINE_JSON_FILE',
    )
    parser.add_argument(
        '-j', '--json',
        help='Prints JSON instead of report.',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-m', '--blackbox-mapping-file',
        help='Input blackbox mapping file.',
        type=str,
        default=default_blackbox_mapping_file
    )
    parser.add_argument(
        '-t', '--trigger-word-file',
        help='Input trigger word file.',
        type=str,
        default=default_trigger_word_file
    )
    parser.add_argument(
        '-csv', '--csv-path',
        help='Give the path of the csv file '
             'repos should be added to.',
        type=str
    )


def _add_print_group(parser):
    print_group = parser.add_mutually_exclusive_group()
    print_group.add_argument(
        '-trim', '--trim-reassigned-in',
        help='Trims the reassigned list to the vulnerability chain.',
        action='store_true',
        default=True
    )
    print_group.add_argument(
        '--interactive',
        help='Will ask you about each vulnerability chain and blackbox nodes.',
        action='store_true',
        default=False
    )


def _add_search_parser(parser):
    subparsers = parser.add_subparsers()
    search_parser = subparsers.add_parser(
        'github_search',
        help='Searches through github and runs PyT '
             'on found repositories. This can take some time.'
    )
    search_parser.set_defaults(which='search')
    search_parser.add_argument(
        '-ss', '--search-string', required=True,
        help='String for searching for repos on github.',
        type=str
    )
    search_parser.add_argument(
        '-sd', '--start-date',
        help='Start date for repo search. '
             'Criteria used is Created Date.',
        type=valid_date,
        default=date(2010, 1, 1)
    )


def parse_args(args):
    parser = argparse.ArgumentParser(prog='python -m pyt')
    parser.set_defaults(which='')

    _add_entry_group(parser)
    _add_regular_arguments(parser)
    _add_print_group(parser)
    _add_search_parser(parser)

    return parser.parse_args(args)
