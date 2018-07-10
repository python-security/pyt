from .cfg_base_test_case import CFGBaseTestCase

from pyt.core.node_types import (
    EntryOrExitNode,
    Node
)


EXAMPLES = 'examples/vulnerable_code_with_expressions/'

class CFGExprTest(CFGBaseTestCase):
    def test_connecting_control_flow_exprs_in_connect_expressions(self):
        self.cfg_create_from_file(
            EXAMPLES + 'connecting_control_flow_exprs_in_connect_expressions.py'
        )

        self.assert_length(self.cfg.nodes, expected_length=9)

        for i, n in enumerate(self.cfg.nodes):
            print(f'#{i} is {n}')
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
            (call_2_and_crazy, first_and_biggest_bool_op),
            (call_3_and_foo, first_and_biggest_bool_op),
            (call_4_req_get_The, first_and_biggest_bool_op),

            (call_1_ret_redirect, call_4_req_get_The),

            (_exit, call_1_ret_redirect),
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
