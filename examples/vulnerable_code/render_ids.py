from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    # Expected value
    ids = [u"one", u"two's", u'"three"']
    # Injected somehow
    ids = ' onmouseover=alert(1) '

    return render_template('render_ids.html', ids=ids)

if __name__ == '__main__':
    app.run(port=80, debug=True)
