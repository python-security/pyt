from sqli import db
from sqli import User


db.create_all()

def add_user(name, email):
    u = User(name, email)
    db.session.add(u)


add_user('hest', 'hest')
add_user('føl', 'føl')

db.session.commit()
