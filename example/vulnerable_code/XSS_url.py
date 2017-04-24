from flask import Flask, make_response
app = Flask(__name__)

@app.route('/XSS_param/<path:url>', methods =['GET'])
def XSS1(url):
    param = url

    html = open('templates/XSS_param.html').read()
    resp = make_response(html.replace('{{ param }}', param))
    return resp

if __name__ == '__main__':
    app.run(debug= True)
