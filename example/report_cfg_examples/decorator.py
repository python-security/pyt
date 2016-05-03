class LabelDecorator(object):
    def __init__(self, number):
        self.number = number

    def __call__(self, f):
        print('Function: ', self.number)
        
        return f
        

@LabelDecorator(1)
def foo(a, b):
    return a + b

print(foo(3, 4))
