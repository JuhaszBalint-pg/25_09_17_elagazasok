"""
3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
"""

a = 10

while a != 0:
    if a % 2 != 0:
        print (f"{a}")
        a = a - 1
    else:
        a = a - 1