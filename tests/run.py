from subprocess import run, PIPE
import argparse

delimiter = '#¤%&/()=?'
results_file = 'results'
pyt_path = '../pyt/pyt.py'
example_file_path = '../example/vulnerable_code/'
python_name = open('python_name.txt', 'r').read().rstrip()
encoding = 'utf-8'

parser = argparse.ArgumentParser()
parser.add_argument('-py', '--python', help='Specify Python 3.', type=str)
parser.add_argument('-s', '--save-results', help='Add new results', action='store_true')
parser.add_argument('-p', '--pyt-output', help='Print output of PyT for each file.', action='store_true')

files = ['XSS.py', 'command_injection.py', 'path_traversal.py', 'path_traversal_sanitised.py', 'sql/sqli.py', 'XSS_form.py', 'XSS_url.py', 'XSS_no_vuln.py', 'XSS_reassign.py', 'XSS_sanitised.py', 'XSS_variable_assign_no_vuln.py', 'XSS_variable_assign.py', 'XSS_variable_multiple_assign.py']
files = [example_file_path + filename for filename in files]

def check_files(python):
    try:
        with open(results_file, 'r', encoding=encoding) as fd:
            results = fd.read().split(delimiter)
    except FileNotFoundError:
        print(results_file + ' file was not found. Generate this file by running this script with option --save-results or -s.')
        exit(1)

    results.pop() # last element is empty because results file always ends with a delimiter
        
    passed = True

    if len(results) != len(files):
        print('Number of results are not equal to the number of files')
        print('Results: ' + str(len(results)) + ' Files: ' + str(len(files)))
        exit(0)

    for i, f in enumerate(files):
        print('################# ' + f + ' #################')
        process = run([python, pyt_path, f], stdout=PIPE)
        stdout = str(process.stdout)
        if results[i] == stdout:
            print('Test passed.')
        else:
            print('Test failed.')
            passed = False
    return passed

def save_results(python):
    with open(results_file, 'w', encoding=encoding) as fd:
        for f in files:
            print('################# ' + f + ' #################')
            process = run([python, pyt_path, f], stdout=PIPE)
            fd.write(str(process.stdout))
            fd.write(delimiter)
            print('Saved result to file: "' + results_file + '".')

def print_pyt_output(python):
    for f in files:
        print('################# ' + f + ' #################')
        run([python, pyt_path, f])

if __name__ == '__main__':
    args = parser.parse_args()

    if args.python:
        python_name = args.python

    if args.save_results:
        save_results(python_name)
    elif args.pyt_output:
        print_pyt_output(python_name)
    else:
        check_files(python_name)
