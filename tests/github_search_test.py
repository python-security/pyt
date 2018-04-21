import unittest
from datetime import date

from pyt.github_search import get_dates


class GetDatesTest(unittest.TestCase):
    def test_get_dates(self):
        date_ranges = get_dates(
            date(2018, 1, 1),
            date(2018, 1, 31)
        )
        EXPECTED_RANGE = (
            ('2018-01-01', '2018-01-08'),
            ('2018-01-08', '2018-01-15'),
            ('2018-01-15', '2018-01-22'),
            ('2018-01-22', '2018-01-29')
        )
        for date_range, expected_range in zip(date_ranges, EXPECTED_RANGE):
            for date_, expected_date in zip(date_range, expected_range):
                assert str(date_) == expected_date
