def outer(outer_arg):
	outer_ret_val = outer_arg + 'hey'
	return outer_ret_val

def inner(inner_arg):
	inner_ret_val = inner_arg + 'hey'
	return inner_ret_val

foo = 'bar'
abc = outer(inner(foo))
