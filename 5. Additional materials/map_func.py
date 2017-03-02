x = range(10)
z = range(10,20)
f = lambda i, j: i*j
new = map(f, x, z)

map( lambda x: x*3, z)
[x*3 for x in z]