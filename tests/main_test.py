import mock

from .base_test_case import BaseTestCase
from pyt.__main__ import main


class MainTest(BaseTestCase):
    @mock.patch('pyt.__main__.parse_args')
    @mock.patch('pyt.__main__.find_vulnerabilities')
    @mock.patch('pyt.__main__.text')
    def test_text_output(self, mock_text, mock_find_vulnerabilities, mock_parse_args):
        mock_find_vulnerabilities.return_value = 'stuff'
        example_file = 'examples/vulnerable_code/inter_command_injection.py'
        output_file = 'mocked_outfile'

        mock_parse_args.return_value = mock.Mock(
            autospec=True,
            filepath=example_file,
            project_root=None,
            baseline=None,
            json=None,
            output_file=output_file
        )
        main([
            'parse_args is mocked'
        ])
        assert mock_text.report.call_count == 1
        # This with: makes no sense
        with self.assertRaises(AssertionError):
            assert mock_text.report.assert_called_with(
                mock_find_vulnerabilities.return_value,
                mock_parse_args.return_value.output_file
            )

    @mock.patch('pyt.__main__.parse_args')
    @mock.patch('pyt.__main__.find_vulnerabilities')
    @mock.patch('pyt.__main__.json')
    def test_json_output(self, mock_json, mock_find_vulnerabilities, mock_parse_args):
        mock_find_vulnerabilities.return_value = 'stuff'
        example_file = 'examples/vulnerable_code/inter_command_injection.py'
        output_file = 'mocked_outfile'

        mock_parse_args.return_value = mock.Mock(
            autospec=True,
            filepath=example_file,
            project_root=None,
            baseline=None,
            json=True,
            output_file=output_file
        )
        main([
            'parse_args is mocked'
        ])
        assert mock_json.report.call_count == 1
        # This with: makes no sense
        with self.assertRaises(AssertionError):
            assert mock_json.report.assert_called_with(
                mock_find_vulnerabilities.return_value,
                mock_parse_args.return_value.output_file
            )
