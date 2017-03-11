def zrange(val):
    i = 0
    while i < val:
        yield i
        i += 1

for i in zrange(10):
    print i
