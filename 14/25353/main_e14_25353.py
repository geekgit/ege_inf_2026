for x in range (0, 27001): # x будет в диапазоне от 0 до 27000 включительно

    s = 3 * pow(27, 9) + 2 * pow(27, 6) + pow(27, 3) - x
    cnt = 0
    while s > 0:
        if s % 27 == 0:
            cnt += 1
        s //= 27
    if cnt == 6:
        print(x)
        break

