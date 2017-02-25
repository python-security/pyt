import unittest
from datetime import date

from pyt.github_search import get_dates


class GetDatesTest(unittest.TestCase):
    def test_range_shorter_than_interval(self):
        date_range = get_dates(date(2016,12,12), date(2016,12,13), 7)


