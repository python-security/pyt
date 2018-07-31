async def g(x, *args):
    return await x()


async def f(y):
    z = await g(y, await v)
    return z


f(w)
