import pstats
import os
from subprocess import run as sub_run, PIPE

python = 'python3'
pyt_path = '../pyt/pyt.py'
STATS_FILENAME = 'stats.prof'
snakeviz = 'snakeviz'
KERNPROF = 'kernprof'

def clean_up():
    if os.path.isfile(STATS_FILENAME):
        os.remove(STATS_FILENAME)

def prepare_results(number_of_results):
    stats = pstats.Stats(STATS_FILENAME)
    stats.sort_stats('cumulative')
    stats.print_stats(number_of_results)

def visualise():
    try:
        sub_run([snakeviz, STATS_FILENAME])
    except KeyboardInterrupt:
        pass
    except:
        print('It seems that snakeviz is not installed.')
        print('To install snakeviz see: https://jiffyclub.github.io/snakeviz/ .')
        exit(0)

def run(project, project_file, number_of_results):
    if project:
        sub_run([python, '-m', 'cProfile', '-o', STATS_FILENAME,
            pyt_path, '-pr', project, project_file], stdout=PIPE)
    else:
        sub_run([python, '-m', 'cProfile', '-o', STATS_FILENAME,
            pyt_path, project_file], stdout=PIPE)

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
    filename = 'reaching_definitions_taint.py'
    list_of_functions = ['arrow', 'join', 'fixpointmethod']
    insert_profile('../pyt/' + filename, list_of_functions)
    if project:
        sub_run([KERNPROF, '-l', '-v', pyt_path, '-pr', project, project_file])
    else:
        sub_run([KERNPROF, '-l', '-v', pyt_path, project_file])
    remove_profile('../pyt/' + filename)
