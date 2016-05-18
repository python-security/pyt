import argparse
import os

from cfg import generate_ast, CFG
from draw import draw_cfg
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis
from fixed_point import analyse
from flask_adaptor import FlaskAdaptor
from vulnerabilities import find_vulnerabilities
from project_handler import get_python_modules, get_directory_modules
import log

parser = argparse.ArgumentParser()

parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)
parser.add_argument('-d', '--draw-cfg', help = 'Draw CFG and output as .svg file.', action='store_true')
parser.add_argument('-o', '--output-filename', help = 'Output filename.', type = str)
parser.add_argument('-p', '--print', help = 'Prints the nodes of the CFG.', action='store_true')
parser.add_argument('-vp', '--verbose-print', help = 'Verbose printing of -p.', action='store_true')
parser.add_argument('-t', '--trigger-word-file', help='Input trigger word file.', type=str)
parser.add_argument('-l', '--log-level', help='Chose logging level: CRITICAL, ERROR, WARNING(Default), INFO, DEBUG, NOTSET.', type=str)

args = parser.parse_args()

if __name__ == '__main__':
    logger = log.get_logger(args.log_level, __name__, show_path=False)

    path = os.path.normpath(args.filename)

    directory = os.path.dirname(path)
    project_modules = get_python_modules(directory)
    local_modules = get_directory_modules(directory)
    
    tree = generate_ast(path)
    cfg = CFG(project_modules, local_modules)
    cfg.create(tree)

    cfg_list = [cfg]

    adaptor_type = FlaskAdaptor(cfg_list)

    analyse(cfg_list, analysis_type=ReachingDefinitionsTaintAnalysis)
    
    vulnerability_log = None
    if args.trigger_word_file:
        vulnerability_log = find_vulnerabilities(cfg_list, args.trigger_word_file)
    else:
        vulnerability_log = find_vulnerabilities(cfg_list)

    vulnerability_log.print_report()

    if args.draw_cfg:
        if args.output_filename:
            draw_cfg(cfg, args.output_filename)
        else:
            draw_cfg(cfg)
    if args.print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(e)
    if args.verbose_print:
        for i, e in enumerate(cfg_list):
            print('############## CFG number: ', i)
            print(repr(e))
    

    
