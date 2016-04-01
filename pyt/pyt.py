import argparse
from cfg import generate_ast, CFG
from draw import draw_cfg
from reaching_definitions import reaching_definitions_analysis
from fixed_point import fixed_point_analysis
import flask_engine
from vulnerability_log import Vulnerability, VulnerabilityLog

parser = argparse.ArgumentParser()

parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)
parser.add_argument('-d', '--draw-cfg', help = 'Draw CFG and output as .svg file.', action='store_true')
parser.add_argument('-o', '--output-filename', help = 'Output filename.', type = str)
parser.add_argument('-p', '--print', help = 'Prints the nodes of the CFG.', action='store_true')
parser.add_argument('-vp', '--verbose-print', help = 'Verbose printing of -p.', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':
    tree = generate_ast(args.filename)
    cfg = CFG()
    cfg.create(tree)

    analysis = fixed_point_analysis(reaching_definitions_analysis)
    analysis.fixpoint_runner(cfg)

    sources_and_sinks = flask_engine.identify_sources_and_sinks(cfg)
    
    vulnerability_log = VulnerabilityLog()
    flask_engine.find_vulnerabilities(sources_and_sinks[0], sources_and_sinks[1], vulnerability_log)
    

    if args.draw_cfg:
        if args.output_filename:
            draw_cfg(cfg, args.output_filename)
        else:
            draw_cfg(cfg)
    if args.print:
        print(cfg)
    if args.verbose_print:
        print(repr(cfg))
    

    
