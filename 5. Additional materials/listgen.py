import os
l1 = range(10)
l2 = [x*2 for x in l1 if x>5 and x%2]
d = {i:i*2 for i in l1}
f = (x for x in l2)
s = {i for i in l2}
p = 'c:/windows'
e = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and os.path.splitext(x)[-1] == '.exe']
e = {x:os.stat(os.path.join(p,x)).st_size for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and os.path.splitext(x)[-1] == '.exe' and os.stat(os.path.join(p,x)).st_size > 1024*1024*2}
