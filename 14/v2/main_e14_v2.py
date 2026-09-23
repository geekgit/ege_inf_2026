s = (4 * pow(2187, 2101) + pow(729, 2000)
     - 5 * pow(243,2100) + pow(81, 2200)
     - 3 * pow(27, 2250) - 26244)

cnt = 0
while s > 0:
    if s % 27 > 9:
        cnt += 1
    s //= 27
print(cnt)

