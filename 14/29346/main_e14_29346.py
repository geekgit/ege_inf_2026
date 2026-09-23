s = (5 * pow(1296, 2021) - 4 * pow(216, 2022)
     + 3 * pow(36, 2023) - 2 * pow(6, 2024) - 2025)
list = []
while s > 0:
    digit = s % 36
    if digit % 2 == 0:
        list.append(digit)
    s //= 36
print(len(list))

