"""The comand line module of PyT."""

import os
import sys

from .analysis.constraint_table import initialize_constraint_table
from .analysis.fixed_point import analyse
from .cfg import make_cfg
from .core.ast_helper import generate_ast
from .core.project_handler import (
    get_directory_modules,
    get_modules
)
from .formatters import (
    json,
    text
)
from .usage import parse_args
from .vulnerabilities import (
    find_vulnerabilities,
    get_vulnerabilities_not_in_baseline,
    UImode
)
from .web_frameworks import (
    FrameworkAdaptor,
    is_django_view_function,
    is_flask_route_function,
    is_function,
    is_function_without_leading_
)
<<<<<<< HEAD
=======
from .github_search import scan_github, set_github_api_token
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
                             help='Trims the reassigned list to the vulnerability chain.',
                             action='store_true',
                             default=False)
    print_group.add_argument('-i', '--interactive',
                             help='Will ask you about each vulnerability chain and blackbox nodes.',
                             action='store_true',
                             default=False)

    parser.add_argument('-t', '--trigger-word-file',
                        help='Input trigger word file.',
                        type=str,
                        default=default_trigger_word_file)
    parser.add_argument('-m', '--blackbox-mapping-file',
                        help='Input blackbox mapping file.',
                        type=str,
                        default=default_blackbox_mapping_file)
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
    parser.add_argument('-j', '--json',
                        help='Prints JSON instead of report.',
                        action='store_true',
                        default=False)

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

    parser.add_argument('-ppm', '--print-project-modules',
                        help='Print project modules.', action='store_true')
    parser.add_argument('-b', '--baseline',
                        help='path of a baseline report to compare against '
                             '(only JSON-formatted files are accepted)',
                        type=str,
                        default=False)
    parser.add_argument('--ignore-nosec', dest='ignore_nosec', action='store_true',
                         help='do not skip lines with # nosec comments')

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
                             help='Output analysis results to file' +
                             ' in form of a constraint table.',
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
                               'Criteria used is Created Date.',
                               type=valid_date,
                               default=date(2010, 1, 1))
    return parser.parse_args(args)


def analyse_repo(args, github_repo, analysis_type, ui_mode, nosec_lines):
    cfg_list = list()
    directory = os.path.dirname(github_repo.path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)
    tree = generate_ast(github_repo.path)
    cfg = make_cfg(
        tree,
        project_modules,
        local_modules,
        github_repo.path
    )
    cfg_list.append(cfg)

    initialize_constraint_table(cfg_list)
    analyse(cfg_list, analysis_type=analysis_type)
    vulnerabilities = find_vulnerabilities(
        cfg_list,
        analysis_type,
        ui_mode,
        VulnerabilityFiles(
            args.blackbox_mapping_file,
            args.trigger_word_file
        ),
        nosec_lines
    )
    return vulnerabilities
>>>>>>> 5b372d267efa8cccc75c998b5d3fe56f2904f116


def main(command_line_args=sys.argv[1:]):
    args = parse_args(command_line_args)

    ui_mode = UImode.NORMAL
    if args.interactive:
        ui_mode = UImode.INTERACTIVE
    elif args.trim_reassigned_in:
        ui_mode = UImode.TRIM

    path = os.path.normpath(args.filepath)
<<<<<<< HEAD
=======
    cfg_list = list()
    if args.ignore_nosec:
        nosec_lines = set()
    else:
        file = open(path, "r")
        lines = file.readlines()
        nosec_lines = set(
                    lineno for
                    (lineno, line) in enumerate(lines, start=1)
                    if '#nosec' in line or '# nosec' in line)
        
    if args.git_repos:
        repos = get_repos(args.git_repos)
        for repo in repos:
            repo.clone()
            vulnerabilities = analyse_repo(args, repo, analysis, ui_mode, nosec_lines)
            if args.json:
                json.report(vulnerabilities, sys.stdout)
            else:
                text.report(vulnerabilities, sys.stdout)
            if not vulnerabilities:
                repo.clean_up()
        exit()


    if args.which == 'search':
        set_github_api_token()
        scan_github(
            args.search_string,
            args.start_date,
            analysis,
            analyse_repo,
            args.csv_path,
            ui_mode,
            args
        )
        exit()

    directory = None
>>>>>>> 5b372d267efa8cccc75c998b5d3fe56f2904f116
    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_modules(directory)
    local_modules = get_directory_modules(directory)

    tree = generate_ast(path)

    cfg = make_cfg(
        tree,
        project_modules,
        local_modules,
        path
    )
    cfg_list = [cfg]
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
<<<<<<< HEAD
        args.blackbox_mapping_file,
        args.trigger_word_file
=======
        VulnerabilityFiles(
            args.blackbox_mapping_file,
            args.trigger_word_file
        ),
        nosec_lines
>>>>>>> 5b372d267efa8cccc75c998b5d3fe56f2904f116
    )
    
    if args.baseline:
        vulnerabilities = get_vulnerabilities_not_in_baseline(
            vulnerabilities,
            args.baseline
        )

    if args.json:
        json.report(vulnerabilities, args.output_file)
    else:
        text.report(vulnerabilities, args.output_file)


if __name__ == '__main__':
    main()
