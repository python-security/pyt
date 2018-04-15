import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

def outer(outer_arg):
    outer_ret_val = outer_arg + 'hey'
    return outer_ret_val

def inner(inner_arg):
    inner_ret_val = inner_arg + 'hey'
    return inner_ret_val

@app.route('/menu', methods=['POST'])
def menu():
    req_param = request.form['suggestion']

    subprocess.call(outer(inner(req_param)), shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)
