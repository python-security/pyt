import scrypt


def first_inner(first_arg):
    first_ret_val = first_arg + '1st'
    return first_ret_val

def third_inner(second_arg):
    third_ret_val = second_arg + '2nd'
    return third_ret_val

image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
foo = scrypt.outer(first_inner(image_name), scrypt.second_inner(image_name), third_inner(image_name)) # Any call after ControlFlowNode caused the problem
send_file(foo)
