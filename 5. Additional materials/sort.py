import os
p = r'C:\Windows\en-US'
l = os.listdir(p)

"""New lists sorted, but an existing list unchanged"""
sorted(l, reverse=1, key=lambda x: os.stat(os.path.join(p,x)).st_size)
sorted(l, cmp=lambda x, y: x > y)

"""Sort an existing list"""
l.sort()
