"""This module is the comand line tool of pyt."""

import argparse
import os

from cfg import generate_ast, build_cfg
from draw import draw_cfgs, draw_lattices
#from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from fixed_point import analyse
from flask_adaptor import FlaskAdaptor
from vulnerabilities import find_vulnerabilities
from project_handler import get_python_modules, get_directory_modules
from save import create_database
from lattice import generate_lattices
import log

parser = argparse.ArgumentParser()

parser.add_argument('filepath', help='Path to the file that should be analysed.', type=str)
parser.add_argument('-pr', '--project-root', help='Add project root, this is important when the entry file is not at the root of the project.', type=str)
parser.add_argument('-d', '--draw-cfg', help='Draw CFG and output as .pdf file.', action='store_true')
parser.add_argument('-o', '--output-filename', help='Output filename.', type=str)
print_group=parser.add_mutually_exclusive_group()
print_group.add_argument('-p', '--print', help='Prints the nodes of the CFG.', action='store_true')
print_group.add_argument('-vp', '--verbose-print', help='Verbose printing of -p.', action='store_true')
parser.add_argument('-t', '--trigger-word-file', help='Input trigger word file.', type=str)
parser.add_argument('-l', '--log-level', help='Chose logging level: CRITICAL, ERROR, WARNING(Default), INFO, DEBUG, NOTSET.', type=str)
parser.add_argument('-a', '--adaptor', help='Chose an adaptor: FLASK(Default) or DJANGO.', type=str)
parser.add_argument('-db', '--create-database', help='Creates a sql file that can be used to create a database.', action='store_true')
parser.add_argument('-dl', '--draw-lattice',  nargs='+', help='Draws a lattice.')

args = parser.parse_args()

if __name__ == '__main__':
    log.set_logger(args.log_level, show_path=False)

    path = os.path.normpath(args.filepath)

    directory = None
    if args.project_root:
        directory = os.path.normpath(args.project_root)
    else:
        directory = os.path.dirname(path)
    project_modules = get_python_modules(directory)
    local_modules = get_directory_modules(directory)
    
    tree = generate_ast(path)
    cfg = build_cfg(tree, project_modules, local_modules, path)

    cfg_list = [cfg]

    adaptor_type = FlaskAdaptor(cfg_list, project_modules, local_modules)

    lattices = generate_lattices(cfg_list)

    analyse(cfg_list, lattices, analysis_type=ReachingDefinitionsTaintAnalysis)
    
    vulnerability_log = None
    if args.trigger_word_file:
        vulnerability_log = find_vulnerabilities(cfg_list, lattices, args.trigger_word_file)
    else:
        vulnerability_log = find_vulnerabilities(cfg_list, lattices)

    vulnerability_log.print_report()

    if args.draw_cfg:
        if args.output_filename:
            draw_cfgs(cfg_list, args.output_filename)
        else:
            draw_cfgs(cfg_list)
    if args.print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(e)
    if args.verbose_print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(repr(e))

    if args.create_database:
        create_database(cfg_list, vulnerability_log)
    if args.draw_lattice:
        draw_lattices(cfg_list)
        
