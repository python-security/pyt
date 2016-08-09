"""Runs the profiler everytime travis is building.

Saves the result for future reference.
"""
from subprocess import Popen, PIPE

TRAVIS_PYTHON = 'python'
PROFILER = 'profiler.py'
TEST_PROJECT_1 = 'test_projects/flaskbb_lite_1/flaskbb/app.py'
TEST_PROJECT_2 = 'test_projects/flaskbb_lite_2/flaskbb/app.py'
TEST_PROJECT_3 = 'test_projects/flaskbb_lite_3/flaskbb/app.py'

with open('saved.txt', 'a') as fd:
    p = Popen(['python3', PROFILER, TEST_PROJECT_1], stdout=fd)
with open('saved.txt', 'a') as fd:
    p = Popen(['python3', PROFILER, TEST_PROJECT_2], stdout=fd)
with open('saved.txt', 'a') as fd:
    p = Popen(['python3', PROFILER, TEST_PROJECT_3], stdout=fd)

