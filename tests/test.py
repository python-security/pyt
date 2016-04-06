from unittest import TextTestRunner
from unittest import TestSuite
from unittest import makeSuite

from label_visitor_test import LabelVisitorTest
from vars_visitor_test import VarsVisitorTest
from cfg_test import CFGIfTest, CFGWhileTest, CFGForTest, CFGGeneralTest, CFGFunctionNodeTest, CFGFunctionParameterNodeTest, CFGAssignmentAndBuiltinTest, CFGFunctionNodeWithReturnTest, CFGMultipleParametersTest, CFGStr, CFGNameConstant, CFGName, CFGAssignmentMultiTargetTest, CFGCallWithAttributeTest, CFGAssignListComprehension
from reaching_definitions_test import FixedPointTest
from flask_engine_test import FlaskEngineTest
test_suite = TestSuite()

# Add TestCase's here
tests = [
    LabelVisitorTest,
    VarsVisitorTest,
    CFGIfTest,
    CFGWhileTest,
    CFGForTest,
    CFGGeneralTest,
    FixedPointTest,
    CFGAssignmentAndBuiltinTest,
    CFGFunctionNodeWithReturnTest,
    CFGMultipleParametersTest,
    CFGStr,
    CFGNameConstant,
    CFGName,
    CFGAssignmentMultiTargetTest,
    CFGCallWithAttributeTest,
    FlaskEngineTest,
    CFGAssignListComprehension
]

for test in tests:
    test_suite.addTest(makeSuite(test))

runner = TextTestRunner(verbosity=2)
result = runner.run(test_suite)
if result.wasSuccessful():
    print('Success')
    exit(0)
else:
    print('Failure')
    exit(1)
