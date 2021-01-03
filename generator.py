def mygen():
    yield 'A'
    yield 'B'
g=mygen()
print(g)
print(next(g))
print(next(g))
