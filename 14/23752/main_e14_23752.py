s = (2 * pow(2187, 2020) + pow(729, 2021)
     - 2 * pow(243, 2022) + pow(81, 2023)
     - 2 * pow(27, 2024) - 6561)

cnt = 0
while s > 0:
    if s % 27 > 9:
        cnt += 1
    s //= 27
print(cnt)

