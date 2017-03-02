from ..pyt.cfg import CFG, print_CFG, generate_ast


ast = generate_ast('example_inputs/example.py')

cfg = CFG()
cfg.create(ast)

print_CFG(cfg)

