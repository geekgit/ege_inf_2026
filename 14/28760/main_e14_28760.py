s = (2 * pow(2187, 507) + pow(729, 566)
     - 2 * pow(243, 565) + pow(81, 564)
     - 2 * pow(27, 563) - 6561)
cnt = 0
while s > 0:
    x = s % 27
    if (x % 2 == 0) and (x > 9):
        cnt += 1
    s //= 27
print(cnt)

