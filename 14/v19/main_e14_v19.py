s = (2 * pow(3, 2022) + 5 * pow(3, 1800)
     + pow(3, 1001) + 4 * pow(3, 1000)
     + 3)
list = []
while s > 0:
    list.append(s % 9)
    s //= 9
print(list.count(0))

