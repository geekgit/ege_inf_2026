from math import dist
from fnmatch import fnmatch

with open("27_B.txt") as f:
    p = [[float(x), float(y), v] for x, y, v in
         (s.replace(",", ".").split() for s in f)]

c = [
    [p for p in p if p[0] > 20],
    [p for p in p if p[0] <= 20 and p[1] > 22],
    [p for p in p if p[0] <= 20 and p[1] <= 22]
]

centers = [
    min(cluster, key=lambda q: sum(dist(q[:2], p[:2]) for p in cluster))
    for cluster in c
]

z = [
    [p[:2] for p in cluster if fnmatch(p[2], "Z?I")]
    for cluster in c
]

d = [
    dist(a, b)
    for cluster in z
    for a in cluster
    for b in cluster
    if a != b
]

b1=int(abs(min(d) * 10000))
b2=int(abs(dist(centers[0][:2], centers[2][:2]) * 10000))

print(b1, b2)