a = int(input("Adj meg egy évszámot! \n"))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print (f"{a} szökőév")
else:
    print (f"{a} nem szökőév")