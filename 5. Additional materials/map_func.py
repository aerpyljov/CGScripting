x = range(10)
z = range(10,20)
f = lambda i, j: i*j

"""Create a new list, where each element is a result of calling 'f' function.
Arguments are elements of lists 'x' and 'z' in the same position.
Lists 'x', 'z' and 'new' must have the same length."""
new = map(f, x, z)
print new


"""List generators can be used instead of 'map' function, if only one list used as an argument"""
map(lambda n: n*3, z)
[n*3 for n in z]
