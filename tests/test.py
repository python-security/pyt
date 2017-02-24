from run import check_files
from unittest import TestLoader, TestSuite, TextTestRunner


test_suite = TestSuite()
loader = TestLoader()
suite = loader.discover('.', pattern='*_test.py')

runner = TextTestRunner(verbosity=2)
result = runner.run(suite)

passed = check_files()

if result.wasSuccessful() and passed:
    print('Success')
    exit(0)
else:
    print('Failure')
    exit(1)
