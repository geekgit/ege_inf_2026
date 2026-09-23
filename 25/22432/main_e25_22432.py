from fnmatch import *

def all_digits_unique(number):
    num_str = str(number)
    return len(num_str) == len(set(num_str))

for x in range(0, 10 ** 12 + 1, 84318):
    if fnmatch(str(x), "5*7?") and all_digits_unique(x):
        print(x, x // 84318)
