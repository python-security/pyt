from unittest import mock

from .base_test_case import BaseTestCase
from pyt.__main__ import discover_files, main


class MainTest(BaseTestCase):
    @mock.patch('pyt.__main__.discover_files')
    @mock.patch('pyt.__main__.parse_args')
    @mock.patch('pyt.__main__.find_vulnerabilities')
    @mock.patch('pyt.__main__.text')
    def test_text_output(self, mock_text, mock_find_vulnerabilities, mock_parse_args, mock_discover_files):
        mock_find_vulnerabilities.return_value = 'stuff'
        example_file = 'examples/vulnerable_code/inter_command_injection.py'
        output_file = 'mocked_outfile'

        mock_discover_files.return_value = [example_file]
        mock_parse_args.return_value = mock.Mock(
            project_root=None,
            baseline=None,
            json=None,
            output_file=output_file
        )
        with self.assertRaises(SystemExit):
            main(['parse_args is mocked'])
        assert mock_text.report.call_count == 1
        mock_text.report.assert_called_with(
            mock_find_vulnerabilities.return_value,
            mock_parse_args.return_value.output_file
        )

    @mock.patch('pyt.__main__.discover_files')
    @mock.patch('pyt.__main__.parse_args')
    @mock.patch('pyt.__main__.find_vulnerabilities')
    @mock.patch('pyt.__main__.text')
    def test_no_vulns_found(self, mock_text, mock_find_vulnerabilities, mock_parse_args, mock_discover_files):
        mock_find_vulnerabilities.return_value = []
        example_file = 'examples/vulnerable_code/inter_command_injection.py'
        output_file = 'mocked_outfile'

        mock_discover_files.return_value = [example_file]
        mock_parse_args.return_value = mock.Mock(
            project_root=None,
            baseline=None,
            json=None,
            output_file=output_file
        )
        main(['parse_args is mocked'])  # No SystemExit
        assert mock_text.report.call_count == 1
        mock_text.report.assert_called_with(
            mock_find_vulnerabilities.return_value,
            mock_parse_args.return_value.output_file
        )

    @mock.patch('pyt.__main__.discover_files')
    @mock.patch('pyt.__main__.parse_args')
    @mock.patch('pyt.__main__.find_vulnerabilities')
    @mock.patch('pyt.__main__.json')
    def test_json_output(self, mock_json, mock_find_vulnerabilities, mock_parse_args, mock_discover_files):
        mock_find_vulnerabilities.return_value = 'stuff'
        example_file = 'examples/vulnerable_code/inter_command_injection.py'
        output_file = 'mocked_outfile'

        mock_discover_files.return_value = [example_file]
        mock_parse_args.return_value = mock.Mock(
            project_root=None,
            baseline=None,
            json=True,
            output_file=output_file
        )
        with self.assertRaises(SystemExit):
            main(['parse_args is mocked'])
        assert mock_json.report.call_count == 1
        mock_json.report.assert_called_with(
            mock_find_vulnerabilities.return_value,
            mock_parse_args.return_value.output_file
        )


class DiscoverFilesTest(BaseTestCase):
    def test_targets_with_no_excluded(self):
        targets = ["examples/vulnerable_code/inter_command_injection.py"]
        excluded_files = ""

        included_files = discover_files(targets, excluded_files)
        expected = ["examples/vulnerable_code/inter_command_injection.py"]
        self.assertListEqual(included_files, expected)

    def test_targets_with_exluded(self):
        targets = ["examples/vulnerable_code/inter_command_injection.py"]
        excluded_files = "examples/vulnerable_code/inter_command_injection.py"

        included_files = discover_files(targets, excluded_files)
        expected = []
        self.assertListEqual(included_files, expected)

    def test_targets_with_recursive(self):
        targets = ["examples/vulnerable_code/"]
        excluded_files = ""

        included_files = discover_files(targets, excluded_files, True)
        self.assertEqual(len(included_files), 31)

    def test_targets_with_recursive_and_excluded(self):
        targets = ["examples/vulnerable_code/"]
        excluded_files = "inter_command_injection.py"

        included_files = discover_files(targets, excluded_files, True)
        self.assertEqual(len(included_files), 30)
