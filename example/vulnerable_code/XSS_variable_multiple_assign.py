from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/XSS_param', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    other_var = param + ''

    not_the_same_var = '' + other_var

    another_one = not_the_same_var + ''

    html = open('templates/XSS_param.html').read()
    resp = make_response(html.replace('{{ param }}', another_one))
    
    return resp

if __name__ == '__main__':
    app.run(debug= True)
