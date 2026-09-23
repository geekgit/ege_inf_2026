max = 0

for x in range (1,232): # x будет в диапазоне от 1 до 231 включительно
    s = pow(64, 678) + pow(55, 123) - x
    cnt = 0 # число нулей в 25-ричной записи с текущим x
    while s > 0:
        if s % 25 == 0:
            cnt += 1
        s //= 25
    if cnt > max:
        max = cnt

print(max)

