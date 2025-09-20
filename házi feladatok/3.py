"""
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot!
 Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
"""

import random
b = random.randint (1, 5)

print ("Gondoltam egy számra, találd ki melyikre 1-5 között")
a = int(input ("A szám melyre gondoltál: \n"))

if a==b: 
    print ("Kitaláltad!")
elif a>b:
    print ("A szám melyre gomdoltam kisebb")
elif a<b:
    print ("A szám melyre gondoltam nagyobb")


