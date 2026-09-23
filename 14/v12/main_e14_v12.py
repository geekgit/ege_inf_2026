from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:19]

for x in alph:
    s = int(f"3{x}2{x}1{x}0{x}1", 19) + int(f"{x}2024", 19) + int(f"1{x}077",19)
    if s % 18 == 0:
        print(x, s // 18)

