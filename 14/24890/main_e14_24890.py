max = 0
for x in range (1, 7291): # x будет в диапазоне от 1 до 7291, не включая 7291
    s = pow(27, 298) + pow(27, 269) - x
    cnt = 0
    while s > 0:
        if s % 27 == 0:
            cnt += 1
        s //= 27
    if cnt > max:
        max = cnt

print(max)

