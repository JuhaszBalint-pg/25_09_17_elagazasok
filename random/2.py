"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

import random
b = random.randint (1,2)
a = input ("Fej vagy írás? ")

if b==1 and a=="fej":
    print ("Eltaláltad")

elif b==1 and a=="írás":
    print ("Nem találtad el")

elif b==2 and a=="fej":
    print ("nem találtad el")

elif b==2 and a=="írás":
    print ("Eltaláltad")

else:
    print ("nem megfelelő adat")