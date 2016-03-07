import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
from ast import parse

from pyt.cfg import CFG, print_CFG

class CFGTestCase(unittest.TestCase):
    def assertInOutgoing(self, a, b):
        '''Assert that a is in b.outgoing'''
        self.assertIn(a,b.outgoing)
        
class CFG_if_test(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse('if x > 0:\n\tx += 1\n\tx+=2\nelif x==0:\n\tx+=3\nelse:\n\tx+=4\nx+=5')
        self.cfg.create(obj)
        self.nodes = self.cfg.nodes

    def test_if_first_if(self):
        test = self.nodes['x > 0']
        eliftest = self.nodes['x == 0']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        next_stmt = self.nodes['x += 5']
        
        self.assertInOutgoing(eliftest, test)
        self.assertInOutgoing(body_1, test)
        self.assertInOutgoing(body_2, body_1)
        self.assertInOutgoing(next_stmt, body_2)
        
    def test_if_elif(self):
        test = self.nodes['x == 0']
        eliftest = self.nodes['x += 4'] # in this cas the elif is just a statement
        body_1 = self.nodes['x += 3']
        next_stmt = self.nodes['x += 5']

        self.assertInOutgoing(eliftest,test)
        self.assertInOutgoing(body_1, test)
        self.assertInOutgoing(next_stmt, body_1)
        self.assertInOutgoing(next_stmt, eliftest)
        
        
