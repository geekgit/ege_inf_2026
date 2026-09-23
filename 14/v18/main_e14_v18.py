s = (pow(4, 2022) - 2 * pow(4, 1111)
     + pow(16, 600) + 192)
list = []
while s > 0:
    list.append(s % 4)
    s //= 4
print(list.count(3))

