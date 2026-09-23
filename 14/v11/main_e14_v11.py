from string import digits
from string import ascii_uppercase
symbols = digits + ascii_uppercase
alph = symbols[:25]

for x in alph:
    s = int(f"1{x}2{x}3{x}4{x}5",25) + int(f"2{x}024",25) + int(f"1{x}099",25)
    if s % 24 == 0:
        print(x, s // 24)

