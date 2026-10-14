#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Crea una classe Bici con:
	marca,modello,colore												punti 20	
	crea le opportune get e set											punti 20	
	crea un metodo per gonfiare le ruote								punti 20	
	crea un metodo per aprire e chiudere il lucchetto					punti 20	
	crea un metodo per accendere e spegnere il fanale					punti 20	
	crea un metodo per decidere se si può usare la bici:				punti 20	
		lucchetto aperto, pressione gomme>2

nel main:																punti 20	
	visualizza: 
			Bicietta marca Rossignoli modello Garibaldi si può usare
			Bicietta marca Bianchi modello Spillo non si può usare
				
																Totale	punti 140	
															Sufficienza	punti 84
Voto			
Voto reale		
Note		
'''

from Bici import *

colore=input("Inserisci di seguito il colore della bici \n --> ")
marca=input("Inserisci di seguito la marca della bici \n --> ")
modello=input("Inserisci di seguito il modello della bici \n --> ")
bici=Bici(marca,modello,colore)
avanti="si"
domanda=input("Il lucchetto della bici è "+str(bici.getLucchetto())+". Vuoi aprire/chiudere il lucchetto? \n --> ").lower()
bici.lucchetto(domanda)
while avanti=="si":
    domanda=input("La pressione della bici è "+str(bici.getPressione())+". Vuoi gonfiare la bici? \n --> ").lower()
    if domanda=="si":
        bici.gonfiare()
    if bici.getPressione()==3.5:
        print("Se la gonfi ancora la ruota esploderà")
    avanti=input("Vuoi gonfiare di nuovo? \n --> ").lower()
    if bici.getPressione()>3.5:
        print("La ruota è esplosa")
        avanti="no"

    
domanda=input("Il fanale della bici è "+str(bici.getFanale())+". Vuoi che il fanale sia acceso o spento? \n --> ").lower()
bici.fanale(domanda)

print(bici)
