from unittest import TextTestRunner
from unittest import TestSuite
from unittest import makeSuite
from unittest import TestLoader

test_suite = TestSuite()


loader = TestLoader()
suite = loader.discover('.',pattern='*_test.py')

runner = TextTestRunner(verbosity=2)
result = runner.run(suite)
if result.wasSuccessful():
    print('Success')
    exit(0)
else:
    print('Failure')
    exit(1)
