import scrypt


image_name = request.args.get('image_name')
for x in range(0, 10):
	print(x)
foo = scrypt.outer(scrypt.inner(image_name), scrypt.other_inner(image_name)) # Any call after ControlFlowNode caused the problem
send_file(foo)
