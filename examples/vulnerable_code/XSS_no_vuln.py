from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    html = open('templates/XSS_param.html').read()
    other = ''
    resp = make_response(html.replace('{{ param }}', other))
    return resp

if __name__ == '__main__':
    app.run(debug= True)
