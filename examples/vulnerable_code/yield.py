import subprocess
from flask import Flask, request

app = Flask(__name__)


def things_to_run():
    yield "echo hello"
    yield from request.get_json()["commands"]
    yield "echo done"


@app.route('/', methods=['POST'])
def home():
    script = "; ".join(things_to_run())
    subprocess.call(script, shell=True)
    return 'Executed'


if __name__ == '__main__':
    app.run(debug=True)
