import scrypt


image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
foo = scrypt.encrypt(scrypt.encrypt(), image_name) # Nested call after if caused the problem
send_file(foo)
