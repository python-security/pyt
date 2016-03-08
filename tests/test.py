from unittest import TextTestRunner
from unittest import TestSuite
from unittest import makeSuite
from unittest import defaultTestLoader as loader

from label_visitor_test import LabelVisitorTest
from vars_visitor_test import VarsVisitorTest

test_suite = TestSuite()

# Add TestCase's here
test_suite.addTest(makeSuite(LabelVisitorTest))
test_suite.addTest(makeSuite(VarsVisitorTest))


runner = TextTestRunner(verbosity=2)
runner.run(test_suite)
