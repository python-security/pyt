from .cfg_base_test_case import CFGBaseTestCase

from pyt.core.node_types import (
    EntryOrExitNode,
    Node
)


EXAMPLES = 'examples/vulnerable_code_with_expressions/'

class CFGExprTest(CFGBaseTestCase):
    def test_assignment_before_blackbox_call(self):
        """
        This tests
        stmt_star_handler ->
         connect_nodes ->
          elif isinstance(next_node, (AssignmentCallNode, BBorBInode)): ->
           _get_inner_most_expression
        """
        self.cfg_create_from_file(
            EXAMPLES + 'assignment_before_blackbox_call.py'
        )

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        self.assert_length(self.cfg.nodes, expected_length=5)

        entry = 0
        h_equals_5 = 1
        h_arg = 2
        call_1_some_function = 3
        _exit = 4

        self.assertInCfg([
            (h_equals_5, entry),
            (h_arg, h_equals_5),
            (call_1_some_function, h_arg),
            (_exit, call_1_some_function),
        ])

    def test_assignment_before_blackbox_call_assignment(self):
        """
        This tests
        stmt_star_handler ->
         connect_nodes ->
          elif isinstance(next_node, (AssignmentCallNode, BBorBInode)): ->
           if isinstance(next_node, AssignmentCallNode):
           _get_inner_most_expression
        """
        self.cfg_create_from_file(
            EXAMPLES + 'assignment_before_blackbox_call_assignment.py'
        )

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        h_equals_5 = 1
        h_arg = 2
        call_1_some_function = 3
        foo_equals_call_1 = 4
        _exit = 5

        self.assertInCfg([
            (h_equals_5, entry),
            (h_arg, h_equals_5),
            (call_1_some_function, h_arg),
            (foo_equals_call_1, call_1_some_function),
            (_exit, foo_equals_call_1),
        ])

    def test_if_statement_before_blackbox_call(self):
        """
        This tests
        stmt_star_handler ->
         connect_nodes ->
          _connect_control_flow_node ->
           elif isinstance(next_node, (AssignmentCallNode, BBorBInode)): ->
            _get_inner_most_expression
        """
        self.cfg_create_from_file(
            EXAMPLES + 'if_statement_before_blackbox_call.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=6)

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        entry = 0
        if_predicate = 1
        h_equals_5 = 2
        h_arg = 3
        call_1_some_function = 4
        _exit = 5

        self.assertInCfg([
            (if_predicate, entry),

            (h_equals_5, if_predicate),

            (h_arg, if_predicate),
            (h_arg, h_equals_5),

            (call_1_some_function, h_arg),

            (_exit, call_1_some_function),
        ])

    def test_if_statement_before_blackbox_call_assignment(self):
        """
        This tests
        stmt_star_handler ->
         connect_nodes ->
          _connect_control_flow_node ->
           elif isinstance(next_node, (AssignmentCallNode, BBorBInode)): ->
            if isinstance(next_node, AssignmentCallNode):
             _get_inner_most_expression
        """
        self.cfg_create_from_file(
            EXAMPLES + 'if_statement_before_blackbox_call_assignment.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=7)

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        entry = 0
        if_predicate = 1
        h_equals_5 = 2
        h_arg = 3
        call_1_some_function = 4
        foo_equals_call_1 = 5
        _exit = 6

        self.assertInCfg([
            (if_predicate, entry),

            (h_equals_5, if_predicate),

            (h_arg, if_predicate),
            (h_arg, h_equals_5),

            (call_1_some_function, h_arg),

            (foo_equals_call_1, call_1_some_function),

            (_exit, foo_equals_call_1),
        ])

    def test_blackbox_library_call(self):
        self.cfg_create_from_file(
            EXAMPLES + 'blackbox_library_call.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=11)

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        entry = 0
        call_1_req_get_suggestion = 1
        param_equal_call_1 = 2
        param = 3
        call_2_encrypt = 4
        command_equal_call_2 = 5
        hey_equal_command = 6
        hey = 7
        shell_equal_true = 8
        call_3_equal_subprocess_call = 9
        _exit = 10

        self.assertInCfg([
            (call_1_req_get_suggestion, entry),

            (param_equal_call_1, call_1_req_get_suggestion),
            
            (call_2_encrypt, param_equal_call_1),

            (command_equal_call_2, call_2_encrypt),

            (hey_equal_command, command_equal_call_2),

            (hey, hey_equal_command),

            (shell_equal_true, hey),

            (call_3_equal_subprocess_call, shell_equal_true),

            (_exit, call_3_equal_subprocess_call),
        ])

    def test_connecting_control_flow_exprs_in_connect_expressions(self):
        self.cfg_create_from_file(
            EXAMPLES + 'connecting_control_flow_exprs_in_connect_expressions.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=9)

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        entry = 0
        first_and_biggest_bool_op = 1
        call_2_and_crazy = 2
        call_2_req_get_Laundry = 3
        call_3_and_foo = 4
        call_3_req_get_French = 5
        call_4_req_get_The = 6
        call_1_ret_redirect = 7
        _exit = 8

        self.assertInCfg([
            (first_and_biggest_bool_op, entry),

            (call_2_and_crazy, first_and_biggest_bool_op),

            # (call_2_req_get_Laundry, call_2_and_crazy),  # On purpose

            (call_3_and_foo, first_and_biggest_bool_op),

            # (call_3_req_get_French, call_3_and_foo),  # On purpose

            (call_4_req_get_The, first_and_biggest_bool_op),

            (call_1_ret_redirect, call_4_req_get_The),

            (_exit, call_1_ret_redirect),
        ])

    def test_sink_as_just_the_call(self):
        self.cfg_create_from_file(
            EXAMPLES + 'sink_as_just_the_call.py'
        )

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')


        self.assert_length(self.cfg.nodes, expected_length=6)

        entry = 0
        call_1_req_get_The = 1
        hey_equal_call_1 = 2
        hey = 3
        call_2_ret_redirect = 4
        _exit = 5

        self.assertInCfg([
            (call_1_req_get_The, entry),

            (hey_equal_call_1, call_1_req_get_The),

            (hey, hey_equal_call_1),

            (call_2_ret_redirect, hey),

            (_exit, call_2_ret_redirect)
        ])

    def test_sink_on_rhs(self):
        self.cfg_create_from_file(
            EXAMPLES + 'sink_on_rhs.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=7)

        for i, n in enumerate(self.cfg.nodes):
            print(f'\n\n\n\n#{i} is {n}')
            print(f'n.ingoing is {n.ingoing}')
            print(f'n.outgoing is {n.outgoing}')

        entry = 0
        call_1_req_get_The = 1
        french_equal_call_1 = 2
        french = 3
        call_2_ret_redirect = 4
        laundry_equal_call_2 = 5
        _exit = 6

        self.assertInCfg([
            (call_1_req_get_The, entry),

            (french_equal_call_1, call_1_req_get_The),

            (french, french_equal_call_1),

            (call_2_ret_redirect, french),

            (laundry_equal_call_2, call_2_ret_redirect),

            (_exit, laundry_equal_call_2)
        ])

    def test_last_and_not_tainted(self):
        self.cfg_create_from_file(
            EXAMPLES + 'last_var_in_and_is_not_tainted.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        first_if_exp_test_if_Hey_or_You = 1
        call_2_req_get_The = 2
        second_if_exp_test_if_Foo = 3
        call_3_req_get_French = 4
        and_bool_op = 5
        call_4_req_get_Aces = 6
        call_1_ret_redirect = 7
        _exit = 8

        self.assertInCfg([
            (first_if_exp_test_if_Hey_or_You, entry),

            (call_2_req_get_The, first_if_exp_test_if_Hey_or_You),
            (second_if_exp_test_if_Foo, first_if_exp_test_if_Hey_or_You),

            (call_1_ret_redirect, call_2_req_get_The),

            (call_3_req_get_French, second_if_exp_test_if_Foo),
            (and_bool_op, second_if_exp_test_if_Foo),

            (call_1_ret_redirect, call_3_req_get_French),

            (_exit, call_1_ret_redirect)
        ])

    def test_last_and_tainted(self):
        self.cfg_create_from_file(
            EXAMPLES + 'last_var_in_and_is_tainted.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=9)

        entry = 0
        first_if_exp_test_if_Hey_or_You = 1
        call_2_req_get_The = 2
        second_if_exp_test_if_Foo = 3
        call_3_req_get_French = 4
        and_bool_op = 5
        call_4_req_get_Aces = 6
        call_1_ret_redirect = 7
        _exit = 8

        self.assertInCfg([
            (first_if_exp_test_if_Hey_or_You, entry),

            (call_2_req_get_The, first_if_exp_test_if_Hey_or_You),
            (second_if_exp_test_if_Foo, first_if_exp_test_if_Hey_or_You),

            (call_1_ret_redirect, call_2_req_get_The),

            (call_3_req_get_French, second_if_exp_test_if_Foo),
            (and_bool_op, second_if_exp_test_if_Foo),

            (call_1_ret_redirect, call_3_req_get_French),

            (call_4_req_get_Aces, and_bool_op),  # Connected this time

            (call_1_ret_redirect, call_4_req_get_Aces),  # Connected this time

            (_exit, call_1_ret_redirect)
        ])
