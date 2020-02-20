def fab_gen(a,b):
    x=int(input('range'))
    yield a
    yield b
    for i in range(x):
        c=a+b
        a=b
        b=c
        yield c
