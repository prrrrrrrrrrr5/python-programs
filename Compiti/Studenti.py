import random

#Inizio

def identificativo(ident):
    scelte="abcdefghijklmnopqrstuvwxyz1234567890"
    Id=[]
    stringa=""
    for i in range(0,5):
        Id.append(random.choice(scelte))
    stringa="".join(Id)
    if Id not in ident:
        ident.append(stringa)

nomi=[]
cognomi=[]
telefono=[]
ident=[]
Input=""
Input2=""
avanti="si"
avanti2="no"
opzione=0
lista=[]
lista2=[]
lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

n=int(input("Quanti ragazzi devono essere aggiunti? \n --> "))
for i in range(n):
    nomi.append(input("Qual'è il nome del ragazzo? \n --> "))
    cognomi.append(input("Qual'è il cognome del ragazzo? \n --> "))
    telefono.append(input("Qual'è il numero di telefono del ragazzo? \n --> "))
    identificativo(ident)

while avanti=="si":
    opzione=int(input("Inserisca il numero dell'opzione desiderata: \n 1. Modificare nominativo o numero di telefono di un ragazzo \n 2. Mostrare l'id e il numero di telefono di un ragazzo tramite nominativo \n 3. Eliminare uno studente tramite nominativo \n 4. Mostrare in ordine alfabetico gli studenti con il cognome compreso tra due lettere inserite \n --> "))
    if opzione==1:
        Input=input("Inserisci di seguito l'id della persona \n --> ")
        x=ident.index(Input)
        domanda=input("Vuoi cambiare nome, cognome o numero di telefono? \n --> ").lower()
        if domanda=="nome":
            nnome=input("Inserisci il nuovo nome \n --> ")
            del nomi[x]
            nomi.insert(x,nnome)
        if domanda=="cognome":
            ncognome=input("Inserisci il nuovo cognome \n --> ")
            del cognomi[x]
            cognomi.insert(x,ncognome)
        if domanda=="numero di telefono":
            ntel=input("Inserisci il nuovo numero di telefono \n --> ")
            del telefono[x]
            telefono.insert(x,ntel)

    if opzione==2:
        Input=input("Inserisci il nome della persona \n --> ")
        Input2=input("Inserisci il cognome della persona \n --> ")
        x=nomi.index(Input)
        if nomi.count(Input)>1:
            x=cognomi.index(Input2)
        else:
            if cognomi.count(Input2)>1:
                x=nomi.index(Input)
        print("L'id è:" ,ident[x], "mentre il numero di telefono è:" ,telefono[x])
    
    if opzione==3:
        while avanti2=="no":
            Input=input("Inserisca l'id della persona \n --> ")
            print("L'id inserito appartiene a" ,nomi[ident.index(Input)]," ",cognomi[ident.index(Input)])
            domanda=input("Vuole eliminare la persona? \n --> ").lower()
            if domanda=="si":
                x=ident.index(Input)
                del nomi[x]
                del cognomi[x]
                del telefono [x]
                del ident[x]
                avanti2="si"
    if opzione==4:
        pr_lett=input("Inserisci di seguito la prima lettera \n --> ").upper()
        ul_lett=input("Inserisci di seguito l'ultima lettera \n --> ").upper()
        lista=cognomi.copy()
        lista.sort()
        x=lettere.index(pr_lett)
        for i in range(x):
            del lettere[0]
        lettere.reverse()
        x=lettere.index(ul_lett)
        for i in range(x):
            del lettere[0]
        lettere.reverse()
        for i in range(len(lista)-1):
            if lista[i][0] not in lettere:
                del lista[i]
                del lista2[i]
        for i in range(len(lista)):
            lista2.append(nomi[cognomi.index(lista[i])])
        for i in range(len(lista)):
            print(lista[i], end="\t")
            print(lista2[i], end="\n")
        lista=[]
        lista2=[]
        lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Fine
