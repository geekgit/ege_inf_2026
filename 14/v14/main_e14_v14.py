s = (pow(4, 2022) - 6 * pow(4, 522)
     + 5 * pow(64, 510) - 3 * pow(2, 330)
     - 100)
list = []
while s > 0:
    list.append(s % 8)
    s //= 8
print(list.count(7))

