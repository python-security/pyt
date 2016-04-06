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
                if not (element, sets) in connections:
                    self.assertNotIn(self.cfg.nodes[element], self.cfg.nodes[sets].outgoing, "(%s <- %s)" % (element, sets)  +  " expected to be disconnected")
                    self.assertNotIn(self.cfg.nodes[sets], self.cfg.nodes[element].ingoing, "(%s <- %s)" % (sets, element)  +  " expected to be disconnected")

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

    def assertLineNumber(self, node, line_number):
        self.assertEqual(node.line_number, line_number)

    def cfg_list_to_dict(self, list):
        '''This method converts the CFG list to a dict, making it easier to find nodes to test.
        This method assumes that no nodes in the code have the same label'''
        return {x.label: x for x in list}

    def assert_length(self, _list, *, expected_length):
        actual_length = len(_list)
        self.assertEqual(expected_length, actual_length)


class CFGGeneralTest(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''\
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
'''\
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
        self.assert_length(self.cfg.nodes, expected_length=8)
        
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        for_node = self.nodes['for x in range(3):']
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
'''\
for x in range(3):
    print(x)
    y += 1
x = 3
'''
)
        self.cfg.create(obj)
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=6)

        for_node = self.nodes['for x in range(3):']
        body_1 = self.nodes['print(x)']
        body_2 = self.nodes['y += 1']
        next_node = self.nodes['x = 3']

        self.assertConnected(body_1, body_2)
        self.assertConnected(for_node, body_1)
        self.assertConnected(for_node, next_node)
        self.assertConnected(body_2, for_node)

        # NOT IN
        self.assertNotConnected(body_2, next_node)

    def test_for_tuple_target(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/for_tuple_target.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length = 4)

        entry_node = 0
        for_node = 1
        print_node = 2
        exit_node = 3

        print(repr(self.cfg))
        
        self.assertInCfg([(for_node,entry_node),(print_node,for_node),(for_node,print_node),(exit_node,for_node)])
        self.assertEqual(self.cfg.nodes[for_node].label, "for (x, y) in [(1, 2), (3, 4)]:")

    def test_for_line_numbers(self):
        self.cfg = CFG()
        obj = parse(
'''\
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
        self.assert_length(self.cfg.nodes, expected_length=8)
        
        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        for_node = self.nodes['for x in range(3):']
        body_1 = self.nodes['print(x)']
        body_2 = self.nodes['y += 1']
        else_body_1 = self.nodes["print('Final: %s' % x)"]
        else_body_2 = self.nodes['print(y)']
        next_node = self.nodes['x = 3']
        
        self.assertLineNumber(for_node, 1)
        self.assertLineNumber(body_1, 2)
        self.assertLineNumber(body_2, 3)
        self.assertLineNumber(else_body_1, 5)
        self.assertLineNumber(else_body_2, 6)
        self.assertLineNumber(next_node, 7)

        
class CFGIfTest(CFGTestCase):

    def setUp(self):
        self.cfg = CFG()
        obj = parse(
'''\
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
        test = self.nodes['if x > 0:']
        eliftest = self.nodes['elif x == 0:']
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
        test = self.nodes['elif x == 0:']
        eliftest = self.nodes['x += 4'] # in this cas the elif is just a statement
        body_1 = self.nodes['x += 3']
        next_stmt = self.nodes['x += 5']

        self.assertConnected(test, eliftest)
        self.assertConnected(test, body_1)
        self.assertConnected(body_1, next_stmt)
        self.assertConnected(eliftest, next_stmt)

        
    def test_single_if(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/if.py')
        self.cfg.create(tree)
    
        self.assert_length(self.cfg.nodes, expected_length=4)
        
        start_node = 0
        test_node = 1
        body_node = 2
        exit_node = 3
        self.assertInCfg([(test_node,start_node), (body_node,test_node), (exit_node,test_node), (exit_node,body_node)])

    def test_single_if_else(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/if_else.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=5)

        start_node = 0
        test_node = 1
        body_node = 2
        else_body = 3
        exit_node = 4
        self.assertInCfg([(test_node,start_node), (body_node,test_node), (else_body,test_node), (exit_node,else_body), (exit_node,body_node)])

    def test_multiple_if_else(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/multiple_if_else.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=9)

        start_node = 0
        first_if = 1
        first_if_body = 2
        first_if_else_body = 3
        second_if = 4
        second_if_body = 5
        third_if = 6
        third_if_body = 7
        exit_node = 8
        self.assertInCfg([
            (first_if, start_node),
            (first_if_body, first_if),
            (first_if_else_body, first_if),
            (second_if, first_if_body),
            (second_if, first_if_else_body),
            (second_if_body, second_if),
            (third_if, second_if),
            (third_if, second_if_body),
            (third_if_body, third_if),
            (exit_node, third_if_body),
            (exit_node, third_if)
        ])

    def test_if_else_elif(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/if_else_elif.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=7)

        start_node = 0
        _if = 1
        _if_body = 2
        _elif = 3
        _elif_body = 4
        _else_body = 5
        exit_node = 6
        self.assertInCfg([
            (_if, start_node),
            (_if_body, _if),
            (_elif, _if),
            (_elif_body, _elif),
            (_else_body, _elif),
            (exit_node, _if_body),
            (exit_node, _elif_body),
            (exit_node, _else_body)
        ])

    def test_nested_if_else_elif(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/nested_if_else_elif.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=12)

        start = 0
        _if = 1
        if_body = 2
        nested_if = 3
        nested_if_body = 4
        nested_elif = 5
        nested_elif_body = 6
        nested_else_body = 7
        _elif = 8
        elif_body = 9
        else_body = 10
        _exit = 11
        self.assertInCfg([
            (_if, start),
            (if_body, _if),
            (nested_if, if_body),
            (nested_if_body, nested_if),
            (nested_elif, nested_if),
            (nested_elif_body, nested_elif),
            (nested_else_body, nested_elif),
            (_elif, _if),
            (elif_body, _elif),
            (else_body, _elif),
            (_exit, nested_if_body),
            (_exit, nested_elif_body),
            (_exit, nested_else_body),
            (_exit, else_body),
            (_exit, elif_body)
        ])

        
    def test_if_line_numbers(self):
        test = self.nodes['if x > 0:']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']

        eliftest = self.nodes['elif x == 0:']
        elif_body = self.nodes['x += 3']
        else_body = self.nodes['x += 4']
        next_stmt = self.nodes['x += 5']

        self.assertLineNumber(test, 1)
        self.assertLineNumber(body_1, 2)
        self.assertLineNumber(body_2, 3)
        self.assertLineNumber(eliftest, 4)
        self.assertLineNumber(elif_body, 5)
        self.assertLineNumber(else_body, 7)
        self.assertLineNumber(next_stmt, 8)

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

        test = self.nodes['while x > 0:']
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

        test = self.nodes['while x > 0:']
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

    def test_while_line_numbers(self):
        self.cfg = CFG()
        obj = parse(
'''\
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

        test = self.nodes['while x > 0:']
        body_1 = self.nodes['x += 1']
        body_2 = self.nodes['x += 2']
        else_body_1 = self.nodes['x += 3']
        else_body_2 = self.nodes['x += 4']
        next_stmt = self.nodes['x += 5']

        self.assertLineNumber(test, 1)
        self.assertLineNumber(body_1, 2)
        self.assertLineNumber(body_2, 3)
        self.assertLineNumber(else_body_1, 5)
        self.assertLineNumber(else_body_2, 6)
        self.assertLineNumber(next_stmt, 7)
        
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

    def test_start_line_numbers(self):
        self.assertLineNumber(self.cfg.nodes[0], None)
        self.assertLineNumber(self.cfg.nodes[1], 1)
        self.assertLineNumber(self.cfg.nodes[2], None)

class CFGAssignmentMultiTargetTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/assignment_two_targets.py')
        self.cfg.create(tree)

    def test_assignment_multi_target(self):
        start_node = self.cfg.nodes[0]
        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertConnected(start_node, node)
        self.assertConnected(node_2, exit_node)
        self.assertConnected(node, node_2)

        self.assertEqual(node.label, 'x = 1')
        self.assertEqual(node_2.label, 'y = 2')

        self.assertEqual(start_node.ast_type, 'ENTRY')
        self.assertEqual(exit_node.ast_type, 'EXIT')

    def test_assignment_multi_target_line_numbers(self): 
        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]

        self.assertLineNumber(node, 1)
        self.assertLineNumber(node_2, 1)
        
        
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

    def test_function_line_numbers(self):
        y_assignment = self.cfg.nodes[1]
        save_y = self.cfg.nodes[2]
        entry_foo = self.cfg.nodes[3]
        body_foo = self.cfg.nodes[4]
        exit_foo = self.cfg.nodes[5]
        y_load = self.cfg.nodes[6]

        self.assertLineNumber(y_assignment, 5)
        self.assertLineNumber(save_y, None)
        self.assertLineNumber(entry_foo, None)
        self.assertLineNumber(body_foo, 2)


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
        self.assert_length(self.cfg.nodes, expected_length=18)

        l = zip(range(1, len(self.cfg.nodes)), range(len(self.cfg.nodes)))
        self.assertInCfg(list(l))

    def test_function_line_numbers(self):
        assignment_with_function = self.cfg.nodes[1]

        self.assertLineNumber(assignment_with_function, 9)

class CFGAssignmentAndBuiltinTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/assignmentandbuiltin.py')
        self.cfg.create(tree)

    def test_assignment_and_builtin(self):
        start_node = self.cfg.nodes[0]
        assign = self.cfg.nodes[1]
        builtin = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertConnected(start_node, assign)
        self.assertConnected(assign, builtin)
        self.assertConnected(builtin, exit_node)

    def test_assignment_and_builtin_line_numbers(self):
        assign = self.cfg.nodes[1]
        builtin = self.cfg.nodes[2]

        self.assertLineNumber(assign, 1)
        self.assertLineNumber(builtin, 2)
        
class CFGMultipleParametersTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/multiple_parameters_function.py')
        self.cfg.create(tree)

    def test_start(self):
        length = len(self.cfg.nodes)
        self.assertEqual(length, 21)
        l = zip(range(1, length), range(length))

        self.assertInCfg(list(l))


class CFGCallWithAttributeTest(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/call_with_attribute.py')
        self.cfg.create(tree)

    def test_call_with_attribute(self):
        call = self.cfg.nodes[2]

        self.assertEqual(call.label, "request.args.get('param', 'not set')")

        length = 14
        self.assert_length(self.cfg.nodes, expected_length=length)

        l = zip(range(1, length), range(length))
        self.assertInCfg(list(l))

    def test_call_with_attribute_line_numbers(self):
        call = self.cfg.nodes[2]

        self.assertLineNumber(call, 5)

class CFGAssignListComprehension(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/list_comprehension.py')
        self.cfg.create(tree)

    def test_call_with_attribute(self):
        call = self.cfg.nodes[1]
        self.assertEqual(call.label, "x = ''.join(x.n for x in range(16))")

        length = 3
        self.assert_length(self.cfg.nodes, expected_length = length)

        l = zip(range(1, length), range(length))

        self.assertInCfg(list(l))


class CFGStr(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/str_ignored.py')
        self.cfg.create(tree)

    def test_str_ignored(self):
        self.assert_length(self.cfg.nodes, expected_length=3)

        expected_label = 'x = 0'
        actual_label = self.cfg.nodes[1].label
        self.assertEqual(expected_label, actual_label)

class CFGNameConstant(CFGTestCase):
    def setUp(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/name_constant.py')
        self.cfg.create(tree)

    def test_name_constant_in_assign(self):
        expected_label = 'x = True'
        actual_label = self.cfg.nodes[1].label
        self.assertEqual(expected_label, actual_label)

    def test_name_constant_if(self):
        expected_label = 'if True:'
        actual_label = self.cfg.nodes[2].label
        self.assertEqual(expected_label, actual_label)
        

class CFGName(CFGTestCase):
    """Test is Name nodes are properly handled in different contexts"""
    
    def test_name_if(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/name_if.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=5)
        self.assertEqual(self.cfg.nodes[2].label, 'if x:')

    def test_name_for(self):
        self.cfg = CFG()
        tree = generate_ast('../example/example_inputs/name_for.py')
        self.cfg.create(tree)

        self.assert_length(self.cfg.nodes, expected_length=4)
        self.assertEqual(self.cfg.nodes[1].label, 'for x in l:')
        
