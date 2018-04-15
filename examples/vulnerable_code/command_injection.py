import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

@app.route('/menu', methods=['POST'])
def menu():
    param = request.form['suggestion']
    command = 'echo ' + param + ' >> ' + 'menu.txt'

    subprocess.call(command, shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

@app.route('/clean')
def clean():
    subprocess.call('echo Menu: > menu.txt', shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
