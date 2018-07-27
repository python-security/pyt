def foo():
    a = 1
    if a == 1:
        yield 0
    yield a

foo()
