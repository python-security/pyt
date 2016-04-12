from flask import Flask, render_template, request, make_response
import random
import string
app = Flask(__name__)

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    html = open('templates/XSS_param.html').read()
    resp = make_response(html.replace('{{ param }}', param))
    return resp

if __name__ == '__main__':
    app.run(debug= True)
