from flask import Flask, request, make_response
app = Flask(__name__)

class AwesomeString():

    def __init__(self, s):
        self.s = s

def dum(p):
    p = ''

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')
    pik = dum(param)

    html = open('templates/XSS_param.html').read()
    resp = make_response(html.replace('{{ param }}', pik))
    return resp

if __name__ == '__main__':
    app.run(debug= True)
