from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:29]

for x in alph:
    s = int(f"923{x}874",29) + int(f"524{x}6152",29)
    if s % 28 == 0:
        print(x, s // 28)

