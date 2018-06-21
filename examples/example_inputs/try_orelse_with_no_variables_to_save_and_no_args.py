def does_this_kill_us():
	return subprocess.call('ls', shell=True)

# @app.route('/poc', methods=['POST'])
# def poc():
try:
    print('A5')
except ImportError:
    print('Wagyu')
else:
    does_this_kill_us()
    print('So')
print('Good')
