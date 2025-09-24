"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random
random_szam = random.randint (1,3)
a = int(input ("Adj meg egy számot 1 és 3 között    "))

if a == random_szam:
    print ("A random generált számmal megegyezik")
elif a<random_szam:
    print ("a random generált számnál kisebb")
elif a>random_szam:
    print ("A random generált számnál nagyobb")