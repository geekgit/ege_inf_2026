from fnmatch import *

for x in range(0, 10 ** 8 + 1, 123):
    if fnmatch(str(x), "32*823"):
        print(x, x // 123)
