import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node


class CFGTestCase(unittest.TestCase):
    def assertConnected(self, node, successor):
        '''Asserts that a node is connected to its successor.
        This means that node has successor in its outgoing and
        successor has node in its ingoing.'''

        self.assertIn(successor, node.outgoing,
                       '\n%s was NOT found in the outgoing list of %s containing: ' % (successor.label, node.label) + '[' + ', '.join([x.label for x in node.outgoing]) + ']')
        
        self.assertIn(node, successor.ingoing,
                       '\n%s was NOT found in the ingoing list of %s containing: ' % (node.label, successor.label) + '[' + ', '.join([x.label for x in successor.ingoing]) + ']')

    def assertNotConnected(self, node, successor):
        '''Asserts that a node is not connected to its successor.
        This means that node does not the successor in its outgoing and
        successor does not have the node in its ingoing.'''

        self.assertNotIn(successor, node.outgoing,
                       '\n%s was mistakenly found in the outgoing list of %s containing: ' % (successor.label, node.label) + '[' + ', '.join([x.label for x in node.outgoing]) + ']')
        
        self.assertNotIn(node, successor.ingoing,
                         '\n%s was mistakenly found in the ingoing list of %s containing: ' % (node.label, successor.label) + '[' + ', '.join([x.label for x in successor.ingoing]) + ']')

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

    def test_repr_cfg(self):
        print(repr(self.cfg))

    def test_str_cfg(self):
        print(self.cfg)

    def test_no_tuples(self):
        for node in self.cfg.nodes:
            for edge in node.outgoing + node.ingoing:
                self.assertIsInstance(edge, Node)
    
class CFGForTest(CFGTestCase):

    def test_for_complete(self):
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

        for_node = self.nodes['for x in range(3)']
        body_1 = self.nodes['print(x)']
        body_2 = self.nodes['y += 1']
        else_body_1 = self.nodes["print('Final: %s' % x)"]
        else_body_2 = self.nodes['print(y)']
        next_node = self.nodes['x = 3']

        self.assertConnected(else_body_2, next_node)
        self.assertConnected(else_body_1, else_body_2)
        self.assertConnected(for_node, else_body_1)
        self.assertConnected(body_1, body_2)
        self.assertConnected(for_node, body_1)
        self.assertConnected(body_2, for_node)

        #NOT IN
        self.assertNotConnected(body_2, else_body_1)
        self.assertNotConnected(body_2, next_node)

    def test_for_no_orelse(self):
        self.cfg = CFG()
        obj = parse(
'''
for x in range(3):
    print(x)
    y += 1
x = 3
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        for_node = self.nodes['for x in range(3)']
        body_1 = self.nodes['print(x)']
        body_2 = self.nodes['y += 1']
        next_node = self.nodes['x = 3']

        self.assertConnected(body_1, body_2)
        self.assertConnected(for_node, body_1)
        self.assertConnected(for_node, next_node)
        self.assertConnected(body_2, for_node)

        # NOT IN
        self.assertNotConnected(body_2, next_node)

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

        self.assertConnected(test, eliftest)
        self.assertConnected(test, body_1)
        self.assertConnected(body_1, body_2)
        self.assertConnected(body_2, next_stmt)

        self.assertNotConnected(body_2, eliftest)
        self.assertNotConnected(body_1, eliftest)
        
    def test_if_elif(self):
        test = self.nodes['x == 0']
        eliftest = self.nodes['x += 4'] # in this cas the elif is just a statement
        body_1 = self.nodes['x += 3']
        next_stmt = self.nodes['x += 5']

        self.assertConnected(test, eliftest)
        self.assertConnected(test, body_1)
        self.assertConnected(body_1, next_stmt)
        self.assertConnected(eliftest, next_stmt)


class CFGWhileTest(CFGTestCase):

    def test_while_complete(self):
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

        test = self.nodes['x > 0']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        else_body_1 = self.nodes['x += 3']
        else_body_2 = self.nodes['x += 4']
        next_stmt = self.nodes['x += 5']
        
        self.assertConnected(test, body_1)
        self.assertConnected(test, else_body_1)
        
        self.assertConnected(body_1, body_2)
        self.assertConnected(body_2, test)

        self.assertConnected(else_body_1, else_body_2)
        self.assertConnected(else_body_2, next_stmt)

        #NOT IN
        self.assertNotConnected(body_2, else_body_1)
        self.assertNotConnected(test, next_stmt)
        self.assertNotConnected(body_1, next_stmt)
        self.assertNotConnected(else_body_1, next_stmt)
        self.assertNotConnected(body_2, next_stmt)

    def test_while_no_orelse(self):
        self.cfg = CFG()
        obj = parse(
'''
while x > 0:
    x += 1
    x += 2
x += 5
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        test = self.nodes['x > 0']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        next_stmt = self.nodes['x += 5']
        
        self.assertConnected(test, body_1)
        self.assertConnected(test, next_stmt)
        
        self.assertConnected(body_1, body_2)
        self.assertConnected(body_2, test)

        #NOT IN
        self.assertNotConnected(body_1, next_stmt)
        self.assertNotConnected(body_1, test)
        self.assertNotConnected(test, body_2)
        self.assertNotConnected(body_2, body_1)
        self.assertNotConnected(body_2, next_stmt)

        
        
        
class CFGStartExitNodeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/simple.py')
        self.cfg.create(tree)

    def test_start(self):
        start_node = self.cfg.nodes[0]
        node = self.cfg.nodes[1]
        exit_node = self.cfg.nodes[-1]

        self.assertConnected(start_node, node)
        self.assertConnected(node, exit_node)

        self.assertEqual(start_node.ast_type, 'ENTRY')
        self.assertEqual(exit_node.ast_type, 'EXIT')


        
class CFGFunctionNodeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/function.py')
        self.cfg.create(tree)

    def test_function(self):
        self.assertEqual( len(self.cfg.functions), 3)

        print(self.cfg.functions['baz'][2])
        
