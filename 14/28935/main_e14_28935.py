from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:23]

for x in alph:
    s = int(f"761{x}035", 23) + int(f"338{x}932", 23)
    if s % 22 == 0:
        print(x, s // 22)

