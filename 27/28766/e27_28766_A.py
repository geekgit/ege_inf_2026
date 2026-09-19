from math import dist
from fnmatch import fnmatch

with open("27_A.txt") as f:
    p = [[float(x), float(y), v] for x, y, v in
         (s.replace(",", ".").split() for s in f)]

c = [
    [p for p in p if p[1] > 10],
    [p for p in p if p[1] <= 10]
]

centers = [
    min(cluster, key=lambda q: sum(dist(q[:2], p[:2]) for p in cluster))
    for cluster in c
]

d = [
    dist(centers[0][:2], p[:2])
     for p in p if fnmatch(p[2], "Y?III")
]

a1 = int(min(d) * 10000)
a2 = int(max(d) * 10000)

print(a1, a2)
