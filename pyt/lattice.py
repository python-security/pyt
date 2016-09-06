from constraint_table import constraint_table
class Lattice:

    def __init__(self, cfg_nodes, analysis_type):
        self.el2bv = dict() # Element to bitvector dictionary
        self.bv2el = list() # Bitvector to element list
        for i, e in enumerate(analysis_type.get_lattice_elements(cfg_nodes)):
            self.el2bv[e] = 0b1 << i
            self.bv2el.append(e)
        self.bv2el = list(reversed(self.bv2el))

        LatticeElement.__eq__ = analysis_type.equality

    def get_elements(self, number):
        r = list()

        if number == 0:
            return r

        for i, x in enumerate(format(number, '0' + str(len(self.bv2el)) + 'b')):
            if x == '1':
                r.append(self.bv2el[i])
        return r

    def in_constraint(self, node1, node2):
        """Checks if node1 is in node2's constraints
        For instance node1 = 010 and node2 = 110:
        010 & 110 = 010 -> has the element."""
        constraint = constraint_table[node2]

        try:
            value = self.el2bv[node1]
        except KeyError:
            value = 0b0

        if constraint == 0b0 or value == 0b0:
            return False

        return constraint & value != 0

class LatticeElement:
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        raise Eception('This must be implemented by the analysis.')

    def __or__(self, value):
        return self.value | value

    def __ror__(self, value):
        return value | self.value

    def __and__(self, value):
        return self.value & value

    def __rand__(self, value):
        return value & self.value

    def __lshift__(self, value):
        return self.value << value

    def __rshift__(self, value):
        return self.value >> value

    def __rlshift__(self, value):
        return value << self.value

    def __rrshift__(self, value):
        return value >> self.value

    def __xor__(self, value):
        return self.value ^ value

    def __rxor__(self, value):
        return value ^ self.value

    def __str__(self):
        return str(self.value)
