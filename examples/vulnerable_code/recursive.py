from flask import Flask, request

app = Flask(__name__)


def recur_without_any_propagation(x):
    if len(x) < 20:
        return recur_without_any_propagation("a" * 24)
    return "Done"


def recur_no_propagation_false_positive(x):
    if len(x) < 20:
        return recur_no_propagation_false_positive(x + "!")
    return "Done"


def recur_with_propagation(x):
    if len(x) < 20:
        return recur_with_propagation(x + "!")
    return x


@app.route('/recursive')
def route():
    param = request.args.get('param', 'not set')
    repeated_completely_untainted = recur_without_any_propagation(param)
    app.db.execute(repeated_completely_untainted)
    repeated_untainted = recur_no_propagation_false_positive(param)
    app.db.execute(repeated_untainted)
    repeated_tainted = recur_with_propagation(param)
    app.db.execute(repeated_tainted)
