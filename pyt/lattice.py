from cfg import AssignmentNode


class Lattice:

    def __init__(self, cfg_nodes, analysis_type):
        self.d = dict()
        self.l = list()
        for i, e in enumerate(analysis_type.get_lattice_elements(cfg_nodes)):
            self.d[e] = 0b1 << i
            self.l.append(e)
        self.l = list(reversed(self.l))
        self.table = dict()

        LatticeElement.__eq__ = analysis_type.equality
        for node in cfg_nodes:
            self.table[node] = LatticeElement(0b0)

    def meet(self, iterable1, iterable2):
        r1 = self.constraint_join(iterable1)
        r2 = self.constraint_join(iterable2)
        return r1 & r2

    def simple_meet(self, iterable):
        r = self.d[iterable[0]]
        for e in iterable:
            r = r & self.table[e]
        return r

    def constraint_meet(self, iterable):
        r = self.d[iterable[0]]
        for e in iterable:
            r = r & self.table[e]
        return r

    def join(self, iterable1, iterable2):
        r1 = self.constraint_join(iterable1)
        r2 = self.constraint_join(iterable2)
        return r1 | r2

    def simple_join(self, iterable):
        r = 0
        for e in iterable:
            r = r | self.d[e]
        return r

    def constraint_join(self, iterable):
        r = 0
        for e in iterable:
            r = r | self.table[e]
        return r

    def get_elements(self, number):
        r = list()

        if number == 0:
            return r

        for i, x in enumerate(format(number, '0' + str(len(self.l)) + 'b')):
            if x == '1':
                r.append(self.l[i])
        return r

    def has_element(self, node1, node2):
        """Checks if node1 is in node2's constraints
        For instance node1 = 010 and node2 = 110:
        010 & 110 = 010 -> has the element."""
        constraint = self.table[node2]

        try:
            value = self.d[node1] #if node1 in self.d else 0b0
        except KeyError:
            value = 0b0

        if constraint == 0b0 or value == 0b0:
            return False

        return constraint & value != 0

    def __getitem__(self, key):
        try:
            return self.table[key]
        except KeyError:
            print('KeyError FUCK')
            return None

class LatticeElement:
    def __init__(self, value):
        self.value = value

class ConstraintTable:
    def __init__(self, elements):
        self.table = dict.fromkeys(elements, 0b0)
    def __getitem__(self, key):
        return self.table[key]
        
def generate_lattices(cfg_list, *, analysis_type):
    lattices = list()
    for cfg in cfg_list:
        lattices.append(Lattice(cfg.nodes, analysis_type))
    return lattices


if __name__ == '__main__':
    from sys import getsizeof as gso
    l = Lattice(['a', 'b', 'c']) # Consider duplicates
    print(l.d['a'])
    print(bin(l.join(['a'], ['b'])))
    print(l.d)
    print([bin(x) for x in l.d.values()])
    print(bin(l.meet(['a', 'b'], ['b', 'c'])))
    print(l.l)
    print(l.get_elements(4))
    input()
    l = Lattice([*range(10000)])
    print(gso(l.d)/1000000, 'mb')
    print(gso(l.l)/1000000, 'mb')
