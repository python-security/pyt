import sys
import os

from base_test_case import BaseTestCase
sys.path.insert(0, os.path.abspath('../pyt'))
from lattice import Lattice, LatticeElement, subset_relation

class LatticeTest(BaseTestCase):

    def is_lattice_element_equal(self, e1, e2):
        for x in range(len(e1)):
            if e1.elements[x] != e2.elements[x]:
                return False
        return True

    def same_elements(self, l1, l2):
        for x in range(len(l1)):
            if not self.is_lattice_element_equal(l1[x], l2[x]):
                return False
        return True

    def test_generate_integer_elements(self):
        lattice = Lattice([1,2,3], subset_relation)

        elements = list()
        for i in [(), tuple([1]), tuple([2]), tuple([3]), (1,2), (1,3), (2,3), (1,2,3)]:
            elements.append(LatticeElement(i))

        self.assertEqual(self.same_elements(lattice.elements, elements), True)

    def test_generate_string_elements(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)

        elements = list()
        for i in [(), tuple([a]), tuple([b]), tuple([c]), (a,b), (a,c), (b,c), (a,b,c)]:
            elements.append(LatticeElement(i))

        self.assertEqual(self.same_elements(lattice.elements, elements), True)

    def test_join(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)
        self.assertEqual(self.is_lattice_element_equal(lattice.join(LatticeElement([a]), LatticeElement([b])), LatticeElement((a, b))), True)

    def test_meet1(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)
        self.assertEqual(self.is_lattice_element_equal(lattice.meet(LatticeElement([a,b]), LatticeElement([b,c])), LatticeElement([b])), True)

    def test_meet2(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)
        self.assertEqual(self.is_lattice_element_equal(lattice.meet(LatticeElement([a,b]), LatticeElement([a,b,c])), LatticeElement([a, b])), True)

    def test_largest_element(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)
        self.assertEqual(self.is_lattice_element_equal(lattice.largest_element(), LatticeElement([a,b,c])), True)

    def test_smallest_element(self):
        a = 'x = 1'
        b = 'y = 2'
        c = 'x = y'
        lattice = Lattice([a, b, c], subset_relation)
        self.assertEqual(self.is_lattice_element_equal(lattice.smallest_element(), LatticeElement([])), True)
