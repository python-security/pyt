def func(x):
    yield x
    yield 2

def main():
    gen = func(1)
    print(next(gen))
    x = 1
    y = 2
    print(next(gen))
