import os
import sys
import unittest
from ast import parse

sys.path.insert(0, os.path.abspath('../pyt'))
from cfg import CFG, generate_ast, Node


class CFGTestCase(unittest.TestCase):
    def assertInCfg(self, connections):
        ''' Assert that all connections in the connections list exists in the cfg,
        as well as all connections not in the list do not exist

        connections is a list of tuples where the node at index 0 of the tuple has to be in the new_constraintset of the node a index 1 of the tuple'''
        for connection in connections:
            self.assertIn(self.cfg.nodes[connection[0]], self.cfg.nodes[connection[1]].outgoing, str(connection) + " expected to be connected")
            self.assertIn(self.cfg.nodes[connection[1]], self.cfg.nodes[connection[0]].ingoing, str(connection) + " expected to be connected")

        nodes = len(self.cfg.nodes)

        for element in range(nodes):
            for sets in range(nodes):
                if not (element, sets) in connections or (sets, element) in connections:
                    self.assertNotIn(self.cfg.nodes[element], self.cfg.nodes[sets].outgoing, "(%s,%s)" % (element, sets)  +  " expected to be disconnected")
                    self.assertNotIn(self.cfg.nodes[sets], self.cfg.nodes[element].ingoing, "(%s,%s)" % (sets, element)  +  " expected to be disconnected")

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

class CFGAssignmentMultiTargetTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/assignment_two_targets.py')
        self.cfg.create(tree)

    def test_start(self):
        start_node = self.cfg.nodes[0]
        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertConnected(start_node, node)
        self.assertConnected(node_2, exit_node)
        self.assertConnected(node, node_2)

        self.assertEqual(start_node.ast_type, 'ENTRY')
        self.assertEqual(exit_node.ast_type, 'EXIT')
        
        
class CFGFunctionNodeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/simple_function.py')
        self.cfg.create(tree)

    def connected(self, node, successor):
        return (successor, node)

    def test_function(self):
        entry = 0
        y_assignment = 1
        save_y = 2
        entry_foo = 3
        body_foo = 4
        exit_foo = 5
        y_load = 6
        exit_ = 7

        self.assertInCfg([self.connected(entry, y_assignment), self.connected(y_assignment, save_y),
                          self.connected(save_y, entry_foo), self.connected(entry_foo, body_foo),
                          self.connected(body_foo, exit_foo), self.connected(exit_foo, y_load),
                          self.connected(y_load, exit_)])

class CFGFunctionParameterNodeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/parameters_function.py')
        self.cfg.create(tree)

    def connected(self, node, successor):
        return (successor, node)

    def test_function(self):
        entry = 0
        y_assignment = 1
        save_y = 2
        save_actual_y = 3
        bar_local_y = 4
        entry_bar = 5
        bar_y_assignment = 6
        bar_print_y = 7
        bar_print_x = 8
        exit_bar = 9
        restore_actual_y = 10
        exit_ = 11

        self.assertInCfg([self.connected(entry, y_assignment), self.connected(y_assignment, save_y),
                          self.connected(save_y, save_actual_y), self.connected(save_actual_y, bar_local_y),
                          self.connected(bar_local_y, entry_bar), self.connected(entry_bar, bar_y_assignment),
                          self.connected(bar_y_assignment, bar_print_y), self.connected(bar_print_y, bar_print_x),
                          self.connected(bar_print_x, exit_bar), self.connected(exit_bar, restore_actual_y),
                          self.connected(restore_actual_y, exit_)])
        
class CFGFunctionNodeWithReturnTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/simple_function_with_return.py')
        self.cfg.create(tree)

    def connected(self, node, successor):
        return (successor, node)

    def test_function(self):
        '''
Node: 1 Label:  y = input()

Node: 2 Label:  save_1_y = y

Node: 3 Label:  Entry node: foo

Node: 4 Label:  print('h')

Node: 5 Label:  ret_foo = 1

Node: 6 Label:  Exit node: foo

Node: 7 Label:  y = save_1_y

Node: 8 Label:  call_1 = ret_foo

Node: 9 Label:  save_2_y = y

Node: 10 Label:  Entry node: bar

Node: 11 Label:  x = 2

Node: 12 Label:  ret_bar = x

Node: 13 Label:  Exit node: bar

Node: 14 Label:  y = save_2_y

Node: 15 Label:  call_2 = ret_bar

Node: 16 Label:  x = call_2

Node: 17 Label:  Exit node
'''
        print(repr(self.cfg))

        l = zip(range(1, len(self.cfg.nodes)), range(len(self.cfg.nodes)))
        for x,y in l:
            print(x,y)
                       
        self.assertInCfg(l)


class CFGAssignmentAndBuiltinTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/assignmentandbuiltin.py')
        self.cfg.create(tree)

    def test_start(self):
        start_node = self.cfg.nodes[0]
        assign = self.cfg.nodes[1]
        builtin = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertConnected(start_node, assign)
        self.assertConnected(assign, builtin)
        self.assertConnected(builtin, exit_node)
