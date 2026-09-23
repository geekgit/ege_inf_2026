s = (3 * pow(512, 1500) + pow(256, 1501)
     - 2 * pow(128, 1502) + pow(64, 1503)
     - 3 * pow(32, 1504) - 10240)

cnt = 0
while s > 0:
    if s % 32 <= 9:
        cnt += 1
    s //= 32
print(cnt)

