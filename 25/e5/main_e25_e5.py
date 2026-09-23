cnt = 0
i = 900000 + 1
while cnt != 5:
    divs = []
    for j in range (2, int(i ** 0.5 + 1)):
        if j * j == i:
            divs.append(j)
        elif i % j == 0:
            divs.append(j)
            divs.append(i // j)
    if divs:
        if (min(divs)+max(divs)) % 151 == 0:
            print(i, min(divs) + max(divs))
            cnt += 1
    i += 1