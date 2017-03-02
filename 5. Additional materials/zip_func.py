l1 = [1,2]
l2 = [4,5]
l3 = [7,8]
zip(l1, l2, l3)
pos = [
        [12.3, 32.1, 43.0],
        [87.5, 49.3, 34.4],
        [34.5, 98.3, 10.1],
        [65.5, 33.3, 11.0]
      ]
map(lambda x:sum(x)/len(x), zip(*pos))
[sum(x)/len(x) for x in  zip(*pos)]
