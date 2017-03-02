import os
p = r'C:\Windows\ru-RU'
l = os.listdir(p)
sorted(l, reverse=1, key=lambda x: os.stat(os.path.join(p,x)).st_size)
sorted(l,cmp=lambda x,y: x>y)
l.sort()

