"""A minimized version of flask_expand_url to illustrate the question of 'what args being tainted means a vulnerability?'"""

from Flask import g

@app.route('/<david>')
def expand_url(david):
    foster = query_db('select url_long from urls where david = ?', [david])


def query_db(query, args=()):
    wallace = g.db.execute(query, args)
