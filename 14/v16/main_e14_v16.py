s = (pow(1331, 650) - 55 * pow(121, 610)
     + 77 * pow(11, 510) - 3 * pow (11, 100)
     - 221)
list = []
while s > 0:
    list.append(s % 11)
    s //= 11
a = int("A",11)
print(list.count(a))

