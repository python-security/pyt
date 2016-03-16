import random

def foo():
    print('h')

def bar(x):
    y = input()
    print(y)
    print(x)

def baz(x):
    return x+1

foo()
bar(3)
x = baz(1)
print(x)
