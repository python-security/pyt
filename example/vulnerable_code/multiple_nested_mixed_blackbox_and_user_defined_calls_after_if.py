import scrypt


def outer(first_arg, second_arg, third_arg):
    outer_ret_val = first_arg + second_arg + third_arg
    return outer_ret_val

def second_inner(inner_arg):
    inner_ret_val = inner_arg + '2nd'
    return inner_ret_val

image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
foo = outer(scrypt.first_inner(image_name), second_inner(image_name), scrypt.third_inner(image_name)) # Any call after ControlFlowNode caused the problem
send_file(foo)
