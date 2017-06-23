from .constraint_table import constraint_table
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


class Lattice:
    def __init__(self, cfg_nodes, analysis_type):
        self.el2bv = dict()  # Element to bitvector dictionary
        self.bv2el = list()  # Bitvector to element list
        for i, e in enumerate(analysis_type.get_lattice_elements(cfg_nodes)):
            self.el2bv[e] = 0b1 << i
            self.bv2el.append(e)
        self.bv2el = list(reversed(self.bv2el))

    def get_elements(self, number):
        r = list()

        if number == 0:
            return r

        # Turn number into a binary string of length len(self.bv2el)
        for i, x in enumerate(format(number,
                                     '0' + str(len(self.bv2el)) + 'b')):
            if x == '1':
                r.append(self.bv2el[i])
        return r

    def in_constraint(self, node1, node2):
        """Checks if node1 is in node2's constraints
        For instance, if node1 = 010 and node2 = 110:
        010 & 110 = 010 -> has the element."""
        constraint = constraint_table[node2]

        try:
            value = self.el2bv[node1]
        except KeyError:
            value = 0b0

        if constraint == 0b0 or value == 0b0:
            return False

        logger.debug("constraint is %s", bin(constraint))
        logger.debug("value is %s", value)
        return constraint & value != 0


def print_lattice(cfg_list, analysis_type):
    """
        Type of params is...?
    """
    nodes = list()
    for cfg in cfg_list:
        nodes.extend(cfg.nodes)
    l = Lattice(nodes, analysis_type)

    print('Lattice:')
    for k, v in l.el2bv.items():
        print(str(k) + ': ' + str(v))
    return l
