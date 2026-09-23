s = (3 * pow(2187, 1801) + pow(729, 2000)
     - 4 * pow(243,2100) + pow(81, 2200)
     - 2 * pow(27, 2400) - 13122)

cnt = 0
while s > 0:
    if s % 27 > 8:
        cnt += 1
    s //= 27
print(cnt)

