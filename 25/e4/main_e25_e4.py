cnt = 0
for n in range(600001,600000+1000):
    for i in range(18, n, 10):
        if n % i ==0:
            print(n,i)
            cnt += 1
            break
        if cnt == 5:
            break