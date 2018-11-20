import ast

from .cfg_base_test_case import CFGBaseTestCase

from pyt.core.node_types import (
    BBorBInode,
    EntryOrExitNode,
    Node
)


class CFGGeneralTest(CFGBaseTestCase):
    def test_repr_cfg(self):
        self.cfg_create_from_file('examples/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

    def test_str_cfg(self):
        self.cfg_create_from_file('examples/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

    def test_no_tuples(self):
        self.cfg_create_from_file('examples/example_inputs/for_complete.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        for node in self.cfg.nodes:
            for edge in node.outgoing + node.ingoing:
                self.assertIsInstance(edge, Node)

    def test_start_and_exit_nodes(self):
        self.cfg_create_from_file('examples/example_inputs/simple.py')

        self.assert_length(self.cfg.nodes, expected_length=3)

        start_node = 0
        node = 1
        exit_node = 2

        self.assertInCfg([
            (node, start_node),
            (exit_node, node)
        ])

        self.assertEqual(type(self.cfg.nodes[start_node]), EntryOrExitNode)
        self.assertEqual(type(self.cfg.nodes[exit_node]), EntryOrExitNode)

    def test_start_and_exit_nodes_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/simple.py')

        self.assertLineNumber(self.cfg.nodes[0], None)
        self.assertLineNumber(self.cfg.nodes[1], 1)
        self.assertLineNumber(self.cfg.nodes[2], None)

    def test_str_ignored(self):
        self.cfg_create_from_file('examples/example_inputs/str_ignored.py')

        self.assert_length(self.cfg.nodes, expected_length=3)

        expected_label = 'x = 0'
        actual_label = self.cfg.nodes[1].label
        self.assertEqual(expected_label, actual_label)


class CFGForTest(CFGBaseTestCase):
    def test_for_complete(self):
        self.cfg_create_from_file('examples/example_inputs/for_complete.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        for_node = 1
        body_1 = 2
        body_2 = 3
        else_body_1 = 4
        else_body_2 = 5
        next_node = 6
        exit_node = 7

        self.assertEqual(self.cfg.nodes[for_node].label, 'for x in range(3):')
        self.assertEqual(self.cfg.nodes[body_1].label, '~call_1 = ret_print(x)')
        self.assertEqual(self.cfg.nodes[body_2].label, 'y += 1')
        self.assertEqual(self.cfg.nodes[else_body_1].label, "~call_2 = ret_print('Final: %s' % x)")
        self.assertEqual(self.cfg.nodes[else_body_2].label, '~call_3 = ret_print(y)')
        self.assertEqual(self.cfg.nodes[next_node].label, 'x = 3')

        self.assertInCfg([
            (for_node, entry),
            (body_1, for_node),
            (else_body_1, for_node),
            (body_2, body_1),
            (for_node, body_2),
            (else_body_2, else_body_1),
            (next_node, else_body_2),
            (exit_node, next_node)
        ])

    def test_for_no_orelse(self):
        self.cfg_create_from_file('examples/example_inputs/for_no_orelse.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        for_node = 1
        body_1 = 2
        body_2 = 3
        next_node = 4
        exit_node = 5

        self.assertInCfg([
            (for_node, entry),
            (body_1, for_node),
            (body_2, body_1),
            (for_node, body_2),
            (next_node, for_node),
            (exit_node, next_node)
        ])

    def test_for_tuple_target(self):
        self.cfg_create_from_file('examples/example_inputs/for_tuple_target.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        entry_node = 0
        for_node = 1
        print_node = 2
        exit_node = 3

        self.assertInCfg([
            (for_node, entry_node),
            (print_node, for_node),
            (for_node, print_node),
            (exit_node, for_node)
        ])
        self.assertEqual(
            self.cfg.nodes[for_node].label,
            "for (x, y) in [(1, 2), (3, 4)]:"
        )

    def test_for_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/for_complete.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        for_node = self.nodes['for x in range(3):']
        body_1 = self.nodes['~call_1 = ret_print(x)']
        body_2 = self.nodes['y += 1']
        else_body_1 = self.nodes["~call_2 = ret_print('Final: %s' % x)"]
        else_body_2 = self.nodes['~call_3 = ret_print(y)']
        next_node = self.nodes['x = 3']

        self.assertLineNumber(for_node, 1)
        self.assertLineNumber(body_1, 2)
        self.assertLineNumber(body_2, 3)
        self.assertLineNumber(else_body_1, 5)
        self.assertLineNumber(else_body_2, 6)
        self.assertLineNumber(next_node, 7)

    def test_for_func_iterator(self):
        self.cfg_create_from_file('examples/example_inputs/for_func_iterator.py')

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        _for = 1
        entry_foo = 2
        call_to_range = 3
        ret_foo = 4
        exit_foo = 5
        call_foo = 6
        _print = 7
        _exit = 8

        self.assertInCfg([
            (_for, entry),
            (_for, call_foo),
            (_for, _print),
            (entry_foo, _for),
            (call_to_range, entry_foo),
            (ret_foo, call_to_range),
            (exit_foo, ret_foo),
            (call_foo, exit_foo),
            (_print, _for),
            (_exit, _for)
        ])


class CFGTryTest(CFGBaseTestCase):
    def connected(self, node, successor):
        return (successor, node)

    def test_simple_try(self):
        self.cfg_create_from_file('examples/example_inputs/try.py')

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
        self.cfg_create_from_file('examples/example_inputs/try_orelse.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        self.assert_length(self.cfg.nodes, expected_length=20)

        entry = 0
        try_ = 1
        try_body = 2
        print_a5 = 3
        except_im = 4
        except_im_body_1 = 5
        value_equal_call_2 = 6  # value = ~call_2
        print_wagyu = 7
        save_node = 8
        assign_to_temp = 9
        assign_from_temp = 10
        function_entry = 11
        ret_of_subprocess_call = 12
        ret_does_this_kill_us_equal_call_5 = 13  # ret_does_this_kill_us = ~call_5
        function_exit = 14
        restore_node = 15
        return_handler = 16
        print_so = 17
        print_good = 18
        _exit = 19

        self.assertInCfg([
            self.connected(entry, try_),

            self.connected(try_, try_body),

            self.connected(try_body, print_a5),

            self.connected(print_a5, except_im),
            self.connected(print_a5, save_node),
            self.connected(print_a5, print_good),

            self.connected(except_im, except_im_body_1),

            self.connected(except_im_body_1, value_equal_call_2),
            self.connected(value_equal_call_2, print_wagyu),

            self.connected(print_wagyu, print_good),

            self.connected(save_node, assign_to_temp),
            self.connected(assign_to_temp, assign_from_temp),
            self.connected(assign_from_temp, function_entry),
            self.connected(function_entry, ret_of_subprocess_call),
            self.connected(ret_of_subprocess_call, ret_does_this_kill_us_equal_call_5),
            self.connected(ret_does_this_kill_us_equal_call_5, function_exit),
            self.connected(function_exit, restore_node),
            self.connected(restore_node, return_handler),
            self.connected(return_handler, print_so),

            self.connected(print_so, print_good),
            self.connected(print_good, _exit)
        ])

    def test_orelse_with_no_variables_to_save(self):
        self.cfg_create_from_file('examples/example_inputs/try_orelse_with_no_variables_to_save.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        self.assert_length(self.cfg.nodes, expected_length=15)

        entry = 0
        try_ = 1
        print_a5 = 2
        except_im = 3
        print_wagyu = 4
        temp_3_diff = 5
        diff = 6
        function_entry = 7
        ret_subprocess_call = 8
        ret_does_this_kill_us_4 = 9
        exit_does_this_kill_us = 10
        ret_does_this_kill_us_3 = 11
        print_so = 12
        print_good = 13
        _exit = 14

        self.assertInCfg([
            self.connected(entry, try_),
            self.connected(try_, print_a5),
            self.connected(print_a5, except_im),
            self.connected(print_a5, temp_3_diff),
            self.connected(print_a5, print_good),
            self.connected(except_im, print_wagyu),
            self.connected(print_wagyu, print_good),
            self.connected(temp_3_diff, diff),
            self.connected(diff, function_entry),
            self.connected(function_entry, ret_subprocess_call),
            self.connected(ret_subprocess_call, ret_does_this_kill_us_4),
            self.connected(ret_does_this_kill_us_4, exit_does_this_kill_us),
            self.connected(exit_does_this_kill_us, ret_does_this_kill_us_3),
            self.connected(ret_does_this_kill_us_3, print_so),
            self.connected(print_so, print_good),
            self.connected(print_good, _exit)
        ])

    def test_try_orelse_with_no_variables_to_save_and_no_args(self):
        self.cfg_create_from_file('examples/example_inputs/try_orelse_with_no_variables_to_save_and_no_args.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)
        self.assert_length(self.cfg.nodes, expected_length=13)

        entry = 0
        try_ = 1
        print_a5 = 2
        except_im = 3
        print_wagyu = 4
        function_entry = 5
        ret_subprocess_call = 6
        ret_does_this_kill_us_4 = 7
        exit_does_this_kill_us = 8
        ret_does_this_kill_us_3 = 9
        print_so = 10
        print_good = 11
        _exit = 12

        self.assertInCfg([
            self.connected(entry, try_),
            self.connected(try_, print_a5),
            self.connected(print_a5, except_im),
            self.connected(print_a5, function_entry),
            self.connected(print_a5, print_good),
            self.connected(except_im, print_wagyu),
            self.connected(print_wagyu, print_good),
            self.connected(function_entry, ret_subprocess_call),
            self.connected(ret_subprocess_call, ret_does_this_kill_us_4),
            self.connected(ret_does_this_kill_us_4, exit_does_this_kill_us),
            self.connected(exit_does_this_kill_us, ret_does_this_kill_us_3),
            self.connected(ret_does_this_kill_us_3, print_so),
            self.connected(print_so, print_good),
            self.connected(print_good, _exit)
        ])

    def test_final(self):
        self.cfg_create_from_file('examples/example_inputs/try_final.py')

        self.nodes = self.cfg_list_to_dict(self.cfg.nodes)

        self.assert_length(self.cfg.nodes, expected_length=7)

        entry = 0
        try_ = 1
        try_body = 2
        except_im = 3
        except_im_body_1 = 4
        print_final = 5
        _exit = 6

        self.assertInCfg([
            self.connected(entry, try_),
            self.connected(try_, try_body),
            self.connected(try_body, except_im),
            self.connected(try_body, print_final),
            self.connected(try_body, _exit),
            self.connected(except_im, except_im_body_1),
            self.connected(except_im_body_1, _exit),
            self.connected(except_im_body_1, print_final),
            self.connected(print_final, _exit)
        ])


class CFGIfTest(CFGBaseTestCase):
    def test_if_complete(self):
        self.cfg_create_from_file('examples/example_inputs/if_complete.py')

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

        self.assertInCfg([
            (test, entry),
            (eliftest, test),
            (body_1, test),
            (body_2, body_1),
            (next_node, body_2),
            (else_body, eliftest),
            (elif_body, eliftest),
            (next_node, elif_body),
            (next_node, else_body),
            (exit_node, next_node)
        ])

    def test_single_if(self):
        self.cfg_create_from_file('examples/example_inputs/if.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        start_node = 0
        test_node = 1
        body_node = 2
        exit_node = 3

        self.assertInCfg([
            (test_node, start_node),
            (body_node, test_node),
            (exit_node, test_node),
            (exit_node, body_node)
        ])

    def test_single_if_else(self):
        self.cfg_create_from_file('examples/example_inputs/if_else.py')

        self.assert_length(self.cfg.nodes, expected_length=5)

        start_node = 0
        test_node = 1
        body_node = 2
        else_body = 3
        exit_node = 4

        self.assertInCfg([
            (test_node, start_node),
            (body_node, test_node),
            (else_body, test_node),
            (exit_node, else_body),
            (exit_node, body_node)
        ])

    def test_multiple_if_else(self):
        self.cfg_create_from_file('examples/example_inputs/multiple_if_else.py')

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
        self.cfg_create_from_file('examples/example_inputs/if_else_elif.py')

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
        self.cfg_create_from_file('examples/example_inputs/nested_if_else_elif.py')

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
        self.cfg_create_from_file('examples/example_inputs/if_complete.py')

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
        self.cfg_create_from_file('examples/example_inputs/if_not.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        entry = 0
        _if = 1
        body = 2
        _exit = 3

        self.assertInCfg([
            (_if, entry),
            (body, _if),
            (_exit, body),
            (_exit, _if)
        ])

    def test_ternary_ifexp(self):
        self.cfg_create_from_file('examples/example_inputs/ternary.py')

        # entry = 0
        tmp_if_1 = 1
        # tmp_if_inner = 2
        call = 3
        # tmp_if_call = 4
        actual_if_exp = 5
        exit = 6

        self.assert_length(self.cfg.nodes, expected_length=exit + 1)
        self.assertInCfg([
            (i + 1, i) for i in range(exit)
        ])

        self.assertCountEqual(
            self.cfg.nodes[actual_if_exp].right_hand_side_variables,
            ['y'],
            "The variables in the test expressions shouldn't appear as RHS variables"
        )

        self.assertCountEqual(
            self.cfg.nodes[tmp_if_1].right_hand_side_variables,
            ['t', 'v'],
        )

        self.assertIn(
            'ret_func(',
            self.cfg.nodes[call].label,
            "Function calls inside the test expressions should still appear in the CFG",
        )


class CFGWhileTest(CFGBaseTestCase):

    def test_while_complete(self):
        self.cfg_create_from_file('examples/example_inputs/while_complete.py')

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

        self.assertInCfg([
            (test, entry),
            (body_1, test),
            (else_body_1, test),
            (body_2, body_1),
            (test, body_2),
            (else_body_2, else_body_1),
            (next_node, else_body_2),
            (exit_node, next_node)
        ])

    def test_while_no_orelse(self):
        self.cfg_create_from_file('examples/example_inputs/while_no_orelse.py')

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        test = 1
        body_1 = 2
        body_2 = 3
        next_node = 4
        exit_node = 5

        self.assertInCfg([
            (test, entry),
            (body_1, test),
            (next_node, test),
            (body_2, body_1),
            (test, body_2),
            (exit_node, next_node)
        ])

    def test_while_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/while_complete.py')

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

    def test_while_func_comparator(self):
        self.cfg_create_from_file('examples/example_inputs/while_func_comparator.py')

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        test = 1
        entry_foo = 2
        ret_foo = 3
        exit_foo = 4
        call_foo = 5
        _print = 6
        body_1 = 7
        _exit = 8

        self.assertEqual(self.cfg.nodes[test].label, 'while foo():')

        self.assertInCfg([
            (test, entry),
            (entry_foo, test),
            (_print, test),
            (_exit, test),
            (body_1, _print),
            (test, body_1),
            (test, call_foo),
            (ret_foo, entry_foo),
            (exit_foo, ret_foo),
            (call_foo, exit_foo)
        ])

    def test_while_func_comparator_rhs(self):
        self.cfg_create_from_file('examples/example_inputs/while_func_comparator_rhs.py')

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        test = 1
        entry_foo = 2
        ret_foo = 3
        exit_foo = 4
        call_foo = 5
        _print = 6
        body_1 = 7
        _exit = 8

        self.assertEqual(self.cfg.nodes[test].label, 'while x < foo():')

        self.assertInCfg([
            (test, entry),
            (entry_foo, test),
            (_print, test),
            (_exit, test),
            (body_1, _print),
            (test, body_1),
            (test, call_foo),
            (ret_foo, entry_foo),
            (exit_foo, ret_foo),
            (call_foo, exit_foo)
        ])

    def test_while_func_comparator_lhs(self):
        self.cfg_create_from_file('examples/example_inputs/while_func_comparator_lhs.py')

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        test = 1
        entry_foo = 2
        ret_foo = 3
        exit_foo = 4
        call_foo = 5
        _print = 6
        body_1 = 7
        _exit = 8

        self.assertEqual(self.cfg.nodes[test].label, 'while foo() > x:')

        self.assertInCfg([
            (test, entry),
            (entry_foo, test),
            (_print, test),
            (_exit, test),
            (body_1, _print),
            (test, body_1),
            (test, call_foo),
            (ret_foo, entry_foo),
            (exit_foo, ret_foo),
            (call_foo, exit_foo)
        ])


class CFGAssignmentMultiTest(CFGBaseTestCase):
    def test_assignment_multi_target(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_two_targets.py')

        self.assert_length(self.cfg.nodes, expected_length=4)
        start_node = 0
        node = 1
        node_2 = 2
        exit_node = 3

        self.assertInCfg([(node, start_node), (node_2, node), (exit_node, node_2)])

        self.assertEqual(self.cfg.nodes[node].label, 'x = 1')
        self.assertEqual(self.cfg.nodes[node_2].label, 'y = 2')

    def test_assignment_multi_target_call(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_multiple_assign_call.py')

        self.assert_length(self.cfg.nodes, expected_length=6)

        # start_node = self.cfg.nodes[0]
        assignment_to_call1 = self.cfg.nodes[1]
        assignment_to_x = self.cfg.nodes[2]
        assignment_to_call2 = self.cfg.nodes[3]
        assignment_to_y = self.cfg.nodes[4]
        # exit_node = self.cfg.nodes[5]

        # This assert means N should be connected to N+1
        self.assertInCfg([
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 4)
        ])

        self.assertEqual(assignment_to_call1.label, '~call_1 = ret_int(5)')
        self.assertEqual(assignment_to_x.label, 'x = ~call_1')
        self.assertEqual(assignment_to_call2.label, '~call_2 = ret_int(4)')
        self.assertEqual(assignment_to_y.label, 'y = ~call_2')

    def test_assignment_multi_target_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_two_targets.py')

        node = self.cfg.nodes[1]
        node_2 = self.cfg.nodes[2]

        self.assertLineNumber(node, 1)
        self.assertLineNumber(node_2, 1)

    def test_assignment_and_builtin(self):
        self.cfg_create_from_file('examples/example_inputs/assignmentandbuiltin.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        entry = 0
        assign = 1
        builtin = 2
        exit_node = 3

        self.assertInCfg([(assign, entry), (builtin, assign), (exit_node, builtin)])

    def test_assignment_and_builtin_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/assignmentandbuiltin.py')

        assign = self.cfg.nodes[1]
        builtin = self.cfg.nodes[2]

        self.assertLineNumber(assign, 1)
        self.assertLineNumber(builtin, 2)

    def test_assignment_with_annotation(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_with_annotation.py')

        self.assert_length(self.cfg.nodes, expected_length=3)

        entry = 0
        assign = 1
        exit_node = 2

        self.assertInCfg([(assign, entry), (exit_node, assign)])
        self.assertEqual(self.cfg.nodes[assign].label, 'y = 5')

    def test_assignment_with_annotation_line_numbers(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_with_annotation.py')

        assign = self.cfg.nodes[1]

        self.assertLineNumber(assign, 2)

    def test_multiple_assignment(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_multiple_assign.py')

        self.assert_length(self.cfg.nodes, expected_length=4)

        assign_y = self.cfg.nodes[1]
        assign_x = self.cfg.nodes[2]

        self.assertEqual(assign_x.label, 'x = 5')
        self.assertEqual(assign_y.label, 'y = 5')

    def test_assign_list_comprehension(self):
        self.cfg_create_from_file('examples/example_inputs/generator_expression_assign.py')

        length = 4
        self.assert_length(self.cfg.nodes, expected_length=length)

        call = self.cfg.nodes[1]
        self.assertEqual(call.label, "~call_1 = ret_''.join((x.n for x in range(16)))")

        self.assertInCfg(
            list(
                zip(
                    range(1, length), range(length)
                )
            )
        )

    def test_assignment_tuple_value(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_tuple_value.py')

        self.assert_length(self.cfg.nodes, expected_length=3)
        start_node = 0
        node = 1
        exit_node = 2

        self.assertInCfg([(node, start_node), (exit_node, node)])

        self.assertEqual(self.cfg.nodes[node].label, 'a = (x, y)')

    def test_assignment_starred(self):
        self.cfg_create_from_file('examples/example_inputs/assignment_starred.py')

        middle_nodes = self.cfg.nodes[1:-1]
        self.assert_length(middle_nodes, expected_length=5)

        visited = [self.cfg.nodes[0]]
        while True:
            current_node = visited[-1]
            if len(current_node.outgoing) != 1:
                break
            visited.append(current_node.outgoing[0])
        self.assertCountEqual(self.cfg.nodes, visited, msg="Did not complete a path from Entry to Exit")

        self.assertEqual(middle_nodes[0].label, 'a = f')
        self.assertCountEqual(  # We don't assert a specific order for the assignment nodes
            [n.label for n in middle_nodes],
            ['a = f', 'd = f + i', 'e = j'] + ['*b, c = *g, *h'] * 2,
        )
        self.assertCountEqual(
            [(n.left_hand_side, n.right_hand_side_variables) for n in middle_nodes],
            [('a', ['f']), ('b', ['g', 'h']), ('c', ['g', 'h']), ('d', ['f', 'i']), ('e', ['j'])],
        )

    def test_assignment_starred_list(self):
        self.cfg_create_from_ast(ast.parse('[a, b, c] = *d, e'))

        middle_nodes = self.cfg.nodes[1:-1]
        self.assert_length(middle_nodes, expected_length=3)

        self.assertCountEqual(
            [n.label for n in middle_nodes],
            ['a, b = *d', 'a, b = *d', 'c = e'],
        )
        self.assertCountEqual(
            [(n.left_hand_side, n.right_hand_side_variables) for n in middle_nodes],
            [('a', ['d']), ('b', ['d']), ('c', ['e'])],
        )

    def test_unpacking_to_tuple(self):
        self.cfg_create_from_ast(ast.parse('a, b, c = d'))

        middle_nodes = self.cfg.nodes[1:-1]
        self.assert_length(middle_nodes, expected_length=3)

        self.assertCountEqual(
            [n.label for n in middle_nodes],
            ['a, b, c = *d'] * 3,
        )
        self.assertCountEqual(
            [(n.left_hand_side, n.right_hand_side_variables) for n in middle_nodes],
            [('a', ['d']), ('b', ['d']), ('c', ['d'])],
        )

    def test_augmented_assignment(self):
        self.cfg_create_from_ast(ast.parse('a+=f(b,c)'))

        (node,) = self.cfg.nodes[1:-1]
        self.assertEqual(node.label, 'a += f(b, c)')
        self.assertEqual(node.left_hand_side, 'a')
        self.assertEqual(node.right_hand_side_variables, ['b', 'c', 'a'])


class CFGComprehensionTest(CFGBaseTestCase):
    def test_nodes(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

    def test_list_comprehension(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[1]

        self.assertEqual(listcomp.label, 'l = [x for x in [1, 2, 3]]')

    def test_list_comprehension_multi(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[2]

        self.assertEqual(listcomp.label, 'll = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]')

    def test_dict_comprehension(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        dictcomp = self.cfg.nodes[3]

        self.assertEqual(dictcomp.label, 'd = {i : x for (i, x) in enumerate([1, 2, 3])}')

    def test_set_comprehension(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        setcomp = self.cfg.nodes[4]

        self.assertEqual(setcomp.label, 's = {x for x in [1, 2, 3, 2, 2, 1, 2]}')

    def test_generator_expression(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')

        listcomp = self.cfg.nodes[5]

        self.assertEqual(listcomp.label, 'g = (x for x in [1, 2, 3])')

    def test_dict_comprehension_multi(self):
        self.cfg_create_from_file('examples/example_inputs/comprehensions.py')
        listcomp = self.cfg.nodes[6]

        self.assertEqual(listcomp.label, 'dd = {x + y : y for x in [1, 2, 3] for y in [4, 5, 6]}')


class CFGFunctionNodeTest(CFGBaseTestCase):
    def connected(self, node, successor):
        return (successor, node)

    def test_simple_function(self):
        path = 'examples/example_inputs/simple_function.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        input_call = 1
        y_assignment = 2
        save_y = 3
        entry_foo = 4
        body_foo = 5
        exit_foo = 6
        y_load = 7
        _exit = 8

        self.assertInCfg([self.connected(entry, input_call),
                          self.connected(input_call, y_assignment),
                          self.connected(y_assignment, save_y),
                          self.connected(save_y, entry_foo),
                          self.connected(entry_foo, body_foo),
                          self.connected(body_foo, exit_foo),
                          self.connected(exit_foo, y_load),
                          self.connected(y_load, _exit)])

    def test_function_line_numbers(self):
        path = 'examples/example_inputs/simple_function.py'
        self.cfg_create_from_file(path)

        input_call = self.cfg.nodes[1]
        y_assignment = self.cfg.nodes[2]
        save_y = self.cfg.nodes[3]
        entry_foo = self.cfg.nodes[4]
        body_foo = self.cfg.nodes[5]
        exit_foo = self.cfg.nodes[6]
        y_load = self.cfg.nodes[7]

        self.assertLineNumber(input_call, 5)
        self.assertLineNumber(y_assignment, 5)
        self.assertLineNumber(save_y, 1)
        self.assertLineNumber(entry_foo, None)
        self.assertLineNumber(body_foo, 2)
        self.assertLineNumber(exit_foo, None)
        self.assertLineNumber(y_load, 1)

    def test_function_parameters(self):
        path = 'examples/example_inputs/parameters_function.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=14)

        entry = 0
        input_call = 1
        y_assignment = 2
        save_y = 3
        save_actual_y = 4
        bar_local_y = 5
        entry_bar = 6
        another_input_call = 7
        bar_y_assignment = 8
        bar_print_y = 9
        bar_print_x = 10
        exit_bar = 11
        restore_actual_y = 12
        _exit = 13

        self.assertInCfg([
            self.connected(entry, input_call),
            self.connected(input_call, y_assignment),
            self.connected(y_assignment, save_y),
            self.connected(save_y, save_actual_y),
            self.connected(save_actual_y, bar_local_y),
            self.connected(bar_local_y, entry_bar),
            self.connected(entry_bar, another_input_call),
            self.connected(another_input_call, bar_y_assignment),
            self.connected(bar_y_assignment, bar_print_y),
            self.connected(bar_print_y, bar_print_x),
            self.connected(bar_print_x, exit_bar),
            self.connected(exit_bar, restore_actual_y),
            self.connected(restore_actual_y, _exit)
        ])

    def test_function_with_return(self):
        path = 'examples/example_inputs/simple_function_with_return.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=19)

        self.assertInCfg(
            list(
                zip(
                    range(1, len(self.cfg.nodes)), range(len(self.cfg.nodes))
                )
            )
        )

    def test_function_multiple_return(self):
        path = 'examples/example_inputs/function_with_multiple_return.py'
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

    def test_generator_multiple_yield(self):
        path = 'examples/example_inputs/generator_with_multiple_yields.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        entry_foo = 1
        a = 2
        _if = 3
        yld_if = 4
        yld = 5
        exit_foo = 6
        call_foo = 7
        _exit = 8

        self.assertInCfg([
            (entry_foo, entry),
            (a, entry_foo),
            (_if, a),
            (yld_if, _if),
            (yld, _if),
            (yld, yld_if),  # Different from return
            (exit_foo, yld),
            (call_foo, exit_foo),
            (_exit, call_foo)
        ])

        yld_if_node = self.cfg.nodes[yld_if]
        self.assertEqual(yld_if_node.left_hand_side, 'yld_foo')
        self.assertEqual(yld_if_node.right_hand_side_variables, ['yld_foo'])
        yld_node = self.cfg.nodes[yld]
        self.assertEqual(yld_node.left_hand_side, 'yld_foo')
        self.assertEqual(yld_node.right_hand_side_variables, ['a', 'yld_foo'])
        self.assertEqual(self.cfg.nodes[call_foo].right_hand_side_variables, ['yld_foo'])

    def test_blackbox_call_after_if(self):
        path = 'examples/vulnerable_code/blackbox_call_after_if.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        ret_request = 1
        image_name_equals_call_1 = 2
        _if = 3
        image_name_equals_foo = 4
        blackbox_call = 5
        foo_equals_call_2 = 6
        ret_send_file = 7
        _exit = 8

        self.assertInCfg([
            (ret_request, entry),
            (image_name_equals_call_1, ret_request),
            (_if, image_name_equals_call_1),
            (image_name_equals_foo, _if),
            (blackbox_call, _if),
            (blackbox_call, image_name_equals_foo),
            (foo_equals_call_2, blackbox_call),
            (ret_send_file, foo_equals_call_2),
            (_exit, ret_send_file)
        ])

    def test_multiple_nested_user_defined_calls_after_if(self):
        path = 'examples/vulnerable_code/multiple_nested_user_defined_calls_after_if.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=39)

        entry = 0
        ret_request = 1
        image_name_equals_call_1 = 2
        _if = 3
        image_name_equals_foo = 4

        save_2_image_name = 5

        save_3_image_name = 6
        temp_3_first_inner_arg = 7
        inner_arg_equals_temp_3 = 8
        function_entry_first_inner = 9
        first_inner_ret_val_assign_1st = 10
        ret_first_inner = 11
        function_exit_first_inner = 12
        image_name_equals_first_inner_arg = 13
        call_3_equals_ret_first_inner = 14
        temp_2_first_arg_equals_call_3 = 15

        save_4_image_name = 16
        save_4_inner_ret_val = 17
        temp_4_inner_arg = 18
        inner_arg_equals_temp_4 = 19
        function_entry_second_inner = 20
        second_inner_ret_val_assign_2nd = 21
        ret_second_inner = 22
        function_exit_second_inner = 23
        image_name_equals_second_inner_arg = 24
        first_inner_ret_val_equals_save_4 = 25
        call_4_equals_ret_second_inner = 26

        temp_2_second_arg_equals_call_4 = 27
        first_arg_equals_temp = 28
        second_arg_equals_temp = 29
        function_entry_outer = 30
        outer_ret_val_assignment = 31
        ret_outer = 32
        function_exit_outer = 33
        image_name_restore = 34
        call_2_equals_ret_outer = 35

        foo_equals_call_2 = 36
        ret_send_file = 37
        _exit = 38

        self.assertInCfg([
            (ret_request, entry),
            (image_name_equals_call_1, ret_request),
            (_if, image_name_equals_call_1),
            (image_name_equals_foo, _if),
            (save_2_image_name, _if),
            (save_2_image_name, image_name_equals_foo),

            (save_3_image_name, save_2_image_name),
            (temp_3_first_inner_arg, save_3_image_name),
            (inner_arg_equals_temp_3, temp_3_first_inner_arg),
            (function_entry_first_inner, inner_arg_equals_temp_3),
            (first_inner_ret_val_assign_1st, function_entry_first_inner),
            (ret_first_inner, first_inner_ret_val_assign_1st),
            (function_exit_first_inner, ret_first_inner),
            (image_name_equals_first_inner_arg, function_exit_first_inner),
            (call_3_equals_ret_first_inner, image_name_equals_first_inner_arg),
            (save_4_image_name, call_3_equals_ret_first_inner),
            (temp_2_first_arg_equals_call_3, call_3_equals_ret_first_inner),
            (save_4_image_name, temp_2_first_arg_equals_call_3),
            (save_4_inner_ret_val, save_4_image_name),
            (temp_4_inner_arg, save_4_inner_ret_val),
            (inner_arg_equals_temp_4, temp_4_inner_arg),
            (function_entry_second_inner, inner_arg_equals_temp_4),
            (second_inner_ret_val_assign_2nd, function_entry_second_inner),
            (ret_second_inner, second_inner_ret_val_assign_2nd),
            (function_exit_second_inner, ret_second_inner),
            (image_name_equals_second_inner_arg, function_exit_second_inner),
            (first_inner_ret_val_equals_save_4, image_name_equals_second_inner_arg),
            (call_4_equals_ret_second_inner, first_inner_ret_val_equals_save_4),
            (temp_2_second_arg_equals_call_4, call_4_equals_ret_second_inner),
            (first_arg_equals_temp, temp_2_second_arg_equals_call_4),
            (second_arg_equals_temp, first_arg_equals_temp),
            (function_entry_outer, second_arg_equals_temp),
            (outer_ret_val_assignment, function_entry_outer),
            (ret_outer, outer_ret_val_assignment),
            (function_exit_outer, ret_outer),
            (image_name_restore, function_exit_outer),
            (call_2_equals_ret_outer, image_name_restore),

            (foo_equals_call_2, call_2_equals_ret_outer),
            (ret_send_file, foo_equals_call_2),
            (_exit, ret_send_file)
        ])

    def test_multiple_nested_blackbox_calls_after_for(self):
        path = 'examples/vulnerable_code/multiple_nested_blackbox_calls_after_for.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=11)

        entry = 0
        ret_request = 1
        image_name_equals_call_1 = 2
        _for = 3
        ret_print = 4
        inner_blackbox_call = 5
        second_inner_blackbox_call = 6
        outer_blackbox_call = 7
        foo_equals_call_3 = 8
        ret_send_file = 9
        _exit = 10

        self.assertInCfg([
            (ret_request, entry),
            (image_name_equals_call_1, ret_request),
            (_for, image_name_equals_call_1),
            (ret_print, _for),
            (_for, ret_print),
            (inner_blackbox_call, _for),
            (second_inner_blackbox_call, inner_blackbox_call),
            (outer_blackbox_call, second_inner_blackbox_call),
            (foo_equals_call_3, outer_blackbox_call),
            (ret_send_file, foo_equals_call_3),
            (_exit, ret_send_file)
        ])

    def test_multiple_blackbox_calls_in_user_defined_call_after_if(self):
        path = 'examples/vulnerable_code/multiple_blackbox_calls_in_user_defined_call_after_if.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=32)

        entry = 0
        ret_request = 1
        image_name_equals_call_1 = 2
        _if = 3
        image_name_equals_foo = 4
        # Function call starts here
        save_2_image_name = 5

        ret_scrypt_first = 6
        temp_2_first_arg = 7
        save_4_image_name = 8
        temp_4_inner_arg = 9
        inner_arg_equals_temp_4 = 10
        function_entry_second_inner = 11
        inner_ret_val_equals_inner_arg_2nd = 12
        ret_second_inner = 13
        function_exit_second_inner = 14

        image_name_equals_save_4 = 15
        call_4_equals_ret_second_inner = 16
        temp_2_second_arg = 17

        ret_scrypt_third = 18
        temp_2_third_arg_equals_call_5 = 19
        first_arg_equals_temp = 20
        second_arg_equals_temp = 21
        third_arg_equals_temp = 22
        function_entry_outer = 23
        outer_ret_val = 24
        ret_outer = 25
        exit_outer = 26
        image_name_equals_save_2 = 27
        call_2_equals_ret_outer = 28
        foo_equals_call_2 = 29
        ret_send_file = 30
        _exit = 31

        self.assertInCfg([
            (save_2_image_name, _if),
            (save_4_image_name, ret_scrypt_first),
            (ret_scrypt_third, call_4_equals_ret_second_inner),
            (ret_request, entry),
            (image_name_equals_call_1, ret_request),
            (_if, image_name_equals_call_1),
            (image_name_equals_foo, _if),
            (save_2_image_name, image_name_equals_foo),
            (ret_scrypt_first, save_2_image_name),
            (temp_2_first_arg, ret_scrypt_first),
            (save_4_image_name, temp_2_first_arg),
            (temp_4_inner_arg, save_4_image_name),
            (inner_arg_equals_temp_4, temp_4_inner_arg),
            (function_entry_second_inner, inner_arg_equals_temp_4),
            (inner_ret_val_equals_inner_arg_2nd, function_entry_second_inner),
            (ret_second_inner, inner_ret_val_equals_inner_arg_2nd),
            (function_exit_second_inner, ret_second_inner),
            (image_name_equals_save_4, function_exit_second_inner),
            (call_4_equals_ret_second_inner, image_name_equals_save_4),
            (temp_2_second_arg, call_4_equals_ret_second_inner),
            (ret_scrypt_third, temp_2_second_arg),
            (temp_2_third_arg_equals_call_5, ret_scrypt_third),
            (first_arg_equals_temp, temp_2_third_arg_equals_call_5),
            (second_arg_equals_temp, first_arg_equals_temp),
            (third_arg_equals_temp, second_arg_equals_temp),
            (function_entry_outer, third_arg_equals_temp),
            (outer_ret_val, function_entry_outer),
            (ret_outer, outer_ret_val),
            (exit_outer, ret_outer),
            (image_name_equals_save_2, exit_outer),
            (call_2_equals_ret_outer, image_name_equals_save_2),
            (foo_equals_call_2, call_2_equals_ret_outer),
            (ret_send_file, foo_equals_call_2),
            (_exit, ret_send_file)
        ])

    def test_multiple_user_defined_calls_in_blackbox_call_after_if(self):
        path = 'examples/vulnerable_code/multiple_user_defined_calls_in_blackbox_call_after_if.py'
        self.cfg_create_from_file(path)

        self.assert_length(self.cfg.nodes, expected_length=30)

        entry = 0
        ret_request = 1
        image_name_equals_call_1 = 2
        _if = 3
        image_name_equals_foo = 4
        # Function call starts here
        save_3_image_name = 5
        temp_3_first_arg = 6
        first_arg_equals_temp = 7
        function_entry_first_inner = 8
        first_ret_val_equals_first = 9
        ret_first_inner = 10
        function_exit_first_inner = 11
        image_name_equals_save_4 = 12
        call_3_equals_ret_first_inner = 13
        call_4_equals_ret_second_inner = 14
        save_5_image_name = 15
        save_5_first_ret_val = 16
        temp_5_second_arg = 17
        second_arg_equals_temp = 18
        function_entry_third_inner = 19
        third_ret_val = 20
        ret_third_inner = 21
        exit_third_inner = 22
        image_name_equals_save_5 = 23
        first_ret_val_equals_save_5 = 24
        call_5_equals_ret_third_inner = 25
        call_2_equals_ret_outer = 26
        foo_equals_call_2 = 27
        ret_send_file = 28
        _exit = 29

        self.assertInCfg([(save_3_image_name, _if),
                          (ret_request, entry),
                          (image_name_equals_call_1, ret_request),
                          (_if, image_name_equals_call_1),
                          (image_name_equals_foo, _if),
                          (save_3_image_name, image_name_equals_foo),
                          (temp_3_first_arg, save_3_image_name),
                          (first_arg_equals_temp, temp_3_first_arg),
                          (function_entry_first_inner, first_arg_equals_temp),
                          (first_ret_val_equals_first, function_entry_first_inner),
                          (ret_first_inner, first_ret_val_equals_first),
                          (function_exit_first_inner, ret_first_inner),
                          (image_name_equals_save_4, function_exit_first_inner),
                          (call_3_equals_ret_first_inner, image_name_equals_save_4),
                          (call_4_equals_ret_second_inner, call_3_equals_ret_first_inner),
                          (save_5_image_name, call_4_equals_ret_second_inner),
                          (save_5_first_ret_val, save_5_image_name),
                          (temp_5_second_arg, save_5_first_ret_val),
                          (second_arg_equals_temp, temp_5_second_arg),
                          (function_entry_third_inner, second_arg_equals_temp),
                          (third_ret_val, function_entry_third_inner),
                          (ret_third_inner, third_ret_val),
                          (exit_third_inner, ret_third_inner),
                          (image_name_equals_save_5, exit_third_inner),
                          (first_ret_val_equals_save_5, image_name_equals_save_5),
                          (call_5_equals_ret_third_inner, first_ret_val_equals_save_5),
                          (call_2_equals_ret_outer, call_5_equals_ret_third_inner),
                          (foo_equals_call_2, call_2_equals_ret_outer),
                          (ret_send_file, foo_equals_call_2),
                          (_exit, ret_send_file)
                          ])

    def test_function_line_numbers_2(self):
        path = 'examples/example_inputs/simple_function_with_return.py'
        self.cfg_create_from_file(path)

        assignment_with_function = self.cfg.nodes[1]

        self.assertLineNumber(assignment_with_function, 9)

    def test_multiple_parameters(self):
        path = 'examples/example_inputs/multiple_parameters_function.py'

        self.cfg_create_from_file(path)

        length = len(self.cfg.nodes)

        self.assertEqual(length, 21)

        self.assertInCfg(
            list(
                zip(
                    range(1, length), range(length)
                )
            )
        )

    def test_call_on_call(self):
        path = 'examples/example_inputs/call_on_call.py'
        self.cfg_create_from_file(path)

    def test_recursive_function(self):
        path = 'examples/example_inputs/recursive.py'
        self.cfg_create_from_file(path)
        recursive_call = self.cfg.nodes[7]
        assert recursive_call.label == '~call_3 = ret_rec(wat)'
        assert isinstance(recursive_call, BBorBInode)  # Not RestoreNode


class CFGCallWithAttributeTest(CFGBaseTestCase):
    def setUp(self):
        self.cfg_create_from_file('examples/example_inputs/call_with_attribute.py')

    def test_call_with_attribute(self):
        length = 14
        self.assert_length(self.cfg.nodes, expected_length=length)

        call = self.cfg.nodes[2]
        self.assertEqual(call.label, "~call_1 = ret_request.args.get('param', 'not set')")

        self.assertInCfg(
            list(
                zip(
                    range(1, length), range(length)
                )
            )
        )

    def test_call_with_attribute_line_numbers(self):
        call = self.cfg.nodes[2]

        self.assertLineNumber(call, 5)


class CFGBreak(CFGBaseTestCase):
    """Break in while and for and other places"""
    def test_break(self):
        self.cfg_create_from_file('examples/example_inputs/while_break.py')

        self.assert_length(self.cfg.nodes, expected_length=8)

        entry = 0
        _while = 1
        _if = 2
        print_x = 3
        _break = 4
        print_hest = 5
        print_next = 6
        _exit = 7

        # (foo, bar) means foo <- bar
        self.assertInCfg([(_while, entry),
                          (_while, print_hest),
                          (_if, _while),
                          (print_x, _if),
                          (_break, print_x),
                          (print_hest, _if),
                          (print_next, _while),
                          (print_next, _break),
                          (_exit, print_next)])


class CFGNameConstant(CFGBaseTestCase):
    def setUp(self):
        self.cfg_create_from_file('examples/example_inputs/name_constant.py')

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


class CFGAsync(CFGBaseTestCase):
    def test_await_keyword_treated_as_if_absent(self):
        self.cfg_create_from_file('examples/example_inputs/asynchronous.py')
        enter_g = 8
        call_x = 9
        ret_g = 10
        exit_g = 11
        call_ret_val = 12
        set_z_to_g_ret_val = 13

        for i in range(enter_g, set_z_to_g_ret_val + 1):
            self.assertIn(self.cfg.nodes[i], self.cfg.nodes[i + 1].ingoing)
            self.assertIn(self.cfg.nodes[i + 1], self.cfg.nodes[i].outgoing)

        self.assertIsInstance(self.cfg.nodes[enter_g], EntryOrExitNode)
        self.assertEqual(self.cfg.nodes[call_x].label, '~call_3 = ret_x()')
        self.assertEqual(self.cfg.nodes[ret_g].label, 'ret_g = ~call_3')
        self.assertIsInstance(self.cfg.nodes[exit_g], EntryOrExitNode)
        self.assertEqual(self.cfg.nodes[call_ret_val].label, '~call_2 = ret_g')
        self.assertEqual(self.cfg.nodes[set_z_to_g_ret_val].label, 'z = ~call_2')


class CFGName(CFGBaseTestCase):
    """Test is Name nodes are properly handled in different contexts"""

    def test_name_if(self):
        self.cfg_create_from_file('examples/example_inputs/name_if.py')

        self.assert_length(self.cfg.nodes, expected_length=5)
        self.assertEqual(self.cfg.nodes[2].label, 'if x:')

    def test_name_for(self):
        self.cfg_create_from_file('examples/example_inputs/name_for.py')

        self.assert_length(self.cfg.nodes, expected_length=4)
        self.assertEqual(self.cfg.nodes[1].label, 'for x in l:')


class CFGFunctionChain(CFGBaseTestCase):
    def test_simple(self):
        self.cfg_create_from_ast(
            ast.parse('a = b.c(z)')
        )
        middle_nodes = self.cfg.nodes[1:-1]
        self.assert_length(middle_nodes, expected_length=2)
        self.assertEqual(middle_nodes[0].label, '~call_1 = ret_b.c(z)')
        self.assertEqual(middle_nodes[0].func_name, 'b.c')
        self.assertCountEqual(middle_nodes[0].right_hand_side_variables, ['z', 'b'])

    def test_chain(self):
        self.cfg_create_from_ast(
            ast.parse('a = b.xxx.c(z).d(y)')
        )
        middle_nodes = self.cfg.nodes[1:-1]
        self.assert_length(middle_nodes, expected_length=4)

        self.assertEqual(middle_nodes[0].left_hand_side, '~call_1')
        self.assertCountEqual(middle_nodes[0].right_hand_side_variables, ['b', 'z'])
        self.assertEqual(middle_nodes[0].label, '~call_1 = ret_b.xxx.c(z)')

        self.assertEqual(middle_nodes[1].left_hand_side, '__chain_tmp_1')
        self.assertCountEqual(middle_nodes[1].right_hand_side_variables, ['~call_1'])

        self.assertEqual(middle_nodes[2].left_hand_side, '~call_2')
        self.assertCountEqual(middle_nodes[2].right_hand_side_variables, ['__chain_tmp_1', 'y'])

        self.assertEqual(middle_nodes[3].left_hand_side, 'a')
        self.assertCountEqual(middle_nodes[3].right_hand_side_variables, ['~call_2'])
