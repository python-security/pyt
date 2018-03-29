@app.route('/index_of_tainted')
def index_of_tainted():
    state = request.args.get('state', '')
    next = base64.urlsafe_b64decode(state).split(';')[1]
    return redirect(next)
