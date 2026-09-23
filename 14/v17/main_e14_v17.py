s = (pow(5, 2022) - 2 * pow(5, 1010)
     + pow(25, 850) + 2500)
list = []
while s > 0:
    list.append(s % 5)
    s //= 5
print(list.count(4))

