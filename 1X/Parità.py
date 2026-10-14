print("Questo programma serve per determinare se 2 numeri hanno la stessa parità")
Numero1=int(input("Scrivi di seguito il primo numero --> "))
Numero2=int(input("Bene, ora scrivi il secondo --> "))
Resto1=Numero1%2
Resto2=Numero2%2
if Resto1==Resto2:
    print("I due numeri hanno la stessa parità")
else:
    print("I due numeri hanno parità differenti")
