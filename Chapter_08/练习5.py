def factory(n):
    if n == 0 :
        return 1
    if n == 1 :
        return 1
    return n * factory(n-1)

def factory_generator(n):
    for i in range(1,n+1):
        yield factory(i)



fg = factory_generator(5)
print(next(fg))
for f in fg:
    print(f, end=' ')