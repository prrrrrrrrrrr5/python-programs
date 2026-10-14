import numpy as np
import matplotlib.pyplot as plt

def figura(punti):
    for i in range(len(punti)):
        plt.plot(punti[i],punti[i-1])

def traslazione(n,lista):
    for i in range(n):
        vx=float(input("Inserisci di seguito la componente x del vettore \n --> "))
        vy=float(input("Inserisci di seguito la componente y del vettore \n --> "))
        t=np.array([[1,0,vx],[0,1,vy],[0,0,1]])
        p=np.array([lista[i][0],lista[i][1],[1]])
        z=np.dot(t,p)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()
def simmetriaX(n,lista):
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[1,0],[0,-1]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()

def simmetriaY(n,lista):
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[-1,0],[0,1]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()
    
def simmetriaO(n,lista):
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[-1,0],[0,-1]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()
    
def simmetria13(n,lista):
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[0,1],[1,0]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()
    
def simmetria24(n,lista):
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[0,-1],[-1,0]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()

def rotazioneOraria(n,lista):
    g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
    g=np.radians(g)
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[np.cos(g),np.sin(g)],[-np.sin(g),np.cos(g)]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()
    
def rotazioneAnti(n,lista):
    g=float(input("Di quanti gradi (degrees) vuoi ruotare il punto? \n --> "))
    g=np.radians(g)
    for i in range(n):    
        pos=np.array(lista[i])
        t=np.array([[np.cos(g),-np.sin(g)],[np.sin(g),np.cos(g)]])
        z=np.dot(t,pos)
        x1=z[0]
        y1=z[1]
        plt.plot(x1,y1, color="red", marker="o")
        plt.plot(lista[i],[x1,y1],color="red")
    plt.show()

def setGrafico():
    plt.figure(figsize=(5,5))
    plt.subplot().grid()
    plt.subplot().axhline(0, linestyle="solid", color="black")
    plt.subplot().axvline(0, linestyle="solid", color="black")

def setPunti(x,y):
    plt.plot(x,y, color="green", marker="o")

punti=[]
n=int(input("Quanti punti ha la figura? \n --> "))
for i in range(n):
    x=float(input("Inserisci di seguito la posizione x del punto \n --> "))
    y=float(input("Inserisci di seguito la posizione y del punto \n --> "))
    punti.append([x,y])

setGrafico()

for i in range(len(punti)):
    setPunti(punti[i][0],punti[i][1])

isometria=input("Scegliere il tipo di isometria che vuoi sia effettuata (fare copia e incolla senza aggiungere spazi)) : \ntraslazione\nsimmetria asse x\nsimmetria asse y\nsimmetria origine\nsimmetria bisettrice 1 e 3 quad\nsimmetria bisettrice 2 e 4 quad\nrotazione antioraria\nrotazione oraria\n--> ").lower()


if isometria=="traslazione":
    traslazione(n,punti)
else:
    if isometria=="simmetria asse x":
        simmetriaX(n,punti)
    else:
        if isometria=="simmetria asse y":
            simmetriaY(n,punti)
        else:
            if isometria=="simmetria origine":
                simmetriaO(n,punti)
            else:
                if isometria=="simmetria bisettrice 1 e 3 quad":
                    simmetria13(n,punti)
                else:
                    if isometria=="simmetria bisettrice 2 e 4 quad":
                        simmetria24(n,punti)
                    else:
                        if isometria=="rotazione oraria":
                            rotazioneOraria(n,punti)
                        else:
                            if isometria=="rotazione antioraria":
                                rotazioneAnti(n,punti)


