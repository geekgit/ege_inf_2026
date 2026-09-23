s = (pow(243, 540) - 6 * pow(9, 530)
     + 21 * pow(3, 511) - 3 * pow(3, 70)
     - 200)
list = []
while s > 0:
    list.append(s % 9)
    s //= 9
print(list.count(8))

