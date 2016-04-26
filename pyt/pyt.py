import argparse
import os

from cfg import generate_ast, CFG
from draw import draw_cfg
from reaching_definitions import ReachingDefinitionsAnalysis
from fixed_point import analyse
from flask_engine import FlaskEngine


parser = argparse.ArgumentParser()

parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)
parser.add_argument('-d', '--draw-cfg', help = 'Draw CFG and output as .svg file.', action='store_true')
parser.add_argument('-o', '--output-filename', help = 'Output filename.', type = str)
parser.add_argument('-p', '--print', help = 'Prints the nodes of the CFG.', action='store_true')
parser.add_argument('-vp', '--verbose-print', help = 'Verbose printing of -p.', action='store_true')
parser.add_argument('-t', '--trigger-word-file', help='Input trigger word file.', type=str)

args = parser.parse_args()

if __name__ == '__main__':
    tree = generate_ast(args.filename)
    cfg = CFG()
    cfg.create(tree)

    cfg_list = [cfg]

    engine_type = None
    if args.trigger_word_file:
        engine_type = FlaskEngine(cfg_list, args.trigger_word_file)
    else:
        engine_type = FlaskEngine(cfg_list) 

    analyse(cfg_list, analysis_type=ReachingDefinitionsAnalysis)
    
    vulnerability_log = engine_type.find_vulnerabilities()
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
    

    
