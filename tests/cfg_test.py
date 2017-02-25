from .base_test_case import BaseTestCase
from pyt.base_cfg import Node, EntryExitNode
from pyt.project_handler import get_python_modules


class CFGGeneralTest(BaseTestCase):
    def test_repr_cfg(self):
        self.cfg_create_from_file('example/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        #print(repr(self.cfg))

    def test_str_cfg(self):
        self.cfg_create_from_file('example/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        #print(self.cfg)

    def test_no_tuples(self):
        self.cfg_create_from_file('example/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        for node in self.cfg.nodes:
            for edge in node.outgoing + node.ingoing:
                self.assertIsInstance(edge, Node)

    def test_start_and_exit_nodes(self):
        self.cfg_create_from_file('example/example_inputs/simple.py')

        self.assert_length(self.cfg.nodes, expected_length=3)

        start_node = 0
        node = 1
        exit_node = 2

        self.assertInCfg([(1,0),(2,1)])

        self.assertEqual(type(self.cfg.nodes[start_node]), EntryExitNode)
        self.assertEqual(type(self.cfg.nodes[exit_node]), EntryExitNode)

    def test_start_and_exit_nodes_line_numbers(self):
        self.cfg_create_from_file('example/example_inputs/simple.py')

        self.assertLineNumber(self.cfg.nodes[0], None)
        self.assertLineNumber(self.cfg.nodes[1], 1)
        self.assertLineNumber(self.cfg.nodes[2], None)

    def test_str_ignored(self):
        self.cfg_create_from_file('example/example_inputs/str_ignored.py')

        self.assert_length(self.cfg.nodes, expected_length=3)

        expected_label = 'x = 0'
        actual_label = self.cfg.nodes[1].label
        self.assertEqual(expected_label, actual_label)


class CFGForTest(BaseTestCase):
    def test_for_complete(self):
        self.cfg_create_from_file('example/example_inputs/for_complete.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        for_node = 1
        body_1 = 2
        body_2 = 3
        else_body_1 = 4
        else_body_2 = 5
        next_node = 6
        exit_node = 7

        self.assertEqual(self.cfg.nodes[for_node].label,'for x in range(3):')
        self.assertEqual(self.cfg.nodes[body_1].label, 'print(x)')
        self.assertEqual(self.cfg.nodes[body_2].label, 'y += 1')
        self.assertEqual(self.cfg.nodes[else_body_1].label, "print('Final: %s' % x)")
        self.assertEqual(self.cfg.nodes[else_body_2].label, 'print(y)')
        self.assertEqual(self.cfg.nodes[next_node].label, 'x = 3')

        self.assertInCfg([(for_node, entry), (body_1, for_node), (else_body_1, for_node), (body_2, body_1), (for_node, body_2), (else_body_2, else_body_1), (next_node, else_body_2), (exit_node, next_node)])

    def test_for_no_orelse(self):
        self.cfg_create_from_file('example/example_inputs/for_no_orelse.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        for_node = 1
        body_1 = 2
        body_2 = 3
        next_node = 4
        exit_node = 5

        self.assertInCfg([(for_node, entry), (body_1, for_node), (body_2, body_1), (for_node, body_2), (next_node, for_node), (exit_node, next_node)])

    def test_for_tuple_target(self):
        self.cfg_create_from_file('example/example_inputs/for_tuple_target.py')

        self.assert_length(self.cfg.nodes, expected_length = 4)

        entry_node = 0
        for_node = 1
        print_node = 2
        exit_node = 3

        self.assertInCfg([(for_node,entry_node),(print_node,for_node),(for_node,print_node),(exit_node,for_node)])
        self.assertEqual(self.cfg.nodes[for_node].label, "for (x, y) in [(1, 2), (3, 4)]:")

    def test_for_line_numbers(self):
        self.cfg_create_from_file('example/example_inputs/for_complete.py')

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

    def test_for_func_iterator(self):
        self.cfg_create_from_file('example/example_inputs/for_func_iterator.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        _for = 1
        entry_foo = 2
        ret_foo = 3
        exit_foo = 4
        call_foo = 5
        _print = 6
        _exit = 7

        self.assertInCfg([(_for, entry), (_for, call_foo), (_for, _print), (entry_foo, _for), (ret_foo, entry_foo), (exit_foo, ret_foo), (call_foo, exit_foo), (_print, _for), (_exit, _for)])

class CFGTryTest(BaseTestCase):
    def connected(self, node, successor):
        return (successor, node)

    def test_simple_try(self):
        self.cfg_create_from_file('example/example_inputs/try.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        try_ = 1
        try_body = 2
        except_ = 3
        except_body = 4
        _exit = 5

        self.assertInCfg([self.connected(entry, try_),
                          self.connected(try_, try_body),
                          self.connected(try_body, except_),
                          self.connected(except_, except_body),
                          self.connected(except_body, _exit),
                          self.connected(try_body, _exit)])

    def test_orelse(self):
        self.cfg_create_from_file('example/example_inputs/try_orelse.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=7)

        entry = 0
        try_ = 1
        try_body = 2
        except_im = 3
        except_im_body_1 = 4
        print_else = 5
        _exit = 6

        self.assertInCfg([self.connected(entry, try_),
                          self.connected(try_, try_body),
                          self.connected(try_body, except_im),
                          self.connected(try_body, print_else),
                          self.connected(try_body, _exit),
                          self.connected(except_im, except_im_body_1),
                          self.connected(except_im_body_1, _exit),
                          self.connected(print_else, _exit)])

    def test_final(self):
        self.cfg_create_from_file('example/example_inputs/try_final.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=7)

        entry = 0
        try_ = 1
        try_body = 2
        except_im = 3
        except_im_body_1 = 4
        print_final = 5
        _exit = 6

        self.assertInCfg([self.connected(entry, try_),
                          self.connected(try_, try_body),
                          self.connected(try_body, except_im),
                          self.connected(try_body, print_final),
                          self.connected(try_body, _exit),
                          self.connected(except_im, except_im_body_1),
                          self.connected(except_im_body_1, _exit),
                          self.connected(except_im_body_1, print_final),
                          self.connected(print_final, _exit)])


class CFGIfTest(BaseTestCase):
    def test_if_complete(self):
        self.cfg_create_from_file('example/example_inputs/if_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        test = 1
        body_1 = 2
        body_2 = 3
        eliftest = 4
        elif_body = 5
        else_body = 6
        next_node = 7
        exit_node = 8

        self.assertEqual(self.cfg.nodes[test].label, 'if x > 0:')
        self.assertEqual(self.cfg.nodes[eliftest].label, 'elif x == 0:')
        self.assertEqual(self.cfg.nodes[elif_body].label, 'x += 3')
        self.assertEqual(self.cfg.nodes[body_1].label, 'x += 1')
        self.assertEqual(self.cfg.nodes[body_2].label, 'x += 2')
        self.assertEqual(self.cfg.nodes[else_body].label, 'x += 4')
        self.assertEqual(self.cfg.nodes[next_node].label, 'x += 5')


        self.assertInCfg([(test, entry), (eliftest, test), (body_1, test), (body_2, body_1), (next_node, body_2), (else_body, eliftest), (elif_body, eliftest), (next_node, elif_body), (next_node, else_body), (exit_node, next_node)])

    def test_single_if(self):
        self.cfg_create_from_file('example/example_inputs/if.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        start_node = 0
        test_node = 1
        body_node = 2
        exit_node = 3
        self.assertInCfg([(test_node,start_node), (body_node,test_node), (exit_node,test_node), (exit_node,body_node)])

    def test_single_if_else(self):
        self.cfg_create_from_file('example/example_inputs/if_else.py')

        self.assert_length(self.cfg.nodes, expected_length=5)

        start_node = 0
        test_node = 1
        body_node = 2
        else_body = 3
        exit_node = 4
        self.assertInCfg([(test_node,start_node), (body_node,test_node), (else_body,test_node), (exit_node,else_body), (exit_node,body_node)])

    def test_multiple_if_else(self):
        self.cfg_create_from_file('example/example_inputs/multiple_if_else.py')

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
        self.cfg_create_from_file('example/example_inputs/if_else_elif.py')

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
        self.cfg_create_from_file('example/example_inputs/nested_if_else_elif.py')

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
        self.cfg_create_from_file('example/example_inputs/if_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        self.assert_length(self.cfg.nodes, expected_length=9)

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

    def test_if_not(self):
        self.cfg_create_from_file('example/example_inputs/if_not.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        entry = 0
        _if = 1
        body = 2
        _exit = 3

        self.assertInCfg([(1, 0), (2, 1), (3, 2), (3, 1)])


class CFGWhileTest(BaseTestCase):

    def test_while_complete(self):
        self.cfg_create_from_file('example/example_inputs/while_complete.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        test = 1
        body_1 = 2
        body_2 = 3
        else_body_1 = 4
        else_body_2 = 5
        next_node = 6
        exit_node = 7

        self.assertEqual(self.cfg.nodes[test].label, 'while x > 0:')

        self.assertInCfg([(test, entry), (body_1, test), (else_body_1, test), ( body_2, body_1), (test, body_2), (else_body_2, else_body_1), (next_node, else_body_2), (exit_node, next_node)])

    def test_while_no_orelse(self):
        self.cfg_create_from_file('example/example_inputs/while_no_orelse.py')

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        test = 1
        body_1 = 2
        body_2 = 3
        next_node = 4
        exit_node = 5

        self.assertInCfg([(test, entry), (body_1, test), ( next_node, test), (body_2, body_1), (test, body_2), (exit_node, next_node)])

    def test_while_line_numbers(self):
        self.cfg_create_from_file('example/example_inputs/while_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        self.assert_length(self.cfg.nodes, expected_length=8)

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


class CFGAssignmentMultiTest(BaseTestCase):
    def test_assignment_multi_target(self):
        self.cfg_create_from_file('example/example_inputs/assignment_two_targets.py')

        self.assert_length(self.cfg.nodes, expected_length=4)
        start_node = 0
        node = 1
        node_2 = 2
        exit_node =3

        self.assertInCfg([(node, start_node), (node_2, node), (exit_node, node_2)])

        self.assertEqual(self.cfg.nodes[node].label, 'x = 1')
        self.assertEqual(self.cfg.nodes[node_2].label, 'y = 2')

    def test_assignment_multi_target_call(self):
        self.cfg_create_from_file('example/example_inputs/assignment_multiple_assign_call.py')

        self.assert_length(self.cfg.nodes, expected_length=4)
        start_node = self.cfg.nodes[0]
        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertInCfg([(1,0),(2,1),(3,2)])

        self.assertEqual(node.label, 'x = int(5)')
        self.assertEqual(node_2.label, 'y = int(4)')

    def test_assignment_multi_target_line_numbers(self):
        self.cfg_create_from_file('example/example_inputs/assignment_two_targets.py')

        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]

        self.assertLineNumber(node, 1)
        self.assertLineNumber(node_2, 1)

    def test_assignment_and_builtin(self):
        self.cfg_create_from_file('example/example_inputs/assignmentandbuiltin.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        entry = 0
        assign = 1
        builtin = 2
        exit_node = 3

        self.assertInCfg([(assign, entry), (builtin, assign), (exit_node, builtin)])

    def test_assignment_and_builtin_line_numbers(self):
        self.cfg_create_from_file('example/example_inputs/assignmentandbuiltin.py')

        assign = self.cfg.nodes[1]
        builtin = self.cfg.nodes[2]

        self.assertLineNumber(assign, 1)
        self.assertLineNumber(builtin, 2)

    def test_multiple_assignment(self):
        self.cfg_create_from_file('example/example_inputs/assignment_multiple_assign.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        start_node = self.cfg.nodes[0]
        assign_y = self.cfg.nodes[1]
        assign_x = self.cfg.nodes[2]
        exit_node = self.cfg.nodes[-1]

        self.assertEqual(assign_x.label, 'x = 5')
        self.assertEqual(assign_y.label, 'y = 5')

    def test_assign_list_comprehension(self):
        self.cfg_create_from_file('example/example_inputs/generator_expression_assign.py')

        length = 3
        self.assert_length(self.cfg.nodes, expected_length = length)

        call = self.cfg.nodes[1]
        self.assertEqual(call.label, "x = ''.join((x.n for x in range(16)))")

        l = zip(range(1, length), range(length))

        self.assertInCfg(list(l))

    def test_assignment_tuple_value(self):
        self.cfg_create_from_file('example/example_inputs/assignment_tuple_value.py')

        self.assert_length(self.cfg.nodes, expected_length=3)
        start_node = 0
        node = 1
        exit_node = 2
        print(self.cfg)

        self.assertInCfg([(node, start_node), (exit_node, node)])

        self.assertEqual(self.cfg.nodes[node].label, 'a = (x, y)')


class CFGComprehensionTest(BaseTestCase):
    def test_nodes(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

    def test_list_comprehension(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[1]

        self.assertEqual(listcomp.label, 'l = [x for x in [1, 2, 3]]')

    def test_list_comprehension_multi(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[2]

        self.assertEqual(listcomp.label, 'll = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]')

    def test_dict_comprehension(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        dictcomp = self.cfg.nodes[3]

        self.assertEqual(dictcomp.label, 'd = {i : x for (i, x) in enumerate([1, 2, 3])}')

    def test_set_comprehension(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        setcomp = self.cfg.nodes[4]

        self.assertEqual(setcomp.label, 's = {x for x in [1, 2, 3, 2, 2, 1, 2]}')

    def test_generator_expression(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[5]

        self.assertEqual(listcomp.label, 'g = (x for x in [1, 2, 3])')

    def test_dict_comprehension_multi(self):
        self.cfg_create_from_file('example/example_inputs/comprehensions.py')
        listcomp = self.cfg.nodes[6]

        self.assertEqual(listcomp.label, 'dd = {x + y : y for x in [1, 2, 3] for y in [4, 5, 6]}')

class CFGFunctionNodeTest(BaseTestCase):
    def connected(self, node, successor):
        return (successor, node)

    def test_simple_function(self):
        path = 'example/example_inputs/simple_function.py'
        self.cfg_create_from_file(path)


        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        y_assignment = 1
        save_y = 2
        entry_foo = 3
        body_foo = 4
        exit_foo = 5
        y_load = 6
        exit_ = 7

        self.assertInCfg([self.connected(entry, y_assignment),
                          self.connected(y_assignment, save_y),
                          self.connected(save_y, entry_foo),
                          self.connected(entry_foo, body_foo),
                          self.connected(body_foo, exit_foo),
                          self.connected(exit_foo, y_load),
                          self.connected(y_load, exit_)])

    def test_function_line_numbers(self):
        path = 'example/example_inputs/simple_function.py'
        self.cfg_create_from_file(path)

        y_assignment = self.cfg.nodes[1]
        save_y = self.cfg.nodes[2]
        entry_foo = self.cfg.nodes[3]
        body_foo = self.cfg.nodes[4]
        exit_foo = self.cfg.nodes[5]
        y_load = self.cfg.nodes[6]

        self.assertLineNumber(y_assignment, 5)
        self.assertLineNumber(save_y, 1)
        self.assertLineNumber(entry_foo, None)
        self.assertLineNumber(body_foo, 2)

    def test_function_parameters(self):
        path = 'example/example_inputs/parameters_function.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=12)

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

    def test_function_with_return(self):
        path = 'example/example_inputs/simple_function_with_return.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=18)

        l = zip(range(1, len(self.cfg.nodes)), range(len(self.cfg.nodes)))
        self.assertInCfg(list(l))

    def test_function_multiple_return(self):
        path = 'example/example_inputs/function_with_multiple_return.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        entry_foo = 1
        a = 2
        _if = 3
        ret_if = 4
        ret = 5
        exit_foo = 6
        call_foo = 7
        _exit = 8

        self.assertInCfg([(entry_foo, entry),
                          (a, entry_foo),
                          (_if, a),
                          (ret_if, _if),
                          (ret, _if),
                          (exit_foo, ret_if),
                          (exit_foo, ret),
                          (call_foo, exit_foo),
                          (_exit, call_foo)])


    def test_function_line_numbers_2(self):
        path = 'example/example_inputs/simple_function_with_return.py'
        self.cfg_create_from_file(path)
#        self.cfg = CFG(get_python_modules(path))
 #       tree = generate_ast(path)
  #      self.cfg.create(tree)

        assignment_with_function = self.cfg.nodes[1]

        self.assertLineNumber(assignment_with_function, 9)

    def test_multiple_parameters(self):
        path = 'example/example_inputs/multiple_parameters_function.py'

        self.cfg_create_from_file(path)

        length = len(self.cfg.nodes)

        self.assertEqual(length, 21)
        l = zip(range(1, length), range(length))

        self.assertInCfg(list(l))

    def test_call_on_call(self):
        path = 'example/example_inputs/call_on_call.py'
        self.cfg_create_from_file(path)




class CFGCallWithAttributeTest(BaseTestCase):
    def setUp(self):
        self.cfg_create_from_file('example/example_inputs/call_with_attribute.py')

    def test_call_with_attribute(self):
        length = 14
        self.assert_length(self.cfg.nodes, expected_length=length)

        call = self.cfg.nodes[2]
        self.assertEqual(call.label, "request.args.get('param', 'not set')")

        l = zip(range(1, length), range(length))
        self.assertInCfg(list(l))

    def test_call_with_attribute_line_numbers(self):
        call = self.cfg.nodes[2]

        self.assertLineNumber(call, 5)

class CFGBreak(BaseTestCase):
    """Break in while and for and other places"""
    def test_break(self):
        self.cfg_create_from_file('example/example_inputs/while_break.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        _while = 1
        _if = 2
        print_x = 3
        _break = 4
        print_hest = 5
        print_next = 6
        _exit = 7

        self.assertInCfg([(_while, entry), (_while, print_hest), (_if, _while), (print_x, _if), (_break, print_x), (print_hest, _if), (print_next, _while), (print_next, _break), (_exit, print_next)])


class CFGNameConstant(BaseTestCase):
    def setUp(self):
        self.cfg_create_from_file('example/example_inputs/name_constant.py')

    def test_name_constant_in_assign(self):
        self.assert_length(self.cfg.nodes, expected_length=6)

        expected_label = 'x = True'
        actual_label = self.cfg.nodes[1].label
        self.assertEqual(expected_label, actual_label)

    def test_name_constant_if(self):
        self.assert_length(self.cfg.nodes, expected_length=6)
        expected_label = 'if True:'
        actual_label = self.cfg.nodes[2].label
        self.assertEqual(expected_label, actual_label)


class CFGName(BaseTestCase):
    """Test is Name nodes are properly handled in different contexts"""

    def test_name_if(self):
        self.cfg_create_from_file('example/example_inputs/name_if.py')


        self.assert_length(self.cfg.nodes, expected_length=5)
        self.assertEqual(self.cfg.nodes[2].label, 'if x:')

    def test_name_for(self):
        self.cfg_create_from_file('example/example_inputs/name_for.py')

        self.assert_length(self.cfg.nodes, expected_length=4)
        self.assertEqual(self.cfg.nodes[1].label, 'for x in l:')
