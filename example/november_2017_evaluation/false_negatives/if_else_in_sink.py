"""
This is very similar to one of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""
import scrypt


@app.route('/login', methods=['GET', 'POST'])
def login():
	# 2 bool op
    return redirect(request.args.get('The') or request.brgs.get('French') or request.crgs.get('Laundry'))


    # 2 IfExp and a string
    # return redirect(request.args.get('The') if 1==2 else request.args.get('French') if 2==3 else 'Laundry')
    # 3 IfExp
    # return redirect(request.args.get('The') if 1==2 else request.args.get('French') if 2==3 else request.args.get('Laundry'))

    # All 3
    # return redirect(request.args.get('The') if 5==5 else url_for('French'), request.args.get('Laundry') or url_for('Sushiritto'), scrypt.encrypt('Mixt'))
