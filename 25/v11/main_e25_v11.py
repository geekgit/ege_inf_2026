from fnmatch import *

for x in range(0, 10 ** 8 + 1, 5171):
    if fnmatch(str(x), "?19*8?3"):
        print(x, x // 5171)
