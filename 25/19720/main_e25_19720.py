from fnmatch import *

for x in range(0, 10 ** 8 + 1, 153):
    if fnmatch(str(x), "1*2?3*45"):
        print(x, x // 153)
