"""This module implements a lattice to use with static analysis."""
from itertools import combinations

class Lattice:
    def __init__(self, elements, relation):
        self.elements = elements # Should be a set as a lattice is a partial order
        self.relation = relation
        self.generate_elements()

    def generate_elements(self):
        l = list()
        for x in range(0, len(self.elements)+1):
            for e in combinations(self.elements, x):
                l.append(LatticeElement(e))
        self.elements = l

    def join(self, e1, e2): # least upper bound
        #Save upper bound on lattice element - speed over memory?
        e1_upper_bounds = list()
        e2_upper_bounds = list()
        for e in self.elements:
            if self.relation(e1, e):
                e1_upper_bounds.append(e)
            if self.relation(e2, e):
                e2_upper_bounds.append(e)
        #print([str(e) for e  in e1_upper_bounds])
        #print([str(e) for e  in e2_upper_bounds])
        common_upper_bounds = set(e1_upper_bounds).intersection(e2_upper_bounds)
        return min(common_upper_bounds, key=len)

    def meet(self, e1, e2): # least upper bound
        #Save lower bound on lattice element - speed over memory?
        e1_lower_bounds = list()
        e2_lower_bounds = list()
        for e in self.elements:
            if self.relation(e, e1):
                e1_lower_bounds.append(e)
            if self.relation(e, e2):
                e2_lower_bounds.append(e)
        #print([str(e) for e  in e1_lower_bounds])
        #print([str(e) for e  in e2_lower_bounds])
        common_lower_bounds = set(e1_lower_bounds).intersection(e2_lower_bounds)
        return max(common_lower_bounds, key=len)
    
    def smallest_element(self):
        return min(self.elements, key=len)

    def largest_element(self):
        return max(self.elements, key=len)

    def __str__(self):
        return ', '.join([str(e) for e in self.elements])

    def __iter__(self):
        return iter(self.elements)

class LatticeElement:
    def __init__(self, elements):
        self.elements = elements
        # Questionable:
        self.upper_bounds = None 
        self.lower_bounds = None
        self.least_upper_bound = None
        self.greatest_lower_bound = None

    def __str__(self):
        return '{' + ', '.join([str(e) for e in self.elements]) + '}'

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return iter(self.elements)


def subset_relation(e1, e2):
    return set(e1.elements).issubset(set(e2.elements))

if __name__ == '__main__':
    l = Lattice([1,2,3,4], subset_relation)
    print(l)
    print(l.join(LatticeElement([1, 2]), LatticeElement([2, 3])))
    print(l.meet(LatticeElement([1, 2]), LatticeElement([2, 3])))
    print(l.smallest_element())
    print(l.largest_element())

    l = Lattice(['x = 1', 'x = x + 1', 'y = 3', 'y = z'], subset_relation)
    print(l)
    print(l.join(LatticeElement(['x = 1', 'y = z']), LatticeElement(['x = 1', 'y = 3'])))
    print(l.meet(LatticeElement(['x = 1', 'y = z']), LatticeElement(['x = 1', 'y = 3'])))
    print(l.smallest_element())
    print(l.largest_element())
