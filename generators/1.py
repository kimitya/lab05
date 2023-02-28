def gen(n):
    for i in range(n):
        yield i*i
for i in gen(10):
    print(i)