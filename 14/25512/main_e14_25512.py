s = (pow(8, 200) - ((pow(2, 4) - 7) * pow(2, 9 + 7)) + 11) // 3

list = []
while s > 0:
    list.append(s % 8)
    s //= 8
print(list.count(2))

