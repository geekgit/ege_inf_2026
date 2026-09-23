from fnmatch import *

for x in range(0, 10 ** 8 + 1, 3377):
    if fnmatch(str(x), "?79?8*3"):
        print(x, x // 3377)
