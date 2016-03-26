import argparse
from cfg import generate_ast, CFG

parser = argparse.ArgumentParser()

parser.add_argument('filename', help = 'Filename of the file that should be analysed.', type = str)
parser.add_argument('-d', '--draw-cfg', help = 'Draw CFG and output as .svg file.', action='store_true')
parser.add_argument('-p', '--print', help = 'Prints the nodes of the CFG.', action='store_true')
parser.add_argument('-vp', '--verbose-print', help = 'Prints the nodes of the CFG verbosely.', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':
    tree = generate_ast(args.filename)
    cfg = CFG()
    cfg.create(tree)

    if args.draw_cfg:
        pass
    if args.print:
        print(cfg)
    if args.verbose_print:
        print(repr(cfg))
    
