def does_this_kill_us(diff):
	return subprocess.call(diff, shell=True)

# @app.route('/poc', methods=['POST'])
# def poc():
try:
    print('A5')
except ImportError:
    print('Wagyu')
else:
    does_this_kill_us("hard-coded string")
    print('So')
print('Good')
