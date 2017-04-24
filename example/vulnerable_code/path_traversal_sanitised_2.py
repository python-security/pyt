import os
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def cat_picture():
    image_name = request.args.get('image_name')

    if not '..' in image_name:
        return 404
    return send_file(os.path.join(os.getcwd(), image_name))

if __name__ == '__main__':
    app.run(debug=True)
