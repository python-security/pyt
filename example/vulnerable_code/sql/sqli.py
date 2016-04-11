from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# SQL Alchemy setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username    
    
@app.route('/')
def index():
    param = request.args.get('param', 'not set')
    result = db.engine.execute(param)
    print(User.query.all(), file=sys.stderr)
    return 'Look console'

@app.route('/value_injection')
def value():
    param = request.args.get('param', 'not set')
    result = db.engine.execute('select * from User where username = "' + param + '";')
    for row in result:
        print(row, file=sys.stderr)
    return 'Look console'


if __name__ == '__main__':
    app.run(debug=True)
