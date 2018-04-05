"""
This is very similar to one of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(request.args.get("next") if 5==5 else url_for("index"))
