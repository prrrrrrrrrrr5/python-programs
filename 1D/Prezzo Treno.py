#Inizio

NPersone=int(input("Inserisci di seguito il numero di persone che prendono parte a questo viaggio \n --> "))
PrezzoBiglietto=float(input("Inserisci di seguito il prezzo del biglietto del treno \n --> "))

NGratuita=NPersone//9
PrezzoTot=PrezzoBiglietto*NPersone-NGratuita*PrezzoBiglietto
PrezzoSingolo=PrezzoTot/NPersone
PrezzoSingoloArr=round(PrezzoSingolo,2)

print("Il prezzo per persona è di" ,PrezzoSingoloArr, "€")

if NGratuita==1:
    print("C'è solo una gratuità")
elif NGratuita>1:
    print("Ci sono" ,NGratuita, "gratuità")
else:
    print("Non ci sono gratuità")

#Fine


#input=Numero persone, prezzo biglietto
#output=Prezzo per persona, numero di gratuità
#prezzo= PrezzoBiglietto*NPersone - gratuità*PrezzoBiglietto
#prezzo singolo= prezzo/NPersone
