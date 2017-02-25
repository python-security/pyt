import argparse

from . import fine_timer


parser = argparse.ArgumentParser()

parser.add_argument('project_file', help='Path to the file where PyT should start to analyse.', type=str)
parser.add_argument('-pr', '--project', help='Path to where the project is located which PyT should analyse.', type=str)
parser.add_argument('-n', '--number-of-results', help='Number of results to be shown. Default: 10.', type=int)
parser.add_argument('-v', '--visualise', help='Visualise the results in an interactive way.', action='store_true')
parser.add_argument('-fp', '--fixed-point', help='Run line profiling on the fixed point algorithm.', action='store_true')
parser.add_argument('-k', '--keep-intermediate-files', help='Keep files from cProfile and the line profiler.', action='store_true')

args = parser.parse_args()

number_of_results = 10
if args.number_of_results:
    number_of_results = args.number_of_results

fine_timer.run(args.project, args.project_file, number_of_results)

if args.fixed_point:
    fine_timer.fixed_point_timer(args.project, args.project_file)

if args.visualise:
    try:
        print()
        print('#############################')
        print('C-c to to clean up and exit.')
        print('#############################')
        print()
        fine_timer.visualise()
    except KeyboardInterrupt:
        pass

if not args.keep_intermediate_files:
    fine_timer.clean_up()
