from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
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
    
@app.route('/raw')
def index():
    param = request.args.get('param', 'not set')
    result = db.engine.execute(param)
    print(User.query.all(), file=sys.stderr)
    return 'Result is displayed in console.'

@app.route('/filtering')
def filtering():
    param = request.args.get('param', 'not set')
    Session = sessionmaker(bind=db.engine)
    session = Session()
    result = session.query(User).filter("username={}".format(param))
    for value in result:
        print(value.username, value.email)
    return 'Result is displayed in console.'

if __name__ == '__main__':
    app.run(debug=True)
