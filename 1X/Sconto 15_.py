print("Questo programma serve per calcolare il prezzo scontato del 15% di un prodotto")

Prezzo=float(input("Scrivi di seguito il prezzo intero del prodotto --> "))
ScontoPercentuale=float(input("Ora metti lo sconto percentuale (es. 0.15) "))
ScontoMassimo=float(input("Inserisci in fine lo sconto massimo "))
Sconto=Prezzo*ScontoPercentuale
if Sconto>ScontoMassimo:
    Sconto=15
elif Sconto<=ScontoMassimo:
    Sconto=Sconto
PrezzoScontato=Prezzo-Sconto
print("Il nuovo prezzo del prodotto è" ,PrezzoScontato, "€")
