from ..base_test_case import BaseTestCase


class VulnerabilitiesBaseTestCase(BaseTestCase):

    def string_compare_alpha(self, output, expected_string):
        return (
            [char for char in output if char.isalpha()] ==
            [char for char in expected_string if char.isalpha()]
        )

    def assertAlphaEqual(self, output, expected_string):
        self.assertEqual(
            ''.join(char for char in output if char.isalpha()),
            ''.join(char for char in expected_string if char.isalpha())
        )
        return True
