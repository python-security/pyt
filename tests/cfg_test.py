import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node


class CFGTestCase(unittest.TestCase):
    def assertInOutgoing(self, a, b):
        '''Assert that a is in b.outgoing'''
        self.assertIn(a,b.outgoing,
                      '\n%s was NOT found in the outgoing list of %s containing: ' % (a.label, b.label) + '[' + ', '.join([x.label for x in b.outgoing]) + ']')
        
    def assertNotInOutgoing(self, a, b):
        '''Assert that a is in b.outgoing'''
        self.assertNotIn(a,b.outgoing,
                         '\n%s was mistakenly found in the outgoing list containing: ' % a.label + '[' + ', '.join([x.label for x in b.outgoing]) + ']')
        
    def cfg_list_to_dict(self, list):
        '''This method converts the CFG list to a dict, making it easier to find nodes to test.
        This method assumes that no nodes in the code have the same label'''
        return {x.label: x for x in list}



class CFGGeneralTest(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''
for x in range(3):
    print(x)
    y += 1
else:
    print('Final: %s' % x)
    print(y)
x = 3
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

    def test_print_cfg(self):
        self.cfg.print()

    def test_no_tuples(self):
        for node in self.cfg.nodes:
            for edge in node.outgoing + node.ingoing:
                self.assertIsInstance(edge, Node)
    
class CFGForTest(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''
for x in range(3):
    print(x)
    y += 1
else:
    print('Final: %s' % x)
    print(y)
x = 3
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)


    def test_for(self):
        for_node = self.nodes['for x in range(3)']
        body_1 = self.nodes['print(x)']
        body_2 = self.nodes['y += 1']
        else_body_1 = self.nodes["print('Final: %s' % x)"]
        else_body_2 = self.nodes['print(y)']
        next_node = self.nodes['x = 3']

        self.assertInOutgoing(next_node, else_body_2)
        self.assertInOutgoing(else_body_2, else_body_1)
        self.assertInOutgoing(else_body_1, for_node)
        self.assertInOutgoing(else_body_1, body_2)
        self.assertInOutgoing(body_2, body_1)
        self.assertInOutgoing(body_1, for_node)
        self.assertInOutgoing(for_node, body_2)
    
class CFGIfTest(CFGTestCase):

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

        self.assertNotInOutgoing(eliftest, body_2)
        self.assertNotInOutgoing(eliftest, body_1)
        
    def test_if_elif(self):
        test = self.nodes['x == 0']
        eliftest = self.nodes['x += 4'] # in this cas the elif is just a statement
        body_1 = self.nodes['x += 3']
        next_stmt = self.nodes['x += 5']

        self.assertInOutgoing(eliftest,test)
        self.assertInOutgoing(body_1, test)
        self.assertInOutgoing(next_stmt, body_1)
        self.assertInOutgoing(next_stmt, eliftest)


class CFGWhileTest(CFGTestCase):

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

    def test_while(self):
        test = self.nodes['x > 0']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        else_body_1 = self.nodes['x += 3']
        else_body_2 = self.nodes['x += 4']
        next_stmt = self.nodes['x += 5']
        
        self.assertInOutgoing(body_1, test)
        self.assertInOutgoing(else_body_1, test)
        
        self.assertInOutgoing(body_2, body_1)
        self.assertInOutgoing(test, body_2)
        self.assertInOutgoing(next_stmt, body_2)
        self.assertInOutgoing(else_body_1, body_2)

        self.assertInOutgoing(else_body_2, else_body_1)
        self.assertInOutgoing(next_stmt, else_body_2)

        #NOT IN
        self.assertNotInOutgoing(next_stmt, test)
        self.assertNotInOutgoing(next_stmt, body_1)
        self.assertNotInOutgoing(next_stmt, else_body_1)

        
class CFGStartExitNodeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/simple.py')
        self.cfg.create(tree)

    def test_start(self):
        start_node = self.cfg.nodes[0]
        node = self.cfg.nodes[1]
        exit_node = self.cfg.nodes[-1]

        self.assertInOutgoing(node, start_node)
        self.assertInOutgoing(exit_node, node)

        self.assertEqual(start_node.ast_type, 'START')
        self.assertEqual(exit_node.ast_type, 'EXIT')
