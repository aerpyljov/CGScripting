import glob
import os
p = 'c:/windows'
e = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) and os.path.splitext(x)[-1] == '.exe']
glob.glob1(p, '*[0-9].exe')
sorted([1,5,8,4])

def c(x,y):
    print x, y
    return 0
