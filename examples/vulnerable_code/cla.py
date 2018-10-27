# This example is based on:
# https://www.kevinlondon.com/2015/07/26/dangerous-python-functions.html
#
# Run this example from the pyt repo root directory with adapter "Every":
# pyt -a Every examples/vulnerable_code/cla.py

import subprocess
from sys import argv

def transcode_file(filename):
    # Piping commands to the shell (shell=True) is a bad idea!
    # What if a file name like "; rm -rf /" is provided?
    # If the host machine runs the Python process as a privileged user,
    # that could delete all of the files on the machine.
    # Use quoting https://docs.python.org/2/library/pipes.html#pipes.quote (Python2) or
    # https://docs.python.org/3.3/library/shlex.html#shlex.quote (Python3)!
    command = 'ffmpeg -i "{source}" probably_never_existing.mp3'.format(source=filename)
    subprocess.call(command, shell=True)

# command line application intended to be called with one arg like:
# script.py stairway_to_heaven.mp4
if __name__ == "__main__":
    transcode_file(argv[1:][0])
