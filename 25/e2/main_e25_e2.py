from fnmatch import *

for x in range(0, 10 ** 8 + 1, 1112):
    if fnmatch(str(x), "11??4*56"):
        print(x, x // 1112)
