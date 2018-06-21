from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    other_var = param + ''

    html = open('templates/XSS_param.html').read()
    resp = make_response(html.replace('{{ param }}', other_var))
    return resp

if __name__ == '__main__':
    app.run(debug= True)
