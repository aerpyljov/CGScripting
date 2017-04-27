f = lambda: 4-2
f()


"""Different functions with the same name"""
def getFunc(v):
    if v > 0:
        return lambda x: x / 10
    else:
        return lambda x: x * 10
f = getFunc(0)  # Argument 'v'
f(120)  # Argument 'x'


"""How to create a lot of attributes"""
class cls(object):
    def __init__(self):
        for i in range(10):
            setattr(self, 'a%s' % i, lambda x=i: x * 2)


c = cls()
c.a1()
c.a7()
c.a9()