for n in range(374457,374505 + 1):
    divs = []
    for i in range (2,n):
        if n % i == 0:
            divs.append(i)
    if len(divs) == 4:
        print(sorted(divs))