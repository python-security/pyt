"""This module is the comand line tool of pyt."""

import argparse
import os
import sys
from datetime import date
from pprint import pprint

from .argument_helpers import valid_date
from .ast_helper import generate_ast
from .draw import draw_cfgs, draw_lattices
from .constraint_table import initialize_constraint_table, print_table
from .fixed_point import analyse
from .framework_adaptor import FrameworkAdaptor
from .framework_helper import (
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_
)
from .github_search import scan_github, set_github_api_token
from .interprocedural_cfg import interprocedural
from .intraprocedural_cfg import intraprocedural
from .lattice import print_lattice
from .liveness import LivenessAnalysis
from .project_handler import get_directory_modules, get_modules
from .reaching_definitions import ReachingDefinitionsAnalysis
from .reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from .repo_runner import get_repos
from .save import (
    cfg_to_file,
    create_database,
    def_use_chain_to_file,
    lattice_to_file,
    Output,
    use_def_chain_to_file,
    verbose_cfg_to_file,
    vulnerabilities_to_file
)
from .vulnerabilities import find_vulnerabilities


def parse_args(args):
    parser = argparse.ArgumentParser(prog='python -m pyt')
    parser.set_defaults(which='')

    subparsers = parser.add_subparsers()

    entry_group = parser.add_mutually_exclusive_group(required=True)
    entry_group.add_argument('-f', '--filepath',
                             help='Path to the file that should be analysed.',
                             type=str)
    entry_group.add_argument('-gr', '--git-repos',
                             help='Takes a CSV file of git_url, path per entry.',
                             type=str)

    parser.add_argument('-pr', '--project-root',
                        help='Add project root, this is important when the entry' +
                        ' file is not at the root of the project.', type=str)
    parser.add_argument('-d', '--draw-cfg',
                        help='Draw CFG and output as .pdf file.',
                        action='store_true')
    parser.add_argument('-o', '--output-filename',
                        help='Output filename.', type=str)
    parser.add_argument('-csv', '--csv-path', type=str,
                        help='Give the path of the csv file'
                        ' repos should be added to.')

    print_group = parser.add_mutually_exclusive_group()
    print_group.add_argument('-p', '--print',
                             help='Prints the nodes of the CFG.',
                             action='store_true')
    print_group.add_argument('-vp', '--verbose-print',
                             help='Verbose printing of -p.', action='store_true')
    print_group.add_argument('-trim', '--trim-reassigned-in',
                             help='Trims the reassigned list to the vulnerability chain.', action='store_true')

    parser.add_argument('-t', '--trigger-word-file',
                        help='Input trigger word file.', type=str)
    parser.add_argument('-py2', '--python-2',
                        help='[WARNING, EXPERIMENTAL] Turns on Python 2 mode,' +
                        ' needed when target file(s) are written in Python 2.', action='store_true')
    parser.add_argument('-l', '--log-level',
                        help='Choose logging level: CRITICAL, ERROR,' +
                        ' WARNING(Default), INFO, DEBUG, NOTSET.', type=str)
    parser.add_argument('-a', '--adaptor',
                        help='Choose an adaptor: Flask(Default), Django, Every or Pylons',
                        type=str)
    parser.add_argument('-db', '--create-database',
                        help='Creates a sql file that can be used to' +
                        ' create a database.', action='store_true')
    parser.add_argument('-dl', '--draw-lattice',
                        nargs='+', help='Draws a lattice.')

    analysis_group = parser.add_mutually_exclusive_group()
    analysis_group.add_argument('-li', '--liveness',
                                help='Run liveness analysis. Default is' +
                                ' reaching definitions tainted version.',
                                action='store_true')
    analysis_group.add_argument('-re', '--reaching',
                                help='Run reaching definitions analysis.' +
                                ' Default is reaching definitions' +
                                ' tainted version.', action='store_true')
    analysis_group.add_argument('-rt', '--reaching-taint',
                                help='This is the default analysis:' +
                                ' reaching definitions tainted version.',
                                action='store_true')

    parser.add_argument('-intra', '--intraprocedural-analysis',
                        help='Run intraprocedural analysis.', action='store_true')
    parser.add_argument('-ppm', '--print-project-modules',
                        help='Print project modules.', action='store_true')

    save_parser = subparsers.add_parser('save', help='Save menu.')
    save_parser.set_defaults(which='save')
    save_parser.add_argument('-fp', '--filename-prefix',
                             help='Filename prefix fx file_lattice.pyt',
                             type=str)
    save_parser.add_argument('-du', '--def-use-chain',
                             help='Output the def-use chain(s) to file.',
                             action='store_true')
    save_parser.add_argument('-ud', '--use-def-chain',
                             help='Output the use-def chain(s) to file',
                             action='store_true')
    save_parser.add_argument('-cfg', '--control-flow-graph',
                             help='Output the CFGs to file.',
                             action='store_true')
    save_parser.add_argument('-vcfg', '--verbose-control-flow-graph',
                             help='Output the verbose CFGs to file.',
                             action='store_true')
    save_parser.add_argument('-an', '--analysis',
                             help='Output analysis results to file'
                             + ' in form of a constraint table.',
                             action='store_true')
    save_parser.add_argument('-la', '--lattice', help='Output lattice(s) to file.',
                             action='store_true')
    save_parser.add_argument('-vu', '--vulnerabilities',
                             help='Output vulnerabilities to file.',
                             action='store_true')
    save_parser.add_argument('-all', '--save-all',
                             help='Output everything to file.',
                             action='store_true')

    search_parser = subparsers.add_parser(
        'github_search',
        help='Searches through github and runs PyT'
        ' on found repositories. This can take some time.')
    search_parser.set_defaults(which='search')

    search_parser.add_argument(
        '-ss', '--search-string', required=True,
        help='String for searching for repos on github.', type=str)

    search_parser.add_argument('-sd', '--start-date',
                               help='Start date for repo search. '
                               'Criteria used is Created Date.', type=valid_date)
    return parser.parse_args(args)


def analyse_repo(github_repo, analysis_type):
    cfg_list = list()
    project_modules = get_modules(os.path.dirname(github_repo.path))
    intraprocedural(project_modules, cfg_list)
    initialize_constraint_table(cfg_list)
    analyse(cfg_list, analysis_type=analysis_type)
    vulnerability_log = find_vulnerabilities(cfg_list, analysis_type)
    return vulnerability_log


def main(command_line_args=sys.argv[1:]):
    args = parse_args(command_line_args)

    analysis = None
    if args.liveness:
        analysis = LivenessAnalysis
    elif args.reaching:
        analysis = ReachingDefinitionsAnalysis
    elif args.reaching_taint:
        analysis = ReachingDefinitionsTaintAnalysis
    else:
        analysis = ReachingDefinitionsTaintAnalysis

    cfg_list = list()
    if args.git_repos:
        repos = get_repos(args.git_repos)
        for repo in repos:
            repo.clone()
            vulnerability_log = analyse_repo(repo, analysis)
            vulnerability_log.print_report()
            if not vulnerability_log.vulnerabilities:
                repo.clean_up()
        exit()

    if args.which == 'search':
        set_github_api_token()
        if args.start_date:
            scan_github(args.search_string, args.start_date,
                        analysis, analyse_repo, args.csv_path)
        else:
            scan_github(args.search_string, date(2010, 1, 1),
                        analysis, analyse_repo, args.csv_path)
        exit()

    path = os.path.normpath(args.filepath)

    directory = None
    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)

    tree = generate_ast(path, python_2=args.python_2)

    cfg_list = list()

    if args.intraprocedural_analysis:
        intraprocedural(project_modules, cfg_list)
    else:
        interprocedural_cfg = interprocedural(tree,
                                              project_modules,
                                              local_modules,
                                              path)
        cfg_list.append(interprocedural_cfg)
        framework_route_criteria = is_flask_route_function
        if args.adaptor:
            if args.adaptor.lower().startswith('e'):
                framework_route_criteria = is_function
            elif args.adaptor.lower().startswith('p'):
                framework_route_criteria = is_function_without_leading_
            elif args.adaptor.lower().startswith('d'):
                framework_route_criteria = is_django_view_function
        # Add all the route functions to the cfg_list
        FrameworkAdaptor(cfg_list, project_modules, local_modules, framework_route_criteria)

    initialize_constraint_table(cfg_list)

    analyse(cfg_list, analysis_type=analysis)

    vulnerability_log = None
    if args.trigger_word_file:
        vulnerability_log = find_vulnerabilities(cfg_list,
                                                 analysis,
                                                 args.trim_reassigned_in,
                                                 args.trigger_word_file)
    else:
        vulnerability_log = find_vulnerabilities(cfg_list,
                                                 analysis,
                                                 args.trim_reassigned_in)

    vulnerability_log.print_report()

    if args.draw_cfg:
        if args.output_filename:
            draw_cfgs(cfg_list, args.output_filename)
        else:
            draw_cfgs(cfg_list)
    if args.print:
        l = print_lattice(cfg_list, analysis)

        print_table(l)
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(e)
    if args.verbose_print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(repr(e))

    if args.print_project_modules:
        print('############## PROJECT MODULES ##############')
        pprint(project_modules)

    if args.create_database:
        create_database(cfg_list, vulnerability_log)
    if args.draw_lattice:
        draw_lattices(cfg_list)

    # Output to file
    if args.which == 'save':
        if args.filename_prefix:
            Output.filename_prefix = args.filename_prefix
        if args.save_all:
            def_use_chain_to_file(cfg_list)
            use_def_chain_to_file(cfg_list)
            cfg_to_file(cfg_list)
            verbose_cfg_to_file(cfg_list)
            lattice_to_file(cfg_list, analysis)
            vulnerabilities_to_file(vulnerability_log)
        else:
            if args.def_use_chain:
                def_use_chain_to_file(cfg_list)
            if args.use_def_chain:
                use_def_chain_to_file(cfg_list)
            if args.control_flow_graph:
                cfg_to_file(cfg_list)
            if args.verbose_control_flow_graph:
                verbose_cfg_to_file(cfg_list)
            if args.lattice:
                lattice_to_file(cfg_list, analysis)
            if args.vulnerabilities:
                vulnerabilities_to_file(vulnerability_log)


if __name__ == '__main__':
    main()
