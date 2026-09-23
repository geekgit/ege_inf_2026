from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:23]

for x in alph:
    s = int(f"1{x}1{x}1{x}1{x}1",23) + int(f"20{x}24",23) + int(f"1{x}235",23)
    if s % 22 == 0:
        print(x, s // 22)

