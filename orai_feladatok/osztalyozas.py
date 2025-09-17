doga_szazaleka = int(input("Add meg a dolgozat százalékát! \n"))

if 0 <= doga_szazaleka <= 49:
    print ("Elégtelen")

elif 50 <= doga_szazaleka <= 64:
    print ("Elégséges")

elif 65 <= doga_szazaleka <= 79:
    print ("Közepes")

elif 80 <= doga_szazaleka <= 89:
    print ("Jó")

elif 90 <= doga_szazaleka <= 100:
    print ("jeles")