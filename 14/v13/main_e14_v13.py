s = (4 * pow(25, 2022) - 2 * pow(5, 2000)
     + pow(125, 1011) - 3 * pow(5, 100)
     - 660)
list = []
while s > 0:
    list.append(s % 5)
    s //= 5
print(list.count(4))

