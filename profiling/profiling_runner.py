"""Runs the profiler everytime travis is building.

Saves the result for future reference.
"""
from datetime import datetime
from shutil import which
from subprocess import Popen


FIXED_POINT_FLAG = '-fp'
KERNPROF = 'kernprof-3.5'
PROFILER = 'profiler.py'
PROFILING_DB = 'db.txt'
TEST_PROJECT_1 = 'test_projects/flaskbb_lite_1/flaskbb/app.py'
TEST_PROJECT_2 = 'test_projects/flaskbb_lite_2/flaskbb/app.py'
TEST_PROJECT_3 = 'test_projects/flaskbb_lite_3/flaskbb/app.py'
TEST_PROJECTS = [TEST_PROJECT_1, TEST_PROJECT_2, TEST_PROJECT_3]
TRAVIS_PYTHON = 'python'


if which(KERNPROF) is None:
    print('You need "kernprof" to run this script. Install: "pip3 install line_profiler".')
    exit(1)

with open(PROFILING_DB, 'a') as fd:
    fd.write('############################################### Profiling \
{} ###############################################\n\n'.format(datetime.now()))

for tp in TEST_PROJECTS:
    print('Profiling: ', tp)
    with open(PROFILING_DB, 'a') as fd:
        fd.write('##### Profiling {} #####\n\n'.format(tp))
    with open(PROFILING_DB, 'a') as fd:
        p = Popen(['python3', PROFILER, tp, FIXED_POINT_FLAG], stdout=fd)
        p.wait()

with open(PROFILING_DB, 'a') as fd:
    fd.write('\n')
