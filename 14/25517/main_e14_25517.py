s = (pow(16, 350) * pow (15 * 3 - 29, pow (4, 2 + 5)) + 1007) // 63
list = []
while s > 0:
    list.append(s % 4)
    s //= 4
print(list.count(1))

