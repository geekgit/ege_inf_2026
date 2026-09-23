from fnmatch import *

for x in range(0, 10 ** 10 + 1, 6437):
    if fnmatch(str(x), "1?3*5*954"):
        print(x, x // 6437)
