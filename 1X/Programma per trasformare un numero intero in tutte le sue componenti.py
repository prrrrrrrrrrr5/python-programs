print("Questo programma serve per trasformare un numero intero (entro le migliaia) in tutte le sue componenti (migliaia, centinaia, decine e unità")
NumeroIniziale=int(input("Scrivi di seguito il numero che vuoi trasformare "))
Migliaia=NumeroIniziale//1000
Centinaia=NumeroIniziale//100
Decine=NumeroIniziale//10
Unità=NumeroIniziale
print("Bene, il tuo numero ha:" ,Unità, ("Unità") ,Decine, ("Decine") ,Centinaia, ("Centinaia") ,Migliaia, ("Migliaia"))
