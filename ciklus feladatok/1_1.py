"""
1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!
"""
szam = 2
while szam <= 10:

    if szam % 2 == 0:
        print (f"{szam} páros szám")
    szam = szam + 2