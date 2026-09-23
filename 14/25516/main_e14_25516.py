s = (pow(25, 500) * pow (4 * 6 + 1, pow (5, 3 + 1)) + 7) // 128
list = []
while s > 0:
    list.append(s % 5)
    s //= 5
print(list.count(4))

