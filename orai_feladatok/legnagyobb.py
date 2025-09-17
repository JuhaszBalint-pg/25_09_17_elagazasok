a = input ("Add meg az első számot számot! \n")
b = input ("Add meg a második számot! \n")
c = input ("Add meg a harmadik számot! \n")
a, b, c = int(a), int(b), int(c)
if a>b and a>c:
    print (f"{a} a legnagyobb szám")

elif b>a and b>c:
    print (f"{b} a legnagyobb szám")

elif c>a and c>b:
    print (f"{c} a legnagyobb szám")