from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:23]

for x in alph:
    s = int(f"2{x}{x}341011",23) + int(f"220{x}4",23) + int(f"110{x}6",23)
    if s % 22 == 0:
        print(x, s // 22)

