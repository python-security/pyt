import os
import pstats
from subprocess import PIPE, run as sub_run


KERNPROF = 'kernprof-3.5'
LINE_PROFILER_FILE = 'pyt.py.lprof'
PYTHON = 'python3'
PYT_PATH = '../pyt/pyt.py'
SNAKEVIZ = 'snakeviz'
STATS_FILENAME = 'stats.prof'


def clean_up():
    if os.path.isfile(STATS_FILENAME):
        os.remove(STATS_FILENAME)
    if os.path.isfile(LINE_PROFILER_FILE):
        os.remove(LINE_PROFILER_FILE)

def prepare_results(number_of_results):
    stats = pstats.Stats(STATS_FILENAME)
    stats.sort_stats('cumulative')
    stats.print_stats(number_of_results)

def visualise():
    try:
        sub_run([SNAKEVIZ, STATS_FILENAME], stdout=PIPE, stderr=PIPE)
    except KeyboardInterrupt:
        pass
    except:
        print('It seems that snakeviz is not installed.')
        print('To install snakeviz see: https://jiffyclub.github.io/snakeviz/ .')
        exit(0)

def run(project, project_file, number_of_results):
    if project:
        sub_run([PYTHON, '-m', 'cProfile', '-o', STATS_FILENAME,
            PYT_PATH, '-pr', project, project_file], stdout=PIPE)
    else:
        sub_run([PYTHON, '-m', 'cProfile', '-o', STATS_FILENAME,
            PYT_PATH, project_file], stdout=PIPE)

    prepare_results(number_of_results)

def get_indendation(line):
    return line.split('def')[0]

def insert_profile(filename, list_of_functions):
    out = list()
    old_line = ''
    with open(filename, 'r') as fd:
        for line in fd:
            for func in list_of_functions:
                if '@profile' not in old_line and 'def ' + func in line:
                    out.append(get_indendation(line) + '@profile\n')
            old_line = line
            out.append(line)

    with open(filename, 'w') as fd:
        for line in out:
            fd.write(line)

def remove_profile(filename):
    out = list()
    with open(filename, 'r') as fd:
        for line in fd:
            if '@profile' not in line:
                out.append(line)
    with open(filename, 'w') as fd:
        for line in out:
            fd.write(line)

def fixed_point_timer(project, project_file):
    analysis_filename = '../pyt/reaching_definitions_taint.py'
    list_of_functions = ['arrow', 'join', 'fixpointmethod']
    insert_profile(analysis_filename, list_of_functions)
    fixed_point_filename = '../pyt/fixed_point.py'
    list_of_functions = ['fixpoint_runner']
    insert_profile(fixed_point_filename, list_of_functions)
    lattice_filename = '../pyt/lattice.py'
    list_of_functions = ['get_elements']
    insert_profile(fixed_point_filename, list_of_functions)

    if project:
        sub_run([KERNPROF, '-l', '-v', PYT_PATH, '-pr', project, project_file])
    else:
        sub_run([KERNPROF, '-l', '-v', PYT_PATH, project_file])

    remove_profile(analysis_filename)
    remove_profile(fixed_point_filename)
    remove_profile(lattice_filename)
