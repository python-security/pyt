import pstats
import os
from subprocess import run as sub_run, PIPE

python = 'python3'
pyt_path = '../pyt/pyt.py'
stats_filename = 'stats'
snakeviz = 'snakeviz'

def clean_up():
    if os.path.isfile(stats_filename):
        os.remove(stats_filename)

def prepare_results(number_of_results):
    stats = pstats.Stats(stats_filename)
    stats.sort_stats('cumulative')
    stats.print_stats(number_of_results)

def visualise():
    try:
        sub_run([snakeviz, stats_filename])
    except KeyboardInterrupt:
        pass
    except:
        print('It seems that snakeviz is not installed.')
        print('To install snakeviz see: https://jiffyclub.github.io/snakeviz/ .')
        exit(0)

def run(project, project_file, number_of_results):
    if project:
        sub_run([python, '-m', 'cProfile', '-o', stats_filename,
            pyt_path, '-pr', project, project_file], stdout=PIPE)
    else:
        sub_run([python, '-m', 'cProfile', '-o', stats_filename,
            pyt_path, project_file], stdout=PIPE)

    prepare_results(number_of_results)

