import unittest

from datetime import date

from pyt.github_search import get_dates


class TestGetDates(unittest.TestCase):
    def assertDateTuple(self, dateInterval, expectedStart, expectedEnd):
        print(dateInterval)
        print(expectedStart)
        print(expectedEnd)

        assert(dateInterval[0] == expectedStart)
        assert(dateInterval[1] == expectedEnd)

    def test_range_shorter_than_interval(self):
        date_range = get_dates(date(2016, 12, 12), date(2016, 12, 13), 7)
        date_range = list(date_range)

        print(date_range)
        self.assertDateTuple(date_range[0],
                             date(2016, 12, 12),
                             date(2016, 12, 13))

    def test_range_longer_than_interval(self):
        date_range = get_dates(date(2016, 12, 12), date(2016, 12, 16), 2)
        date_range = list(date_range)

        print(date_range)
        self.assertDateTuple(date_range[0],
                             date(2016, 12, 12),
                             date(2016, 12, 13))

        self.assertDateTuple(date_range[1],
                             date(2016, 12, 14),
                             date(2016, 12, 15))

        self.assertDateTuple(date_range[2],
                             date(2016, 12, 16),
                             date(2016, 12, 16))
