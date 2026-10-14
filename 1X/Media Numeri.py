print("Questo programma serve per calcolare la media di tot numeri inseriti dall'utente")

Numeri=int(input("Inserisci il numero di numeri di cui vuoi fare la media --> "))
SommaNumeri=0
Numero=float(input("Inserisca un numero di seguito --> "))
NumeroMassimo=Numero
NumeroMinimo=Numero
for i in range(0,Numeri-1):
    Numero=float(input("Inserisci un numero di seguito --> "))
    SommaNumeri=SommaNumeri+Numero
    PosizioneMin=1
    PosizioneMax=1
    if Numero>NumeroMassimo:
        NumeroMassimo=Numero
        PosizioneMax=i
    elif Numero<NumeroMinimo:
        NumeroMinimo=Numero
        PosizioneMin=i
Media=SommaNumeri/Numeri
Semidispersione=(NumeroMassimo-NumeroMinimo)/2
print("La media dei numeri è" ,Media, "e la semidispersione è" ,Semidispersione,)
