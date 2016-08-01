import pstats
import argparse
import os
from subprocess import run, PIPE

python = 'python3'
pyt_path = '../pyt/pyt.py'
stats_filename = 'stats'

parser = argparse.ArgumentParser()

parser.add_argument('project', help='Path to where the project is located which PyT should analyse.', type=str)
parser.add_argument('project_file', help='Path to the file where PyT should start to analyse.', type=str)
parser.add_argument('-n', '--number-of-results', help='Number of results to be shown. Default: 10.')

args = parser.parse_args()

number_of_results = 10
if args.number_of_results:
    number_of_results = args.number_of_results

run([python, '-m', 'cProfile', '-o', stats_filename,
     pyt_path, '-pr', args.project, args.project_file], stdout=PIPE)

def clean_up():
    if os.path.isfile(stats_filename):
        os.remove(stats_filename)

def prepare_results():
    stats = pstats.Stats(stats_filename)
    stats.sort_stats('cumulative')
    stats.print_stats(number_of_results)

prepare_results()
clean_up()

