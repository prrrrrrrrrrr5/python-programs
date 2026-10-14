import random
#Inizio
def campo(nr,nc,lvl):
    tabella=[]
    for i in range(nc):
        l1=[]
        for j in range(nr):
            l1.append(0)
        tabella.append(l1)
    px=random.randint(0,nc-1)
    py=random.randint(0,nr-1)
    fx=random.randint(0,nc-1)
    fy=random.randint(0,nr-1)
    del tabella[px][py]
    tabella[px].insert(py,"p")
    del tabella[fx][fy]
    tabella[fx].insert(fy,"f")
    while fx==px and fy==py:
        fx=random.randint(0,nc-1)
        fy=random.randint(0,nr-1)
    cibo=int(nc*nr*0.1)
    for i in range(cibo):
        cx=random.randint(0,nc-1)
        cy=random.randint(0,nc-1)
        if tabella[cx][cy]==0:
            del tabella[cx][cy]
            tabella[cx].insert(cy,1)
    for i in range(nc):
        l1=[]
        for j in range(nr):
            l1.append(0)
        Campo.append(l1)
    del Campo[px][py]
    Campo[px].insert(py,"F")
    return tabella
    return Campo

def posizione(tabella,plx,ply):
    for i in range(len(tabella)):
        for j in range(len(tabella[i])):
            if Campo[i][j]=="F":
                plx=i
                ply=j
    return (plx,ply)

def spostamento(Campo,casella,energia,plx,ply):
    Input=input("Inserisci un tasto per muoverti(w=alto, a=sinistra, s=basso, d=destra) \n  -->").lower()
    if Input=="w":
        del Campo[plx][ply]
        Campo[plx].insert(ply,casella)
        del Campo[plx-1][ply]
        Campo[plx-1].insert(ply,"F")
        energia-=1
    else:
        if Input=="s":
            del Campo[plx][ply]
            Campo[plx].insert(ply,casella)
            del Campo[plx+1][ply]
            Campo[plx+1].insert(ply,"F")
            energia-=1
        else:
            if Input=="a":
                del Campo[plx][ply]
                Campo[plx].insert(ply,casella)
                del Campo[plx][ply-1]
                Campo[plx].insert(ply-1,"F")
                energia-=1
            else:
                if Input=="d":
                    del Campo[plx][ply]
                    Campo[plx].insert(ply,casella)
                    del Campo[plx][ply+1]
                    Campo[plx].insert(ply+1,"F")
                    energia-=1
    return energia

def azione(tabella,plx,ply,energia,attivo):
    if tabella[plx][ply]==1:
        x=random.randint(1,10)
        energia+=x
        print("Hai ottenuto" ,x, "di energia in più")
    else:
        if tabella[plx][ply]=="f":
            attivo=False
            print("Hai vinto")
    return energia,attivo

def stampaBella(Campo):
    for i in range(len(Campo)):
        for j in range(len(Campo[i])):
            print(Campo[i][j],end="\t")
        print()


attivo=True
nr=15
nc=10
energia=0
casella=0
plx=0
ply=0
Campo=[]
lvl=int(input("Inserisci il livello di difficoltà (1, 2, 3) \n --> "))
if lvl==1:
    energia=150
else:
    if lvl==2:
        energia=100
    else:
        energia=50
tabella=campo(nr,nc,lvl)
while attivo:
    stampaBella(Campo)
    plx,ply=posizione(tabella, plx, ply)
    energia=spostamento(Campo,casella,energia,plx,ply)
    plx,ply=posizione(tabella, plx, ply)
    energia,attivo=azione(tabella,plx,ply,energia,attivo)
    if energia<1:
        attivo=False
        print("Energia finita \nHai perso")


# aggiungere miglioramento di papà: un comando che ti permette di vedere
# il percorso già fatto pagando il 10% di energia
# aggiungere energia nell'output