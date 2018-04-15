import subprocess
from flask import Flask, render_template, request

from other_file import return_the_arg


app = Flask(__name__)

@app.route('/menu', methods=['POST'])
def menu():
    param = request.form['suggestion']

    command = return_the_arg('echo ' + param + ' >> ' + 'menu.txt')
    subprocess.call(command, shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
