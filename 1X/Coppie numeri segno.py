print("Questo programma serve per calcolare quante coppie di numeri inserite hanno lo stesso segno") #introduzione alla funzione del programma

CoppieNumeri=int(input("Inserisci di seguito quante coppie di numeri vuoi inserire --> ")) #Questa riga serve per capire quante coppie l'utente vuole valutare
CoppiePositive=0 #Variabili che contano le coppie con lo stesso segno
CoppieNegative=0
for i in range(0,CoppieNumeri): #Ciclo che serve per far inserire all'utente le coppie di numeri
    NumeroCoppia1=float(input("Inserisci il primo numero della coppia --> ")) #L'utente qui inserisce il primo numero
    NumeroCoppia2=float(input("Inserisci il secondo numero della coppia --> ")) #L'utente qui inserisce il secondo numero
    if NumeroCoppia1>=0 and NumeroCoppia2>=0: #Le seguenti quattro righe servono per calcolare quante sono le coppie con segno positivo e le coppie con segno negativo
        CoppiePositive=CoppiePositive+1
    elif NumeroCoppia1<0 and NumeroCoppia2<0:
        CoppieNegative=CoppieNegative+1
print("Le coppie di numeri con lo stesso segno sono" ,CoppiePositive+CoppieNegative,)
