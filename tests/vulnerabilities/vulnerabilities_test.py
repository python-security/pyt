import ast
import os

from .vulnerabilities_base_test_case import VulnerabilitiesBaseTestCase

from pyt.analysis.constraint_table import initialize_constraint_table
from pyt.analysis.fixed_point import analyse
from pyt.core.node_types import Node
from pyt.usage import (
    default_blackbox_mapping_file,
    default_trigger_word_file
)
from pyt.vulnerabilities import (
    find_vulnerabilities,
    vulnerabilities
)
from pyt.vulnerabilities.trigger_definitions_parser import (
    parse,
    Sink,
    Source,
)
from pyt.web_frameworks import (
    FrameworkAdaptor,
    is_django_view_function,
    is_flask_route_function,
    is_function
)


class EngineTest(VulnerabilitiesBaseTestCase):
    def test_parse(self):
        definitions = parse(
            trigger_word_file=os.path.join(
                os.getcwd(),
                'pyt',
                'vulnerability_definitions',
                'test_triggers.pyt'
            )
        )

        self.assert_length(definitions.sources, expected_length=1)
        self.assert_length(definitions.sinks, expected_length=3)
        self.assert_length(definitions.sinks[0].sanitisers, expected_length=1)
        self.assert_length(definitions.sinks[1].sanitisers, expected_length=3)

    def test_label_contains(self):
        cfg_node = Node('label', None, line_number=None, path=None)
        trigger_words = [Source('get')]
        list_ = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(list_, expected_length=0)

        cfg_node = Node('request.get("stefan")', None, line_number=None, path=None)
        trigger_words = [Sink('request'), Source('get')]
        list_ = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(list_, expected_length=2)

        trigger_node_1 = list_[0]
        trigger_node_2 = list_[1]
        self.assertEqual(trigger_node_1.trigger_word, 'request')
        self.assertEqual(trigger_node_1.cfg_node, cfg_node)
        self.assertEqual(trigger_node_2.trigger_word, 'get')
        self.assertEqual(trigger_node_2.cfg_node, cfg_node)

        cfg_node = Node('request.get("stefan")', None, line_number=None, path=None)
        trigger_words = [Source('get'), Source('get'), Sink('get(')]
        list_ = list(vulnerabilities.label_contains(cfg_node, trigger_words))
        self.assert_length(list_, expected_length=3)

    def test_find_triggers(self):
        self.cfg_create_from_file('examples/vulnerable_code/XSS.py')

        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_flask_route_function)

        XSS1 = cfg_list[1]
        trigger_words = [Source('get')]

        list_ = vulnerabilities.find_triggers(
            XSS1.nodes,
            trigger_words,
            nosec_lines=set()
        )
        self.assert_length(list_, expected_length=1)

    def test_find_sanitiser_nodes(self):
        cfg_node = Node(None, None, line_number=None, path=None)
        sanitiser_tuple = vulnerabilities.Sanitiser('escape', cfg_node)
        sanitiser = 'escape'

        result = list(vulnerabilities.find_sanitiser_nodes(sanitiser, [sanitiser_tuple]))
        self.assert_length(result, expected_length=1)
        self.assertEqual(result[0], cfg_node)

    def test_build_sanitiser_node_dict(self):
        self.cfg_create_from_file('examples/vulnerable_code/XSS_sanitised.py')
        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_flask_route_function)

        cfg = cfg_list[1]

        cfg_node = Node(None, None, line_number=None, path=None)
        sink = Sink.from_json('replace', {'sanitisers': ['escape']})
        sinks_in_file = [vulnerabilities.TriggerNode(sink, cfg_node)]

        sanitiser_dict = vulnerabilities.build_sanitiser_node_dict(cfg, sinks_in_file)
        self.assert_length(sanitiser_dict, expected_length=1)
        self.assertIn('escape', sanitiser_dict.keys())

        self.assertEqual(sanitiser_dict['escape'][0], cfg.nodes[3])

    def run_analysis(
        self,
        path=None,
        adaptor_function=is_flask_route_function,
        trigger_file=default_trigger_word_file,
    ):
        if path:
            self.cfg_create_from_file(path)
        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], adaptor_function)
        initialize_constraint_table(cfg_list)

        analyse(cfg_list)

        return find_vulnerabilities(
            cfg_list,
            default_blackbox_mapping_file,
            trigger_file,
        )

    def test_find_vulnerabilities_assign_other_var(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_assign_to_other_var.py')
        self.assert_length(vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_inter_command_injection(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/inter_command_injection.py')
        self.assert_length(vulnerabilities, expected_length=1)

    def test_find_vulnerabilities_inter_command_injection_2(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/inter_command_injection_2.py')
        self.assert_length(vulnerabilities, expected_length=1)

    def test_XSS_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS.py
             > User input at line 6, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/XSS.py
                 > Line 6: param = ~call_1
            File: examples/vulnerable_code/XSS.py
             > reaches line 9, sink "replace(":
                ~call_4 = ret_html.replace('{{ param }}', param)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_command_injection_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/command_injection.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/command_injection.py
             > User input at line 15, source "form[":
                param = request.form['suggestion']
            Reassigned in:
                File: examples/vulnerable_code/command_injection.py
                 > Line 16: command = 'echo ' + param + ' >> ' + 'menu.txt'
            File: examples/vulnerable_code/command_injection.py
             > reaches line 18, sink "subprocess.call(":
                ~call_1 = ret_subprocess.call(command, shell=True)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_path_traversal_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/path_traversal.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/path_traversal.py
             > User input at line 15, source "request.args.get(":
                 ~call_1 = ret_flask.request.args.get('image_name')
            Reassigned in:
                File: examples/vulnerable_code/path_traversal.py
                 > Line 15: image_name = ~call_1
                File: examples/vulnerable_code/path_traversal.py
                 > Line 6: save_2_image_name = image_name
                File: examples/vulnerable_code/path_traversal.py
                 > Line 10: save_3_image_name = image_name
                File: examples/vulnerable_code/path_traversal.py
                 > Line 10: image_name = save_3_image_name
                File: examples/vulnerable_code/path_traversal.py
                 > Line 19: temp_2_other_arg = image_name
                File: examples/vulnerable_code/path_traversal.py
                 > Line 6: other_arg = temp_2_other_arg
                File: examples/vulnerable_code/path_traversal.py
                 > Line 7: outer_ret_val = outer_arg + 'hey' + other_arg
                File: examples/vulnerable_code/path_traversal.py
                 > Line 8: ret_outer = outer_ret_val
                File: examples/vulnerable_code/path_traversal.py
                 > Line 19: ~call_2 = ret_outer
                File: examples/vulnerable_code/path_traversal.py
                 > Line 19: foo = ~call_2
            File: examples/vulnerable_code/path_traversal.py
             > reaches line 20, sink "send_file(":
                ~call_4 = ret_flask.send_file(foo)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_ensure_saved_scope(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/ensure_saved_scope.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/ensure_saved_scope.py
             > User input at line 15, source "request.args.get(":
                 ~call_1 = ret_flask.request.args.get('image_name')
            Reassigned in:
                File: examples/vulnerable_code/ensure_saved_scope.py
                 > Line 15: image_name = ~call_1
                File: examples/vulnerable_code/ensure_saved_scope.py
                 > Line 6: save_2_image_name = image_name
                File: examples/vulnerable_code/ensure_saved_scope.py
                 > Line 10: save_3_image_name = image_name
            File: examples/vulnerable_code/ensure_saved_scope.py
             > reaches line 20, sink "send_file(":
                ~call_4 = ret_flask.send_file(image_name)
        """
        self.assertAlphaEqual(
            vulnerability_description,
            EXPECTED_VULNERABILITY_DESCRIPTION
        )

    def test_path_traversal_sanitised_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/path_traversal_sanitised.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/path_traversal_sanitised.py
             > User input at line 8, source "request.args.get(":
                 ~call_1 = ret_flask.request.args.get('image_name')
            Reassigned in:
                File: examples/vulnerable_code/path_traversal_sanitised.py
                 > Line 8: image_name = ~call_1
                File: examples/vulnerable_code/path_traversal_sanitised.py
                 > Line 10: ~call_2 = ret_image_name.replace('..', '')
                File: examples/vulnerable_code/path_traversal_sanitised.py
                 > Line 10: image_name = ~call_2
                File: examples/vulnerable_code/path_traversal_sanitised.py
                 > Line 12: ~call_4 = ret_os.path.join(~call_5, image_name)
            File: examples/vulnerable_code/path_traversal_sanitised.py
             > reaches line 12, sink "send_file(":
                ~call_3 = ret_flask.send_file(~call_4)
            This vulnerability is sanitised by:  Label: ~call_2 = ret_image_name.replace('..', '')
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_path_traversal_sanitised_2_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/path_traversal_sanitised_2.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/path_traversal_sanitised_2.py
             > User input at line 8, source "request.args.get(":
                 ~call_1 = ret_flask.request.args.get('image_name')
            Reassigned in:
                File: examples/vulnerable_code/path_traversal_sanitised_2.py
                 > Line 8: image_name = ~call_1
                File: examples/vulnerable_code/path_traversal_sanitised_2.py
                 > Line 12: ~call_3 = ret_os.path.join(~call_4, image_name)
            File: examples/vulnerable_code/path_traversal_sanitised_2.py
             > reaches line 12, sink "send_file(":
                ~call_2 = ret_flask.send_file(~call_3)
            This vulnerability is potentially sanitised by:  Label: if '..' in image_name:
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_sql_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/sql/sqli.py')
        self.assert_length(vulnerabilities, expected_length=3)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/sql/sqli.py
             > User input at line 26, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/sql/sqli.py
                 > Line 26: param = ~call_1
            File: examples/vulnerable_code/sql/sqli.py
             > reaches line 27, sink "execute(":
                ~call_2 = ret_db.engine.execute(param)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_form_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_form.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_form.py
             > User input at line 14, source "form[":
                data = request.form['my_text']
            File: examples/vulnerable_code/XSS_form.py
             > reaches line 15, sink "replace(":
                ~call_2 = ret_html1.replace('{{ data }}', data)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_url_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_url.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_url.py
             > User input at line 4, source "Framework function URL parameter":
                url
            Reassigned in:
                File: examples/vulnerable_code/XSS_url.py
                 > Line 6: param = url
            File: examples/vulnerable_code/XSS_url.py
             > reaches line 9, sink "replace(":
                ~call_3 = ret_html.replace('{{ param }}', param)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_no_vuln_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_no_vuln.py')
        self.assert_length(vulnerabilities, expected_length=0)

    def test_XSS_reassign_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_reassign.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_reassign.py
             > User input at line 6, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/XSS_reassign.py
                 > Line 6: param = ~call_1
                File: examples/vulnerable_code/XSS_reassign.py
                 > Line 8: param = param + ''
            File: examples/vulnerable_code/XSS_reassign.py
             > reaches line 11, sink "replace(":
                ~call_4 = ret_html.replace('{{ param }}', param)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_sanitised_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_sanitised.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_sanitised.py
             > User input at line 7, source "request.args.get(":
                 ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/XSS_sanitised.py
                 > Line 7: param = ~call_1
                File: examples/vulnerable_code/XSS_sanitised.py
                 > Line 9: ~call_2 = ret_flask.Markup.escape(param)
                File: examples/vulnerable_code/XSS_sanitised.py
                 > Line 9: param = ~call_2
            File: examples/vulnerable_code/XSS_sanitised.py
             > reaches line 12, sink "replace(":
                ~call_5 = ret_html.replace('{{ param }}', param)
            This vulnerability is sanitised by:  Label: ~call_2 = ret_flask.Markup.escape(param)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_variable_assign_no_vuln_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_variable_assign_no_vuln.py')
        self.assert_length(vulnerabilities, expected_length=0)

    def test_XSS_variable_assign_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_variable_assign.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_variable_assign.py
             > User input at line 6, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/XSS_variable_assign.py
                 > Line 6: param = ~call_1
                File: examples/vulnerable_code/XSS_variable_assign.py
                 > Line 8: other_var = param + ''
            File: examples/vulnerable_code/XSS_variable_assign.py
             > reaches line 11, sink "replace(":
                ~call_4 = ret_html.replace('{{ param }}', other_var)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_XSS_variable_multiple_assign_result(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/XSS_variable_multiple_assign.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vulnerability_description = str(vulnerabilities[0])
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/XSS_variable_multiple_assign.py
             > User input at line 6, source "request.args.get(":
                ~call_1 = ret_flask.request.args.get('param', 'not set')
            Reassigned in:
                File: examples/vulnerable_code/XSS_variable_multiple_assign.py
                 > Line 6: param = ~call_1
                File: examples/vulnerable_code/XSS_variable_multiple_assign.py
                 > Line 8: other_var = param + ''
                File: examples/vulnerable_code/XSS_variable_multiple_assign.py
                 > Line 10: not_the_same_var = '' + other_var
                File: examples/vulnerable_code/XSS_variable_multiple_assign.py
                 > Line 12: another_one = not_the_same_var + ''
            File: examples/vulnerable_code/XSS_variable_multiple_assign.py
             > reaches line 15, sink "replace(":
                ~call_4 = ret_html.replace('{{ param }}', another_one)
        """

        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_yield(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/yield.py')
        self.assert_length(vulnerabilities, expected_length=1)
        vuln = vulnerabilities[0]
        self.assertEqual(vuln.source.left_hand_side, "yld_things_to_run")
        self.assertIn("yld_things_to_run", vuln.source.right_hand_side_variables)
        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/yield.py
             > User input at line 9, source "request.get_json(":
                     yld_things_to_run += request.get_json()['commands']
            Reassigned in:
                    File: examples/vulnerable_code/yield.py
                     > Line 15: ~call_2 = yld_things_to_run
                    File: examples/vulnerable_code/yield.py
                     > Line 15: ~call_1 = ret_'; '.join(~call_2)
                    File: examples/vulnerable_code/yield.py
                     > Line 15: script = ~call_1
            File: examples/vulnerable_code/yield.py
             > reaches line 16, sink "subprocess.call(":
                    ~call_3 = ret_subprocess.call(script, shell=True)
            This vulnerability is unknown due to:  Label: ~call_1 = ret_'; '.join(~call_2)
        """

        self.assertAlphaEqual(str(vuln), EXPECTED_VULNERABILITY_DESCRIPTION)

    def test_method_of_taint(self):
        def assert_vulnerable(fixture):
            tree = ast.parse('TAINT = request.args.get("")\n' + fixture + '\nexecute(result)')
            self.cfg_create_from_ast(tree)
            vulnerabilities = self.run_analysis()
            self.assert_length(vulnerabilities, expected_length=1, msg=fixture)

        assert_vulnerable('result = TAINT')
        assert_vulnerable('result = TAINT.lower()')
        assert_vulnerable('result = str(TAINT)')
        assert_vulnerable('result = str(TAINT.lower())')
        assert_vulnerable('result = repr(str("%s" % TAINT.lower().upper()))')
        assert_vulnerable('result = repr(str("{}".format(TAINT.lower())))')

    def test_recursion(self):
        # Really this file only has one vulnerability, but for now it's safer to keep the false positive.
        vulnerabilities = self.run_analysis('examples/vulnerable_code/recursive.py')
        self.assert_length(vulnerabilities, expected_length=2)

    def test_list_append_taints_list(self):
        vulnerabilities = self.run_analysis(
            'examples/vulnerable_code/list_append.py',
            adaptor_function=is_function,
        )
        self.assert_length(vulnerabilities, expected_length=1)

    def test_import_bb_or_bi_with_alias(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/command_injection_with_aliases.py')

        EXPECTED_SINK_TRIGGER_WORDS = [
            'os.system(',
            'os.system(',
            'os.system(',
            'os.system(',
            'subprocess.call(',
            'subprocess.Popen('
        ]

        for vuln, expected_sink_trigger_word in zip(vulnerabilities, EXPECTED_SINK_TRIGGER_WORDS):
            self.assertEqual(vuln.sink_trigger_word, expected_sink_trigger_word)


class EngineDjangoTest(VulnerabilitiesBaseTestCase):
    def run_analysis(self, path):
        self.cfg_create_from_file(path)
        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_django_view_function)
        initialize_constraint_table(cfg_list)

        analyse(cfg_list)

        trigger_word_file = os.path.join(
            'pyt',
            'vulnerability_definitions',
            'django_trigger_words.pyt'
        )

        return find_vulnerabilities(
            cfg_list,
            default_blackbox_mapping_file,
            trigger_word_file
        )

    def test_django_view_param(self):
        vulnerabilities = self.run_analysis('examples/vulnerable_code/django_XSS.py')
        self.assert_length(vulnerabilities, expected_length=2)
        vulnerability_description = str(vulnerabilities[0])

        EXPECTED_VULNERABILITY_DESCRIPTION = """
            File: examples/vulnerable_code/django_XSS.py
             > User input at line 4, source "Framework function URL parameter":
                param
            File: examples/vulnerable_code/django_XSS.py
             > reaches line 5, sink "render(":
                ~call_1 = ret_django.shortcuts.render(request, 'templates/xss.html', 'param'param)
        """
        self.assertAlphaEqual(vulnerability_description, EXPECTED_VULNERABILITY_DESCRIPTION)


class EngineEveryTest(VulnerabilitiesBaseTestCase):
    def run_analysis(self, path):
        self.cfg_create_from_file(path)
        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_function)
        initialize_constraint_table(cfg_list)

        analyse(cfg_list)

        trigger_word_file = os.path.join(
            'pyt',
            'vulnerability_definitions',
            'all_trigger_words.pyt'
        )

        return find_vulnerabilities(
            cfg_list,
            default_blackbox_mapping_file,
            trigger_word_file
        )

    def test_self_is_not_tainted(self):
        vulnerabilities = self.run_analysis('examples/example_inputs/def_with_self_as_first_arg.py')
        self.assert_length(vulnerabilities, expected_length=0)


class EnginePositionTest(VulnerabilitiesBaseTestCase):
    def run_analysis(self):
        cfg_list = [self.cfg]

        FrameworkAdaptor(cfg_list, [], [], is_flask_route_function)
        initialize_constraint_table(cfg_list)

        analyse(cfg_list)

        trigger_word_file = os.path.join(
            'pyt',
            'vulnerability_definitions',
            'test_positions.pyt'
        )

        return find_vulnerabilities(
            cfg_list,
            default_blackbox_mapping_file,
            trigger_word_file
        )

    def test_sql_result_ignores_false_positive_prepared_statement(self):
        self.cfg_create_from_file('examples/vulnerable_code/sql/sqli.py')
        vulnerabilities = self.run_analysis()
        self.assert_length(vulnerabilities, expected_length=1)
        self.assertEqual(vulnerabilities[0].source.line_number, 26)

    def test_args_kwargs_that_do_dont_propagate(self):
        def check(fixture, vulnerable):
            tree = ast.parse('TAINT = make_taint()\n' + fixture)
            self.cfg_create_from_ast(tree)
            vulnerabilities = self.run_analysis()
            self.assert_length(vulnerabilities, expected_length=1 if vulnerable else 0, msg=fixture)

        no_vuln_fixtures = (
            'execute(0)',
            'run(0, x, TAINT, 0, x=x)',
            'run(x, 0, non_propagating=TAINT)',
            'execute(x, name=TAINT)',
            'execute(x, *TAINT)',
            'execute(text=x, **TAINT)',
            'execute(x, **TAINT)',
            'dont_run(TAINT)',
        )
        vuln_fixtures = (
            'run(TAINT)',
            'subprocess.run(TAINT)',
            'run(0, TAINT, 0, x=0)',
            'run(0, x, non_propagating=x, tainted=TAINT)',
            'execute(*ok, *TAINT)',
            'execute(name=x, **TAINT)',
        )
        for fixture_str in no_vuln_fixtures:
            check(fixture_str, False)
        for fixture_str in vuln_fixtures:
            check(fixture_str, True)
