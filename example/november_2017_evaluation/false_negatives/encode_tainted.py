@app.route('/encode_tainted')
def encode_tainted():
    state = request.args.get('state', '')
    next = base64.urlsafe_b64decode(state.encode('ascii'))
    return redirect(next)
