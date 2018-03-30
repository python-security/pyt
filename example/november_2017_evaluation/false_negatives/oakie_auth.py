"""
One of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""

@app.route('/auth_callback')
def auth_callback():
    error = request.args.get('error', '')
    if error:
        return 'Error: ' + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        abort(403)
    next = base64.urlsafe_b64decode(state.encode('ascii')).split(';')[1]
    remove_state(state)
    code = request.args.get('code')
    id_token, access_token = get_tokens(code)

    session['email'] = id_token['email']
    return redirect(next)
