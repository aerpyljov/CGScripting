f = lambda : 4-2
f()

def getFunc(v):
    if v > 0:
        return lambda x: x / 10
    else:
        return lambda x: x * 10
f = getFunc(0)
f(120)

class cls(object):
    def __init__(self):
        for i in range(10):
            setattr(self, 'a%s' % i, lambda x=i: x)

c = cls()
c.a1()