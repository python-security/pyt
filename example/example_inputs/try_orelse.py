def does_this_kill_us(diff):
	return subprocess.call(diff, shell=True)

# @app.route('/poc', methods=['POST'])
# def poc():
try:
    value = None
    print('A5')
except ImportError:
    value = request.args.get('foo')
    print('Wagyu')
else:
    does_this_kill_us(value)
    print('So')
print('Good')
