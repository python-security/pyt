import unittest

from datetime import date

from pyt.github_search import get_dates, scan_github, set_github_api_token
from pyt.__main__ import analyse_repo
from pyt.reaching_definitions_taint import ReachingDefinitionsTaintAnalysis


class TestGetDates(unittest.TestCase):
    def assertDateTuple(self, dateInterval, expectedStart, expectedEnd):
        self.assertEqual(dateInterval[0], expectedStart)
        self.assertEqual(dateInterval[1], expectedEnd)

    def test_range_shorter_than_interval(self):
        date_range = get_dates(date(2016, 12, 12), date(2016, 12, 13), 7)
        date_range = list(date_range)

        self.assertDateTuple(date_range[0],
                             date(2016, 12, 12),
                             date(2016, 12, 13))

    def test_range_longer_than_interval(self):
        date_range = get_dates(date(2016, 12, 12), date(2016, 12, 16), 2)
        date_range = list(date_range)

        self.assertDateTuple(date_range[0],
                             date(2016, 12, 12),
                             date(2016, 12, 13))

        self.assertDateTuple(date_range[1],
                             date(2016, 12, 14),
                             date(2016, 12, 15))

        self.assertDateTuple(date_range[2],
                             date(2016, 12, 16),
                             date(2016, 12, 16))


class TestScanGithub(unittest.TestCase):
    def test_scan_simple_repo(self):
        set_github_api_token()
        scan_github('flask',
                    date(2017, 1, 1),
                    ReachingDefinitionsTaintAnalysis,
                    analyse_repo,
                    '')
