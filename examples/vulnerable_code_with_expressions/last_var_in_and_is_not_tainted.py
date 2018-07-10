"""
This is very similar to one of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""

redirect(request.args.get('The') if 'hey' or 'you' else request.args.get('French') if 'foo' else request.args.get('Aces') and 'c')
