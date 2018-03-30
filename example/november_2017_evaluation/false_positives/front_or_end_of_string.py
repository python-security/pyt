"""
One of the false-positives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""
@app.route('/client/passport', methods=['POST','GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?response_type=%s&client_id=%s&redirect_uri=%s' %(code,client_id,redirect_uri)
    return redirect(uri)
