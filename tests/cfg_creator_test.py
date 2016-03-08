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

    def assertNotInOutgoing(self, a, b):
        '''Assert that a is in b.outgoing'''
        self.assertNotIn(a,b.outgoing)
        
    def cfg_list_to_dict(self, list):
        '''This method converts the CFG list to a dict, making it easier to find nodes to test.
        This method assumes that no nodes in the code have the same label'''
        return {x.label: x for x in list}
        
class CFG_if_test(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''
if x > 0:
    x += 1
    x += 2
elif x == 0:
    x += 3
else:
    x += 4
x += 5
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

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


class CFG_while_test(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''
while x > 0:
    x += 1
    x += 2
else:
    x += 3
    x += 4
x += 5
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

    def test_if_first_if(self):
        test = self.nodes['x > 0']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        else_body_1 = self.nodes['x += 3']
        else_body_2 = self.nodes['x += 4']
        next_stmt = self.nodes['x += 5']
        
        self.assertInOutgoing(body_1, test)
        self.assertInOutgoing(else_body_1, test)
        self.assertInOutgoing(next_stmt, test)
        
        self.assertInOutgoing(body_2, body_1)
        self.assertInOutgoing(test, body_2)
        self.assertInOutgoing(next_stmt, body_2)

        self.assertInOutgoing(else_body_2, else_body_1)
        self.assertInOutgoing(next_stmt, else_body_2)
        
