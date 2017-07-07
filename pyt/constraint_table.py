"""Global lookup table for constraints.

Uses cfg node as key and operates on bitvectors in the form of ints."""

constraint_table = dict()
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


def initialize_constraint_table(cfg_list):
    """Collects all given cfg nodes and initializes the table with value 0."""
    for cfg in cfg_list:
        logger.debug("len(cfg.nodes) is %s", len(cfg.nodes))
        constraint_table.update(dict.fromkeys(cfg.nodes, 0))


def constraint_join(cfg_nodes):
    """Looks up all cfg_nodes and joins the bitvectors by using logical or."""
    r = 0
    for e in cfg_nodes:
        logger.debug("len(cfg_nodes) is %s", len(cfg_nodes))
        logger.debug("e is %s", e)
        logger.debug("type(e) is %s", type(e))
        r = r | constraint_table[e]
    return r


def constraint_meet(self, cfg_nodes):
    """Finds the meet by looking up all given cfg nodes
    and performing logical and."""
    r = 0
    for i in range(len(cfg_nodes)):
        r = r | (0b1 << i)

    for e in cfg_nodes:
        r = r & constraint_table[e]
    return r


def print_table(l):
    print('Constraint table:')
    for k, v in constraint_table.items():
        print(str(k) + ': ' + ','.join([str(n) for n in l.get_elements(v)]))
