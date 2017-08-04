def does_this_kill_us(diff):
	return subprocess.call(diff, shell=True)

@app.route('/poc', methods=['POST'])
def poc():
	try:
	    value = None
	except ImportError:
	    value = request.args.get('foo')
	else:
	    does_this_kill_us(value)
