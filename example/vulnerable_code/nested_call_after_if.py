import scrypt

# def outer(outer_arg):
# 	outer_ret_val = outer_arg + 'hey'
# 	return outer_ret_val

image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
# for x in range(0, 10):
# 	print(x)
# print('if this print statement is here everything works')
# print('foo')
foo = scrypt.outer(image_name) # Any call after if causes the problem
send_file(foo)
