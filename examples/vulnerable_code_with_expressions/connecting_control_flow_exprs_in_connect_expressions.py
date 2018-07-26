"""
This is very similar to one of the false-negatives found in our November 16th/17th 2017 evaluation
http://pyt.readthedocs.io/en/latest/past_evaluations.html#november-16-17th-2017
"""

redirect(
	request.args.get('Laundry') and 'crazy'
	or
	request.args.get('French') and 'foo'
	or
	request.args.get('The')
)
