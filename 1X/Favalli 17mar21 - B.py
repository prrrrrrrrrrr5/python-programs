print("Questo programma serve per calcolare l'importo del noleggio in base al tipo di bicicletta e al tempo")

Bicicletta=str(input("Scrivi che bicicletta o che biciclette vuoi noleggiare (le risposte possibili sono:turismo, mountainbike, turismo e mountainbike, mountainbike e turismo) --> "))
Risposta1= "turismo" 
Risposta2= "mountainbike"
Risposta3= "turismo e mountainbike"
Risposta4= "mountainbike e turismo"
if Bicicletta== Risposta1 or Risposta2:
    NBiciToM=int(input("Scrivi di seguito quante bici vuoi noleggiare --> "))
elif Bicicletta== Risposta3 or Risposta4:
    NBiciTeM=int(input("Scrivi di seguito quante coppie di bici (turismo e mountainbike) vuoi noleggiare --> "))
Ore=float(input("Ora scrivi il numero di ore e/o minuti (ricordati di mettere il punto tra ore e minuti, non la virgola) --> "))
RestoOre=Ore%1 
if RestoOre==0:
    Ore=Ore
else:
    Ore=(Ore-RestoOre)+1
PrezzoFissoTurismo
PrezzoFisso