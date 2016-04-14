import argparse
import os

from cfg import generate_ast, CFG
from draw import draw_cfg
from reaching_definitions import ReachingDefinitionsAnalysis
from fixed_point import analyse
import flask_engine


default_trigger_word_file = os.path.join('pyt', 'trigger_definitions', 'flask_trigger_words.pyt')

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
    cfg_list.extend(flask_engine.find_flask_route_functions(cfg.functions))

    analyse(cfg_list, analysis_type=ReachingDefinitionsAnalysis)

    trigger_word_file = default_trigger_word_file
    if args.trigger_word_file:
        trigger_word_file = args.trigger_word_file

    vulnerability_log = flask_engine.find_vulnerabilities(cfg_list, trigger_word_file)
    vulnerability_log.print_report()

    if args.draw_cfg:
        if args.output_filename:
            draw_cfg(cfg, args.output_filename)
        else:
            draw_cfg(cfg)
    if args.print:
        print(cfg)
    if args.verbose_print:
        print(repr(cfg))
    

    
