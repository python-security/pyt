def foo():
    print('h')

@app.route('/', methods = ['GET'])
def flask_function(x):
    return x

print('nothing')
