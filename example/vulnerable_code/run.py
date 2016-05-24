from subprocess import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('python', help='Specify Python 3.', type=str)
args = parser.parse_args()

files = ['XSS.py', 'command_injection.py', 'path_traversal.py', 'path_traversal_sanitised.py', 'path_traversal_sanitised_2.py', 'sql/sqli.py', 'XSS_form.py', 'XSS_no_vuln.py', 'XSS_reassign.py', 'XSS_sanitised.py', 'XSS_variable_assign_no_vuln.py', 'XSS_variable_assign.py', 'XSS_variable_multiple_assign.py']

for f in files:
    run([args.python, '../../pyt/pyt.py', f])
