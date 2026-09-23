for p in range(11,37):
    a = int("29A1", p)
    b = int("47771", p)
    c = int("12A", p)
    s = a + b + c - 1000000
    if 1 <= s <= 500000:
        print(p)



