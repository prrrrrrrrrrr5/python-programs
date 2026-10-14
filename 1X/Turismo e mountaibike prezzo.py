print("Questo programma serve per calcolare l'importo del noleggio in base al tipo di bicicletta e al tempo")

Bicicletta=str(input("Scrivi che bicicletta o che biciclette vuoi noleggiare (le risposte possibili sono: turismo, mountainbike, turismo e mountainbike, mountainbike e turismo) --> ")) #Questa riga serve per chiedere all'utente che tipo di bicicletta vuole
Risposta1= "turismo" #Le seguenti righe servono per memorizzare le possibili risposte
Risposta2= "mountainbike"
Risposta3= "turismo e mountainbike"
Risposta4= "mountainbike e turismo"
if Bicicletta== Risposta1 or Risposta2: #Queste righe servono per capire quante biciclette vuole l'utente
    NBiciToM=int(input("Scrivi di seguito quante bici (mountainbike/turismo) vuoi noleggiare --> ")) #Questa riga serve per chiedere all'utente quante biciclette vuole noleggiare
elif Bicicletta== Risposta3 or Risposta4:
    NBiciTeM=int(input("Scrivi di seguito quante coppie di bici (turismo e mountainbike) vuoi noleggiare --> "))
Ore=float(input("Ora scrivi il numero di ore e/o minuti (ricordati di mettere il punto tra ore e minuti, non la virgola) --> ")) #Questa riga serve per capire per quante ore l'utente vuole noleggiare la bici
RestoOre=Ore%1 #Le righe seguenti servono per calcolare il numero di ore 
if RestoOre==0:
    Ore=Ore
else:
    Ore=(Ore-RestoOre)+1
PrezzoFissoTurismo=3 #Questa riga e la seguente sono i prezzi fissi dei tipi di bici che possono essere cambiati qui dal codice quando l'utente vuole
PrezzoFissoMountainBike=4
Prezzo=0
if Bicicletta==Risposta1: #Le righe seguenti servono per calcolare il prezzo
    Prezzo=PrezzoFissoTurismo*Ore*NBiciToM
elif Bicicletta==Risposta2:
    Prezzo=PrezzoFissoMountainBike*Ore*NBiciToM
elif Bicicletta==Risposta3 or Bicicletta==Risposta4:
    Prezzo=(PrezzoFissoMountainBike+PrezzoFissoTurismo)*Ore*NBiciTeM
Prezzo=int(Prezzo) #Questo passaggio serve per trasformare la variabile del prezzo da numero decimale a numero intero
print("Il prezzo che dovete pagare è" ,Prezzo, "€")
