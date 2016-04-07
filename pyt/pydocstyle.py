import subprocess
import re
from pprint import pprint

docstyle = subprocess.run(["pydocstyle", "--ignore=D105,D203,D212,D213"], stderr=subprocess.PIPE, universal_newlines=True)

lines = re.split('\n', docstyle.stderr)

errors = zip(lines[0::2], lines[1::2])

errors = [x + "\n\t" + y for x,y in errors]

errors = [error for error in errors if 'visit_' not in error]

for error in errors:
    print(error + '\n')

print("Total errors: {}".format(len(errors)))
