#Inizio

Importo=float(input("Inserisci di seguito l'importo da pagare \n --> "))

if Importo>=100:
    Sconto=float(input("Inserisci di seguito la percentuale \n --> "))
    Importo=Importo-Importo*(Sconto/100)

print("L'importo totale è di" ,Importo, "€")

#Fine
