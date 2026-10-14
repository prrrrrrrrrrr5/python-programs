'''
Progetto nÂ°2 (Chimica): crea un software di simulazione di reazioni chimiche utilizzando la 
programmazione orientata agli oggetti in Python. Prevedi di creare delle classi che rappresentano 
molecole, atomi e legami chimici, e di implementare metodi per simulare le reazioni chimiche tra 
di esse. Il software potrebbe poi mostrare in output la composizione chimica dei prodotti, 
bilanciare le equazioni chimiche e visualizzare le reazioni. Prova ad importare dalla libreria 
sympy, gli elementi Eq e solve()
'''
from Atomo import *
from Legami import *
from Molecola import *

def formula(atomo,tipo):
    if tipo[0]=="atomo" and tipo[1]=="atomo":
        formula=atomi[0].getSimbolo()+atomi[1].getSimbolo()
    else:
        if tipo[0]=="atomo" and tipo[1]=="molecola":
            if atomo[1].getElettr()[0]>atomo[1].getElettr()[1]:
                formula=atomi[0].getSimbolo()+atomi[1].getDivisioni()[0]+"+"+atomi[1].getDivisioni()[1]
            else:
                if atomo[1].getElettr()[1]>atomo[1].getElettr()[0]:
                    formula=atomi[0].getSimbolo()+atomi[1].getDivisioni()[1]+"+"+atomi[1].getDivisioni()[0]
        else:
            if tipo[1]=="atomo" and tipo[0]=="molecola":
                if atomo[0].getElettr()[0]>=atomo[0].getElettr()[1]:
                    formula=atomi[1].getSimbolo()+atomi[0].getDivisioni()[0]+"+"+atomi[0].getDivisioni()[1]
                else:
                    if atomo[0].getElettr()[1]>atomo[0].getElettr()[0]:
                        formula=atomi[1].getSimbolo()+atomi[0].getDivisioni()[1]+"+"+atomi[0].getDivisioni()[0]
            else:
                formula=atomi[0].getDivisioni()[0]+atomi[1].getDivisioni()[1]+"+"+atomi[0].getDivisioni()[1]+atomi[1].getDivisioni()[0]
    return formula

atomi=[]
tipi=[]
elett=[]

for i in range(2):
    tipo=""
    simbolo=input("Inserisci il simbolo dell'elemento o della molecola ")
    if len(simbolo)<=2:
        n=int(input("Quanti numeri di ossidazione sono presenti? "))
        nOss=[int(input("Inserisci numero di ossidazione ")) for i in range(n)]
        elettr=float(input("Inserisci l'elettronegatività dell'atomo "))
        atomo=Atomo(simbolo,nOss,elettr)
        tipo="atomo"
    else:
        tipo="molecola"
        for i in range(2):
            elett.append(float(input("Inserisci l'elettronegatività dei singoli atomi uno alla volta ")))
        atomo=Molecola(simbolo,elett)
    atomi.append(atomo)
    tipi.append(tipo)

print("La reazione è: ",atomi[0].getSimbolo(),"+",atomi[1].getSimbolo()," --> ",formula(atomi,tipi))
