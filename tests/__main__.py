from unittest import (
    TestLoader,
    TestSuite,
    TextTestRunner
)


test_suite = TestSuite()
loader = TestLoader()
suite = loader.discover('.', pattern='*_test.py')

runner = TextTestRunner(verbosity=2)
result = runner.run(suite)

if result.wasSuccessful():
    print('Success')
    exit(0)
else:  # pragma: no cover
    print('Failure')
    exit(1)
