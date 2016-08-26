from cfg import AssignmentNode


class Lattice:

    def __init__(self, elements):
        self.d = dict()
        self.l = list()
        for i, e in enumerate(elements):
            self.d[e] = 0b1 << i
            self.l.append(e)
        self.l = list(reversed(self.l))

    def meet(self, iterable1, iterable2):
        r1 = self.simple_join(iterable1)
        r2 = self.simple_join(iterable2)
        return r1 & r2

    def simple_meet(self, iterable):
        r = self.d[iterable[0]]
        for e in iterable:
            r = r & self.d[e]
        return r
    
    def join(self, iterable1, iterable2):
        r1 = self.simple_join(iterable1)
        r2 = self.simple_join(iterable2)
        return r1 | r2

    def simple_join(self, iterable):
        r = 0
        for e in iterable:
            r = r | self.d[e]
        return r

    def get_elements(self, number):
        r = list()

        if number == 0:
            return r

        for i, x in enumerate(bin(number)[2:]):
            if x == '1':
                r.append(self.l[i])
        return r

    def __getitem__(self, key):
        return self.d[key]


def generate_lattices(cfg_list):
    lattices = list()
    for cfg in cfg_list:
        lattices.append(Lattice(node for node in cfg.nodes if isinstance(node, AssignmentNode)))
    return lattices

if __name__ == '__main__':
    from sys import getsizeof as gso
    l = Lattice(['a', 'b', 'c']) # Consider duplicates
    print(l['a'])
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
