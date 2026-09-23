s = (pow(3, 2021) + 5 * pow(3, 2000)
     + pow(3, 501) + 5 * pow(3, 500)
     + 1)
list = []
while s > 0:
    list.append(s % 9)
    s //= 9
print(list.count(0))

