import sys
import os

from base_test_case import BaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from lattice import Lattice

class LatticeTest(BaseTestCase):

    def test_generate_integer_elements(self):
        lattice = Lattice([1,2,3], ['a', 'b', 'c'])

        self.assertEqual(lattice.d[1], 0b1)
        self.assertEqual(lattice.d[2], 0b10)
        self.assertEqual(lattice.d[3], 0b100)

        self.assertEqual(lattice.table['a'], 0b0)
        self.assertEqual(lattice.table['b'], 0b0)
        self.assertEqual(lattice.table['c'], 0b0)

        self.assertEqual(lattice.l[0], 3)
        self.assertEqual(lattice.l[1], 2)
        self.assertEqual(lattice.l[2], 1)

    def test_join(self):
        a = 'x = 1'
        b = 'print(x)'
        c = 'x = 3'
        d = 'y = x'
        
        lattice = Lattice([a, c, d], [a, b, c, d])

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
        a = 'x = 1'
        b = 'print(x)'
        c = 'x = 3'
        d = 'y = x'
        
        lattice = Lattice([a, c, d], [a, b, c, d])

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
        a = 'x = 1'
        b = 'print(x)'
        c = 'x = 3'
        d = 'y = x'
        
        lattice = Lattice([a, c, d], [a, b, c, d])
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
        a = 'x = 1'
        b = 'print(x)'
        c = 'x = 3'
        d = 'y = x'
        
        lattice = Lattice([a, c, d], [a, b, c, d])

        self.assertEqual(set(lattice.get_elements(0b111)), {a,c,d})
        self.assertEqual(set(lattice.get_elements(0b0)), set())
        self.assertEqual(set(lattice.get_elements(0b1)), {a})
        self.assertEqual(set(lattice.get_elements(0b10)), {c})
        self.assertEqual(set(lattice.get_elements(0b100)), {d})
        self.assertEqual(set(lattice.get_elements(0b11)), {a,c})
        self.assertEqual(set(lattice.get_elements(0b101)), {a,d})
        self.assertEqual(set(lattice.get_elements(0b110)), {c,d})
