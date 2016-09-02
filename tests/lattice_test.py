import sys
import os

from base_test_case import BaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from lattice import Lattice
from reaching_definitions_taint import ReachingDefinitionsTaintAnalysis

class LatticeTest(BaseTestCase):

    class AnalysisType:
        @staticmethod
        def get_lattice_elements(cfg_nodes):
            for node in cfg_nodes:
                if node.lattice_element == True:
                    yield node
        def equality(self, value):
            return self.value == value

    class Node:
        def __init__(self, value, lattice_element):
            self.value = value
            self.lattice_element = lattice_element
        def __str__(self):
            return str(self.value)
            
    def test_generate_integer_elements(self):
        one = self.Node(1, True)
        two = self.Node(2, True)
        three = self.Node(3, True)
        a = self.Node('a', False)
        b = self.Node('b', False)
        c = self.Node('c', False)
        cfg_nodes = [one, two, three, a, b, c]
        lattice = Lattice(cfg_nodes, self.AnalysisType)

        self.assertEqual(lattice.d[one], 0b1)
        self.assertEqual(lattice.d[two], 0b10)
        self.assertEqual(lattice.d[three], 0b100)

        self.assertEqual(lattice.table[a], 0b0)
        self.assertEqual(lattice.table[b], 0b0)
        self.assertEqual(lattice.table[c], 0b0)

        self.assertEqual(lattice.l[0], three)
        self.assertEqual(lattice.l[1], two)
        self.assertEqual(lattice.l[2], one)

    def test_join(self):
        a = self.Node('x = 1', True)
        b = self.Node('print(x)', False)
        c = self.Node('x = 3', True)
        d = self.Node('y = x', True)
        
        lattice = Lattice([a, c, d], self.AnalysisType)

        # Constraint results after fixpoint:
        lattice.table[a] = 0b0001
        lattice.table[b] = 0b0001
        lattice.table[c] = 0b0010
        lattice.table[d] = 0b1010

        r = lattice.join([a,c], [c])
        self.assertEqual(r, 0b11)
        r = lattice.join([a, c], [d, c])
        self.assertEqual(r, 0b1011)
        r = lattice.join([a], [c])
        self.assertEqual(r, 0b11)
        r = lattice.join([c], [d])
        self.assertEqual(r, 0b1010)
        r = lattice.join([], [a])
        self.assertEqual(r, 0b1)
        r = lattice.join([a,c,d], [a,c,d])
        self.assertEqual(r, 0b1011)
        r = lattice.join([d,c], [])
        self.assertEqual(r, 0b1010)

    def test_meet(self):
        a = self.Node('x = 1', True)
        b = self.Node('print(x)', False)
        c = self.Node('x = 3', True)
        d = self.Node('y = x', True)
        
        lattice = Lattice([a, c, d], self.AnalysisType)

        # Constraint results after fixpoint:
        lattice.table[a] = 0b0001
        lattice.table[b] = 0b0001
        lattice.table[c] = 0b0010
        lattice.table[d] = 0b1010

        r = lattice.meet([a,c], [c,d])
        self.assertEqual(r, 0b10)
        r = lattice.meet([a], [d])
        self.assertEqual(r, 0b0)
        r = lattice.meet([a,c,d], [a,c])
        self.assertEqual(r, 0b011)
        r = lattice.meet([c,d], [a,d])
        self.assertEqual(r, 0b1010)
        r = lattice.meet([], [])
        self.assertEqual(r, 0b0)
        r = lattice.meet([a], [])
        self.assertEqual(r, 0b0)

    def test_has_element(self):
        a = self.Node('x = 1', True)
        b = self.Node('print(x)', False)
        c = self.Node('x = 3', True)
        d = self.Node('y = x', True)
        
        lattice = Lattice([a, c, d], self.AnalysisType)

        lattice.table[a] = 0b001
        lattice.table[b] = 0b001
        lattice.table[c] = 0b010
        lattice.table[d] = 0b110

        self.assertEqual(lattice.has_element(a, b), True)
        self.assertEqual(lattice.has_element(a, a), True)
        self.assertEqual(lattice.has_element(a, d), False)
        self.assertEqual(lattice.has_element(a, c), False)
        self.assertEqual(lattice.has_element(c, d), True)
        self.assertEqual(lattice.has_element(d, d), True)
        self.assertEqual(lattice.has_element(c, c), True)
        self.assertEqual(lattice.has_element(c, a), False)
        self.assertEqual(lattice.has_element(c, b), False)

    def test_get_elements(self):
        a = self.Node('x = 1', True)
        b = self.Node('print(x)', False)
        c = self.Node('x = 3', True)
        d = self.Node('y = x', True)
        
        lattice = Lattice([a, c, d], self.AnalysisType)

        self.assertEqual(set(lattice.get_elements(0b111)), {a,c,d})
        self.assertEqual(set(lattice.get_elements(0b0)), set())
        self.assertEqual(set(lattice.get_elements(0b1)), {a})
        self.assertEqual(set(lattice.get_elements(0b10)), {c})
        self.assertEqual(set(lattice.get_elements(0b100)), {d})
        self.assertEqual(set(lattice.get_elements(0b11)), {a,c})
        self.assertEqual(set(lattice.get_elements(0b101)), {a,d})
        self.assertEqual(set(lattice.get_elements(0b110)), {c,d})
