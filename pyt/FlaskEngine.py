import os
from cfg import CFG, generate_ast, Node

file = ""


cfg = CFG()
tree = generate_ast("XSS.py")
cfg.create(tree)

print(cfg)

for func in cfg.functions.values():
    print(func.nodes)
