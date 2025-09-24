folytatja = True
while folytatja:
      print('Vidd ki a szemetet!')
      valasz = input('Mondjam még egyszer? (i/n)')
      if valasz == 'n':
          folytatja = False
      elif valasz == "igen" or valasz == "nem":
           print ("Rossz formátum")    
print('>> Program vége! <<')  