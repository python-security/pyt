import subprocess
from flask import Flask, render_template, request

# This is a lib we can't possibly see inside of
import scrypt


app = Flask(__name__)

@app.route('/menu', methods=['POST'])
def menu():
    req_param = request.form['suggestion']

    subprocess.call(scrypt.encypt(scrypt.encypt(req_param)), shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)
