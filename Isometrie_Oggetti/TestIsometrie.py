from Isometrie import *

x=float(input("Inserisci di seguito la posizione x del punto \n --> "))
y=float(input("Inserisci di seguito la posizione y del punto \n --> "))
isom=Isometrie(x,y)
isom.setGrafico(x, y)
isometria=input("Scegliere il tipo di isometria che vuoi sia effettuata (fare copia e incolla senza aggiungere spazi)) : \ntraslazione\nsimmetria asse x\nsimmetria asse y\nsimmetria origine\nsimmetria bisettrice 1 e 3 quad\nsimmetria bisettrice 2 e 4 quad\nrotazione antioraria\nrotazione oraria\n--> ").lower()

if isometria=="traslazione":
    vx=float(input("Inserisci di seguito la componente x del vettore \n --> "))
    vy=float(input("Inserisci di seguito la componente y del vettore \n --> "))
    isom.traslazione(vx, vy)
else:
    if isometria=="simmetria asse x":
        isom.simmetriaX()
    else:
        if isometria=="simmetria asse y":
            isom.simmetriaY()
        else:
            if isometria=="simmetria origine":
                isom.simmetriaO()
            else:
                if isometria=="simmetria bisettrice 1 e 3 quad":
                    isom.simmetria13()
                else:
                    if isometria=="simmetria bisettrice 2 e 4 quad":
                        isom.simmetria24()
                    else:
                        if isometria=="rotazione oraria":
                            g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                            isom.rotazioneOrario(g)
                        else:
                            if isometria=="rotazione antioraria":
                                g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                                isom.rotazioneAnti(g)
