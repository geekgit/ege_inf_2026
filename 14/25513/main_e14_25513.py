s = (pow(17 + 19, 3 * 50) -
     (pow(2 * 3, 1 + 2) +
      (pow(2, 500) - pow(4, 250)))) // 6

list = []
while s > 0:
    list.append(s % 6)
    s //= 6
print(list.count(5))

