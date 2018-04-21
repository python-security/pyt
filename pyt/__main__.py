"""The comand line module of PyT."""

import argparse
import os
import sys
from datetime import date

from .analysis.constraint_table import initialize_constraint_table
from .analysis.fixed_point import analyse
from .argument_helpers import (
    default_blackbox_mapping_file,
    default_trigger_word_file,
    valid_date,
    VulnerabilityFiles,
    UImode
)
from .ast_helper import generate_ast
from .baseline import get_vulnerabilities_not_in_baseline
from .expr_visitor import make_cfg
from .formatters import (
    json,
    text
)
from .framework_adaptor import FrameworkAdaptor
from .framework_helper import (
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_
)
from .github_search import (
    analyse_repos,
    scan_github,
    set_github_api_token
)
from .project_handler import (
    get_directory_modules,
    get_modules
)
from .vulnerabilities import find_vulnerabilities


def parse_args(args):
    parser = argparse.ArgumentParser(prog='python -m pyt')
    parser.set_defaults(which='')

    subparsers = parser.add_subparsers()

    entry_group = parser.add_mutually_exclusive_group(required=True)
    entry_group.add_argument(
        '-f', '--filepath',
        help='Path to the file that should be analysed.',
        type=str
    )
    entry_group.add_argument(
        '-gr', '--git-repos',
        help='Takes a CSV file of git_url, path per entry.',
        type=str
    )

    parser.add_argument(
        '-pr', '--project-root',
        help='Add project root, this is important when the entry '
             'file is not at the root of the project.',
        type=str
    )
    parser.add_argument(
        '-csv', '--csv-path', type=str,
        help='Give the path of the csv file'
        ' repos should be added to.'
    )
    parser.add_argument(
        '-t', '--trigger-word-file',
        help='Input trigger word file.',
        type=str,
        default=default_trigger_word_file
    )
    parser.add_argument(
        '-m', '--blackbox-mapping-file',
        help='Input blackbox mapping file.',
        type=str,
        default=default_blackbox_mapping_file
    )
    parser.add_argument(
        '-py2', '--python-2',
        help='[WARNING, EXPERIMENTAL] Turns on Python 2 mode,' +
             ' needed when target file(s) are written in Python 2.',
        action='store_true'
    )
    parser.add_argument(
        '-l', '--log-level',
        help='Choose logging level: CRITICAL, ERROR,'
             ' WARNING(Default), INFO, DEBUG, NOTSET.',
        type=str
    )
    parser.add_argument(
        '-a', '--adaptor',
        help='Choose an adaptor: Flask(Default), Django, Every or Pylons',
        type=str
    )
    parser.add_argument(
        '-j', '--json',
        help='Prints JSON instead of report.',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-b', '--baseline',
        help='path of a baseline report to compare against '
             '(only JSON-formatted files are accepted)',
        type=str,
        default=False
    )

    print_group = parser.add_mutually_exclusive_group()
    print_group.add_argument(
        '-trim', '--trim-reassigned-in',
        help='Trims the reassigned list to the vulnerability chain.',
        action='store_true',
        default=False
    )
    print_group.add_argument(
        '-i', '--interactive',
        help='Will ask you about each vulnerability chain and blackbox nodes.',
        action='store_true',
        default=False
    )

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

    return parser.parse_args(args)


def main(command_line_args=sys.argv[1:]):
    args = parse_args(command_line_args)

    ui_mode = UImode.NORMAL
    if args.interactive:
        ui_mode = UImode.INTERACTIVE
    elif args.trim_reassigned_in:
        ui_mode = UImode.TRIM

    cfg_list = list()
    if args.git_repos:
        analyse_repos(
            args,
            ui_mode
        )
        exit()
    elif args.which == 'search':
        set_github_api_token()
        scan_github(
            args,
            ui_mode
        )
        exit()

    path = os.path.normpath(args.filepath)

    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)

    tree = generate_ast(path, python_2=args.python_2)

    cfg = make_cfg(
        tree,
        project_modules,
        local_modules,
        path
    )
    cfg_list = list(cfg)
    framework_route_criteria = is_flask_route_function
    if args.adaptor:
        if args.adaptor.lower().startswith('e'):
            framework_route_criteria = is_function
        elif args.adaptor.lower().startswith('p'):
            framework_route_criteria = is_function_without_leading_
        elif args.adaptor.lower().startswith('d'):
            framework_route_criteria = is_django_view_function
    # Add all the route functions to the cfg_list
    FrameworkAdaptor(
        cfg_list,
        project_modules,
        local_modules,
        framework_route_criteria
    )

    initialize_constraint_table(cfg_list)
    analyse(cfg_list)
    vulnerabilities = find_vulnerabilities(
        cfg_list,
        ui_mode,
        VulnerabilityFiles(
            args.blackbox_mapping_file,
            args.trigger_word_file
        )
    )
    if args.baseline:
        vulnerabilities = get_vulnerabilities_not_in_baseline(
            vulnerabilities,
            args.baseline
        )

    if args.json:
        json.report(vulnerabilities, sys.stdout)
    else:
        text.report(vulnerabilities, sys.stdout)


if __name__ == '__main__':
    main()
