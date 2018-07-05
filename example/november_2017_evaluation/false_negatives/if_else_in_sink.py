"""
This is very similar to one of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""
import scrypt


@app.route('/login', methods=['GET', 'POST'])
def login():
	# 2 bool op
    # print('foo')
    # x = 5
    # laun = request.args.get('Laundry')
    laun = 'beep'
    # return redirect(request.args.get('The') or request.args.get('French') or 'laun' and 'crazy')
    # return redirect(request.args.get('The') or request.args.get('French') or request.args.get('Laundry') and 'crazy')

    # works
    # return redirect(request.args.get('The') or request.args.get('French') or 'crazy' and request.args.get('Laundry'))

    return redirect(request.args.get('The') if 1==2 else request.args.get('French') if 'foo' else 'crazy')

    # works
    # return redirect('crazy' and request.args.get('Laundry') )


    # return redirect(request.args.get('The') if 1==2 else request.args.get('French'))
    # return redirect(request.args.get('The') if 1==2 else laun)

    # return redirect(request.args.get('The'))


    # return redirect(request.args.get('The') if 1==2 else 'foo')
    # return redirect('beep', request.args.get('The'))
    # return redirect(request.args.get('The') if 1==2 else 'beep')
    # return redirect(request.args.get('The'))
    # return 'The'
    # return redirect('The')


    # 2 IfExp and a string
    # return redirect(request.args.get('The') if 1==2 else request.args.get('French') if 2==3 else 'Laundry')
    # 3 IfExp
    # return redirect(request.args.get('The') if 1==2 else request.args.get('French') if 2==3 else request.args.get('Laundry'))

    # All 3
    # return redirect(request.args.get('The') if 5==5 else url_for('French'), request.args.get('Laundry') or url_for('Sushiritto'), scrypt.encrypt('Mixt'))
