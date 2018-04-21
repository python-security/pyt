"""Global lookup table for constraints.

Uses cfg node as key and operates on bitvectors in the form of ints."""

constraint_table = dict()


def initialize_constraint_table(cfg_list):
    """Collects all given cfg nodes and initializes the table with value 0."""
    for cfg in cfg_list:
        constraint_table.update(dict.fromkeys(cfg.nodes, 0))


def constraint_join(cfg_nodes):
    """Looks up all cfg_nodes and joins the bitvectors by using logical or."""
    r = 0
    for e in cfg_nodes:
        r = r | constraint_table[e]
    return r
