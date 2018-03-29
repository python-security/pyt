@app.route('/split_tainted')
def split_tainted():
    state = request.args.get('state', '')
    next = base64.urlsafe_b64decode(state).split(';')
    return redirect(next)
