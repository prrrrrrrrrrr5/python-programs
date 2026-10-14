print("Questo programma serve per dire quanti N numeri inseriti dall'utente sono positivi, quanti negativi e quanti uguali a zero")

Numeri=int(input("Inserisci di seguito quanti numeri vuoi che siano contati --> "))
NumeriPositivi=0 #Variabili che servono per contare i vari numeri
NumeriNegativi=0
Numeri0=0
for i in range(0,Numeri): #Ciclo per mettere i numeri da contare
    Numero1=int(input("Inserisci un numero --> "))
    if Numero1>0: #Comando che serve per contare i numeri
        NumeriPositivi=NumeriPositivi+1
    elif Numero1<0:
        NumeriNegativi=NumeriNegativi+1
    elif Numero1==0:
        Numeri0=Numeri0+1
print("Nei numeri inseriti ci sono" ,NumeriPositivi, "numeri maggiori di 0 (positivi)," ,Numeri0, "numeri pari a 0 e" ,NumeriNegativi,"numeri più bassi di 0 (negativi)")
