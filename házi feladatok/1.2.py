"""
Fejleszd tovább az első feladat programját úgy,
 hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""

a = input ("Jó napod van? \n")
if a=="igen":
    print ("Örülök, maradjon így!")
elif a=="nem":
    print ("Sajnálom hogy így érzel, remélem jobbra fordul majd!")
else:
    print ("Sajnos nem értem a válaszodat!")