from fnmatch import *

for x in range(0, 10 ** 10 + 1, 12007):
    if fnmatch(str(x), "9*?001?1"):
        print(x, x // 12007)
