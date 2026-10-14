#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Crea due biblioteche:
	visualizza tutti i dati												punti 30	14
	
																Totale  punti 100	84
															Sufficienza punti 60
Voto			8,4
Voto reale		8,5
Note		Bella ma potete fare meglio
'''
from Libro import*
from Biblioteca import *
def inizializza():
    nome=input("Inserisci di seguito il nome della biblioteca \n --> ")
    tipo=0
    while tipo not in [1,2,3]:
        tipo = int(input("inserire tipo di biblioteca secondo la codifica:\ncittadina : 1\nuniversitaria : 2\nscolastica : 3\n--> "))
    n=int(input("Inserire numero di libri \n --> "))
    libri=[]
    for i in range(n):
        autore=input("Inserire autore \n --> ")
        titolo=input("Inserire titolo \n --> ")
        editore=input("Inserire editore \n --> ")
        pagine=int(input("Inserire numero pagine \n --> "))
        libro=Libro(autore,titolo,editore,pagine)
        libri.append(libro)                                              
    biblioteca=Biblioteca(nome,tipo,libri)
    return biblioteca

biblio1 = inizializza()
biblio2 = inizializza()
print(f'prima: {biblio1}')
for i in range(len(biblio1.getLibri())):
	
				#dovete gestirlo nella __str__ !!! chi visualizza la biblioteca non deve sapere che deve lanciare getLibri()[i].getClassificazione()
    print(biblio1.getLibri()[i].getClassificazione())
    #è uguale scrivere
    #print(biblio1.getLibri()[i]) perchè la str di libri ritrona la classificazione
    
print(f'seconda: {biblio2}')
for i in range(len(biblio2.getLibri())): 
    print(biblio2.getLibri()[i].getClassificazione())

if biblio1 > biblio2:
    print('la prima biblioteca è maggiore della seconda')
else:
    print('la seconda è maggiore della prima')
    
for i in range(len(biblio1.getLibri())):
    if biblio1.getLibri()[i].getClassificazione() == biblio2.getLibri()[i].getClassificazione():
        print(f'i libri {biblio1.getLibri[i]} e {biblio2.getLibri[i]}')
    else:
        if biblio1.getLibri()[i].getClassificazione() > biblio2.getLibri()[i].getClassificazione():
            print(f'il libro {biblio1.getLibri[i]} è maggiore di {biblio2.getLibri[i]}')
