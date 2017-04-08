from flask import Flask, render_template, request

import other_file


app = Flask(__name__)

@app.route('/menu', methods=['POST'])
def menu():
    param = request.form['suggestion']

    other_file.shell_the_arg('echo ' + param + ' >> ' + 'menu.txt')

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
