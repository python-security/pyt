def outer(first_arg, second_arg):
    outer_ret_val = first_arg + second_arg
    return outer_ret_val

def first_inner(first_inner_arg):
    first_inner_ret_val = first_inner_arg + '1st'
    return first_inner_ret_val

def second_inner(second_inner_arg):
    second_inner_ret_val = second_inner_arg + '2nd'
    return second_inner_ret_val
    # return 'foo'

image_name = request.args.get('image_name')
if not image_name:
    image_name = 'foo'
foo = outer(first_inner(image_name), second_inner(image_name)) # Any call after ControlFlowNode caused the problem
send_file(foo)

