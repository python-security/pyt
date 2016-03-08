from unittest import TextTestRunner
from unittest import TestSuite
from unittest import makeSuite

from label_visitor_test import LabelVisitorTest
from vars_visitor_test import VarsVisitorTest
from cfg_test import CFGIfTest, CFGWhileTest, CFGStartExitNodeTest, CFGForTest


test_suite = TestSuite()

# Add TestCase's here
tests = [
    LabelVisitorTest,
    VarsVisitorTest,
    CFGIfTest,
    CFGWhileTest,
    CFGStartExitNodeTest
    CFGForTest
]

for test in tests:
    test_suite.addTest(makeSuite(test))

runner = TextTestRunner(verbosity=2)
runner.run(test_suite)
