s = (5 * pow(512, 1000) + pow(256, 1001)
     - pow(128, 1002) + pow(64, 1003)
     - 7 * pow(32, 1004) - 5120)

cnt = 0
while s > 0:
    if s % 32 <= 9:
        cnt += 1
    s //= 32
print(cnt)

