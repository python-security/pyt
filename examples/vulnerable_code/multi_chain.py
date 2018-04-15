import subprocess
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/multi_chain', methods=['POST'])
def multi_chain():
    suggestion = request.form['suggestion']
    x = fast_eddie(suggestion, 'the')
    y = x + 'foo'
    z = minnesota_fats(suggestion, 'sting')
    ben = graham(y, z)

    subprocess.call(ben, shell=True)

    return render_template('multi_chain.html')
