from Flask import g

@app.route('/<url_short>')
def expand_url(url_short):
    """Check for url in DB"""
    result = query_db('select url_long from urls where url_short = ?',
                        [url_short], one=True)
    if result is None:
        return redirect(url_for("index"))
    else:
        link = result['url_long']
        return redirect(link)


def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv
