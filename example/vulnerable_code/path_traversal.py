import os
from flask import Flask, request, send_file

app = Flask(__name__)

def outer(outer_arg, other_arg):
	outer_ret_val = outer_arg + 'hey' + other_arg
	return outer_ret_val

def inner():
	return 'boom'

@app.route('/')
def cat_picture():
    image_name = request.args.get('image_name')
    if not image_name:
        # image_name = 5
        return 404
    # return send_file(os.path.join(os.getcwd(), image_name))
    # send_file(os.path.join(os.getcwd(), image_name))
    hey = inner()
    foo = outer(hey, image_name) # Inlining inner here fucks everything
    send_file(foo)
    return 'idk'


if __name__ == '__main__':
    app.run(debug=True)
