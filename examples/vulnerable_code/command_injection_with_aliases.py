import os
import os as myos
from os import system
from os import system as mysystem
from subprocess import call as mycall, Popen as mypopen

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/menu', methods=['POST'])
def menu():
    param = request.form['suggestion']
    command = 'echo ' + param + ' >> ' + 'menu.txt'

    os.system(command)
    myos.system(command)
    system(command)
    mysystem(command)
    mycall(command)
    mypopen(command)

    with open('menu.txt', 'r') as f:
        menu_ctx = f.read()

    return render_template('command_injection.html', menu=menu_ctx)


if __name__ == '__main__':
    app.run(debug=True)
