for x in range(0, 10**8+1, 2111):
    if str(x)[:2] == "12" and str(x)[4:6] == "36" and str(x)[-1] == "1":
        print(x, x // 2111)
