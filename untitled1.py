'''
(* Una ditta gestisce sacchi di cereali per l'Italia e il Regno Unito
*  (kg/euro per l'Italia, pound/sterline per il Regno Unito)
* 
*  creare un programma utilizzabile per piu' tipi di cereali che:
*  
* selezionato il paese (IT-Italia / GB-Great Britain))							
* chiesto il prezzo del cereale in questo modo: euro al kg (Italia) 
		/ sterline al pound (Regno Unito)
* chiesto il numero di sacchi
* 
* 1) carichi i dati dei sacchi:											punti 20	
* 	 a)identificativo
* 	 b)peso: in kg (Italia) / in pound (Regno Unito)
* 	 c)prezzo: peso per prezzo
* 
* 3) visualizzi l'elenco con un output di questo tipo:					punti 20	
* 	 Il sacco <identificativo> pesa <peso> kg e 
* 	 costa <prezzo> euro	(Italia)
* 	oppure
* 	 Il sacco <identificativo> pesa <peso> pound e 
* 	 costa <prezzo> sterline (Regno Unito)
* 
* 4) visualizzi l'elenco con un output come il precedente:				punti 20	
* 	 convertendo euro/kg in pound/sterline o viceversa.
* 	 Sapendo che 1 kg=2.2 pound e 1 euro=0.91 sterline
* 
* 5) realizza una ricerca per id										punti 20	 
*
* commenti																punti 5		
* si compila? NO														punti -2	
 
* Totale																Punti 85	
* Sufficienza															Punti 51
* Voto				
* Voto reale		
* Note			
*)
'''

#Inizio

def inserimento(lista,lista2,l1,l2,avanti):
    while avanti=="si":
        l1=[]
        l2=[]
        paese=input("Inserisci di seguito il paese (IT per Italia, GB per Regno Unito) \n --> ").upper()
        l2.append(paese)
        nome=input("Inserisci di seguito il nome del cereale \n --> ")
        Id=input("Inserisci di seguito l'id del sacco \n --> ")
        l1.append(Id)
        sacchi=int(input("Quanti sacchi hai? \n --> "))
        if paese=="IT":
            peso=float(input("Inserisci di seguito il peso (in kg) del sacco \n --> "))
            l1.append(peso)
            prezzo=float(input("Inserisci di seguito il prezzo del sacco (in euro) del sacco \n --> "))
            l1.append(prezzo)
            prezzo2=float(input("Inserisci di seguito il prezzo in euro al kg del cereale \n --> "))
            l2.append(prezzo2)            
        else:
            if paese=="GB":
                peso=float(input("Inserisci di seguito il peso (in pound) del sacco \n --> "))
                l1.append(peso)
                prezzo=float(input("Inserisci di seguito il prezzo del sacco (in sterline) del sacco \n --> "))
                l1.append(prezzo)
                prezzo2=float(input("Inserisci di seguito il prezzo in sterline al pound del cereale \n --> "))
                l2.append(prezzo2)
                sacchi=int(input("Quanti sacchi hai? \n --> "))
                l2.append(sacchi)
        l1.append(nome)
        lista.append(l1)
        lista2.append(l2)
        avanti=input("Ci sono altri pacchi? \n --> ").lower()

def stampaBella(lista,lista2):
    #Stampa normale
    for i in range(len(lista)):
        if lista2[i][0]=="IT":
            print("Il sacco" ,lista[i][0], "pesa" ,lista[i][1], "kg e costa" ,lista[i][2], "euro")
        else:
            if lista2[i][0]=="GB":
                print("Il sacco" ,lista[i][0], "pesa" ,lista[i][1], "pound e costa" ,lista[i][2], "sterline")
    #Stampa invertita
    for i in range(len(lista)):
        if lista2[i][0]=="IT":
            print("Il sacco" ,lista[i][0], "pesa" ,lista[i][1]*2.2, "pound e costa" ,lista[i][2]*0.91, "sterline")
        else:
            if lista2[i][0]=="GB":
                print("Il sacco" ,lista[i][0], "pesa" ,lista[i][1]/2.2, "kg e costa" ,lista[i][2]/0.91, "euro")

def ricerca(lista,trovato):
    Input=input("Inserisci di seguito l'id del pacco che vuoi cercare \n --> ")
    for i in range(len(lista)):
        if lista[i][0]==Input:
            trovato=True

#Main
lista=[]
lista2=[]
l1=[]
l2=[]
avanti="si"
inserimento(lista,lista2,l1,l2,avanti)
stampaBella(lista,lista2)
avanti="si"
trovato=False
while trovato==False:
    trovato=ricerca(lista,lista2)