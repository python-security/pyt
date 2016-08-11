from unittest import TextTestRunner
from unittest import TestSuite
from unittest import makeSuite
from unittest import TestLoader
from run import check_files

python = open('python_name.txt', 'r').read().rstrip()

test_suite = TestSuite()
loader = TestLoader()
suite = loader.discover('.',pattern='*_test.py')

runner = TextTestRunner(verbosity=2)
result = runner.run(suite)

passed = check_files(python)

if result.wasSuccessful() and passed:
    print('Success')
    exit(0)
else:
    print('Failure')
    exit(1)
