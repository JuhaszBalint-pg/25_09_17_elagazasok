a = int(input ("Please enter a number 1-10:  \n"))

paros = [2, 4, 6, 8, 10]
if a in paros and 0<a<10:
    print ("Páros számot adtál meg, 0-10 között")
else:
    print ("Páratlan számot adtál meg, vagy nincs 0-10 között")