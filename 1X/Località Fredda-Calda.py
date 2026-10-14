print("Questo programma serve per dire le località più calda/fredda date N località inserite")

NLocalità=int(input("Inserisci di seguito quante località vuoi valutare --> "))
Località1=str(input("Inserisci di seguito una località --> "))
Temperatura1=float(input("Inserisci di seguito la sua rispettiva temperatura --> "))
LocalitàCalda=Località1
LocalitàFredda=Località1
TemperaturaCalda=Temperatura1
TemperaturaFredda=Temperatura1
for i in range(1,NLocalità):
    Località=str(input("Inserisci di seguito una località --> "))
    Temperatura=float(input("Inserisci di seguito la sua rispettiva temperatura --> "))
    if Temperatura>TemperaturaCalda:
        LocalitàCalda=Località
    elif Temperatura<TemperaturaFredda:
        LocalitàFredda=Località
print("La località più calda è" ,LocalitàCalda, "e la più fredda è" ,LocalitàFredda,)
