"""This module is the comand line tool of pyt."""

import argparse
import os

from ast_helper import generate_ast
from interprocedural_cfg import interprocedural
from intraprocedural_cfg import intraprocedural
from draw import draw_cfgs, draw_lattices
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from liveness import LivenessAnalysis
from reaching_definitions import ReachingDefinitionsAnalysis
from fixed_point import analyse
from flask_adaptor import FlaskAdaptor
from vulnerabilities import find_vulnerabilities
from project_handler import get_python_modules, get_directory_modules
from save import create_database, def_use_chain_to_file
from constraint_table import initialize_constraint_table


parser = argparse.ArgumentParser()

parser.add_argument('filepath',
                    help='Path to the file that should be analysed.', type=str)
parser.add_argument('-pr', '--project-root',
                    help='Add project root, this is important when the entry' +
                    ' file is not at the root of the project.', type=str)
parser.add_argument('-d', '--draw-cfg',
                    help='Draw CFG and output as .pdf file.',
                    action='store_true')
parser.add_argument('-o', '--output-filename',
                    help='Output filename.', type=str)

print_group = parser.add_mutually_exclusive_group()
print_group.add_argument('-p', '--print',
                         help='Prints the nodes of the CFG.',
                         action='store_true')
print_group.add_argument('-vp', '--verbose-print',
                         help='Verbose printing of -p.', action='store_true')

parser.add_argument('-t', '--trigger-word-file',
                    help='Input trigger word file.', type=str)
parser.add_argument('-l', '--log-level',
                    help='Choose logging level: CRITICAL, ERROR,' +
                    ' WARNING(Default), INFO, DEBUG, NOTSET.', type=str)
parser.add_argument('-a', '--adaptor',
                    help='Choose an adaptor: FLASK(Default) or DJANGO.',
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

chains_group = parser.add_mutually_exclusive_group()
chains_group.add_argument('-du', '--def-use-chain',
                          help='Output a def-use chain.', action='store_true')
chains_group.add_argument('-ud', '--use-def-chain',
                          help='Output a use-def chain', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()

    analysis = None
    if args.liveness:
        analysis = LivenessAnalysis
    elif args.reaching:
        analysis = ReachingDefinitionsAnalysis
    elif args.reaching_taint:
        analysis = ReachingDefinitionsTaintAnalysis
    else:
        analysis = ReachingDefinitionsTaintAnalysis

    path = os.path.normpath(args.filepath)

    directory = None
    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_python_modules(directory)
    local_modules = get_directory_modules(directory)

    tree = generate_ast(path)

    cfg_list = list()

    if args.intraprocedural_analysis:
        intraprocedural(project_modules, cfg_list)
    else:
        cfg_list.append(interprocedural(tree, project_modules, local_modules,
                                        path))
        adaptor_type = FlaskAdaptor(cfg_list, project_modules, local_modules)

    initialize_constraint_table(cfg_list)

    analyse(cfg_list, analysis_type=analysis)

    vulnerability_log = None
    if args.trigger_word_file:
        vulnerability_log = find_vulnerabilities(cfg_list, analysis,
                                                 args.trigger_word_file)
    else:
        vulnerability_log = find_vulnerabilities(cfg_list, analysis)

    vulnerability_log.print_report()

    if args.draw_cfg:
        if args.output_filename:
            draw_cfgs(cfg_list, args.output_filename)
        else:
            draw_cfgs(cfg_list)
    if args.print:
        from lattice import print_lattice
        l = print_lattice(cfg_list, analysis)

        from constraint_table import print_table
        print_table(l)
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(e)
    if args.verbose_print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(repr(e))

    if args.print_project_modules:
        from pprint import pprint
        print('############## PROJECT MODULES ##############')
        pprint(project_modules)

    if args.create_database:
        create_database(cfg_list, vulnerability_log)
    if args.draw_lattice:
        draw_lattices(cfg_list)

    if args.def_use_chain:
        def_use_chain_to_file(cfg_list)
