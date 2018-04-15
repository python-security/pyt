import scrypt


image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
foo = scrypt.outer(image_name) # Any call after ControlFlowNode caused the problem
send_file(foo)
