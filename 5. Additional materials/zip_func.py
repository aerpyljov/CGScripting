l1 = [1, 2]
l2 = [4, 5]
l3 = [7, 8]

"""Create a new list with the same length, where each element is a tuple"""
z = zip(l1, l2, l3)

# [(1, 4, 7), (2, 5, 8)]


"""There is a list of points, each described by its 3D coordinates.
We need to find the point in the middle."""
pos = [
        [12.3, 32.1, 43.0],
        [87.5, 49.3, 34.4],
        [34.5, 98.3, 10.1],
        [65.5, 33.3, 11.0]
      ]

"""Two ways to find the central point: sum all coordinates and divide by the number of points"""
# zip(*pos) = [(12.3, 87.5, 34.5, 65.5), (32.1, 49.3, 98.3, 33.3), (43.0, 34.4, 10.1, 11.0)]

map(lambda x: sum(x)/len(x), zip(*pos))
[sum(x)/len(x) for x in zip(*pos)]

# [49.95, 53.25, 24.625]
