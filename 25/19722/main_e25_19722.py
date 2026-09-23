from fnmatch import *

for x in range(0, 10 ** 10 + 1, 12602):
    if fnmatch(str(x), "*45?49*24"):
        print(x, x // 12602)
