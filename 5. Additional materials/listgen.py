import os

"""List generator"""
l1 = range(10)
l2 = [x*2 for x in l1 if x>5 and x%2]
print l1
print l2

"""Dictionary generator"""
d = {i:i*2 for i in l1}
print d

"""A generator object - look at 'gen.py'"""
f = (x for x in l2)
print f

"""Set generator"""
s = {i for i in l2}
print s

"""How to get a list of exe-files """
p = 'c:/windows'
e1 = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and os.path.splitext(x)[-1] == '.exe']

print e1


"""How to get a list of exe-files large than 2 MB"""
e2 = {x: os.stat(os.path.join(p,x)).st_size for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and os.path.splitext(x)[-1] == '.exe' and os.stat(os.path.join(p,x)).st_size > 1024*1024*2}

print e2
