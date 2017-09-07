import subprocess
from flask import Flask, render_template, request

# This is a lib we can't possibly see inside of
import scrypt


app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def menu():
    param = request.args.get('suggestion')

    # This is a function we can't possibly see inside of
    command = scrypt.encrypt('echo ' + param + ' >> ' + 'menu.txt', 'password')
    hey = command
    subprocess.call(hey, shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
