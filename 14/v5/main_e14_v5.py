def digits_calc(x, base, digit):
    cnt = 0
    while x > 0:
        if x % base == 0:
            cnt += 1
        x //= base
    return cnt


s1 = pow(9, 2025)
z1 = digits_calc(s1,9,0)
s2 = pow(9, 1000)
z2 = digits_calc(s2, 9, 0)
print(f"Количество нулей в 9^2025: {z1}")
print(f"Количество нулей в 9^1000: {z2}")
assert digits_calc(pow(9, 2025), 9, 0) == 2025
assert digits_calc(pow(9, 1000), 9, 0) == 1000

for i in range (0,5770): # i будет в диапазоне от 0 до 5770, не включая 5770
    x = 5769 - i # x будет в диапазоне от 5769 до 0 включительно
    s = pow(9, 2025) + pow(9, 1000) - x # s = 9^2025 + 9^1000 - x
    cnt = digits_calc(s,9,0)
    if cnt == 1026:
        print(x)
        break

