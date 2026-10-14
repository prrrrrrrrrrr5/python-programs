#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
    Creare una classe per un ente che gestisce adozioni a distanza		punti 20	
    L'ente ha:
    un nome
    una cifra per l'adozione di un bambino
    una cifra per l'adozione di un ragazzo
        
    Realizza un metodo per la gestione delle adozioni:					punti 20	
		a seconda di chi si vuole adottare
		controlla se si è raggiunta la cifra opportuna
		
	Realizza un metodo per calcolare le tasse:							punti 20	
		se il totale delle quote versate>10000
			si paga il 30% del totale raccolto
		altrineti
			si paga il 20% del totale raccolto
	
    nel main: 															punti 40	
    dato il nome dell'associazione, le quote per le adozioni
    e un numero di persone (0<n<=100)
    chiedere ad ogni persona chi vuole adottare e quanto versa
    visualizzare tutti i dati
    

																 Totale punti 100	
															Sufficienza punti  60
    Voto			
    Voto reale		
    Note        	
'''
from Ente import *
nome=input("Inserisci di seguito il nome dell'ente \n --> ")
cifraB=float(input("Inserisci di seguito la cifra minima per adottare un bambino \n --> "))
cifraR=float(input("Inserisci di seguito la cifra minima per adottare un ragazzo \n --> "))
ente=Ente(nome,cifraB,cifraR)
n=int(input("Inserisci di seguito un nunero di persone maggiore di 0 e minore o uguale a 100 \n --> "))
while n<=0 and n>100:
    n=int(input("Inserisci di seguito un nunero di persone maggiore di 0 e minore o uguale a 100 \n --> "))
for i in range(n):
    persona=int(input("Inserisci 1 se vuoi adottare un ragazzo, 2 se vuoi adottare un bambino, 0 se non vuoi adottare nessuno \n --> "))
    # while persona!=0 or persona!=1 or persona!=2:
    #     persona=int(input("Inserisci 1 se vuoi adottare un ragazzo, 2 se vuoi adottare un bambino, 0 se non vuoi adottare nessuno \n --> "))
    soldi=float(input("Quanti soldi vuoi dare? \n --> "))
    ente.adotta(persona, soldi)
    
print(ente)
