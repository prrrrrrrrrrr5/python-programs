import numpy as np
import matplotlib.pyplot as plt

def showPlot():
    plt.plot(x,y, color="red", marker="o")
    plt.show()

x=float(input("Inserisci di seguito la posizione x del punto \n --> "))
y=float(input("Inserisci di seguito la posizione y del punto \n --> "))
isometria=input("Scegliere il tipo di isometria che vuoi sia effettuata (fare copia e incolla senza aggiungere spazi)) : \ntraslazione\nsimmetria asse x\nsimmetria asse y\nsimmetria origine\nsimmetria bisettrice 1 e 3 quad\nsimmetria bisettrice 2 e 4 quad\nrotazione antioraria\nrotazione oraria\n--> ").lower()
pos=np.array([x,y])
plt.subplot().grid()
plt.subplot().axhline(0, linestyle="solid", color="black")
plt.subplot().axvline(0, linestyle="solid", color="black")
plt.plot(x,y, color="green", marker="o")


if isometria=="traslazione":
    vx=float(input("Inserisci di seguito la componente x del vettore \n --> "))
    vy=float(input("Inserisci di seguito la componente y del vettore \n --> "))
    t=np.array([[1,0,vx],[0,1,vy],[0,0,1]])
    p=np.array([[x],[y],[1]])
    z=np.dot(t,p)
    x=z[0]
    y=z[1]
    showPlot()
else:
    if isometria=="simmetria asse x":
        t=np.array([[1,0],[0,-1]])
        z=np.dot(t,pos)
        x=z[0]
        y=z[1]
        showPlot()
    else:
        if isometria=="simmetria asse y":
            t=np.array([[-1,0],[0,1]])
            z=np.dot(t,pos)
            x=z[0]
            y=z[1]
            showPlot()
        else:
            if isometria=="simmetria origine":
                t=np.array([[-1,0],[0,-1]])
                z=np.dot(t,pos)
                x=z[0]
                y=z[1]
                showPlot()
            else:
                if isometria=="simmetria bisettrice 1 e 3 quad":
                    t=np.array([[0,1],[1,0]])
                    z=np.dot(t,pos)
                    x=z[0]
                    y=z[1]
                    showPlot()
                else:
                    if isometria=="simmetria bisettrice 2 e 4 quad":
                        t=np.array([[0,-1],[-1,0]])
                        z=np.dot(t,pos)
                        x=z[0]
                        y=z[1]
                        showPlot()
                    else:
                        if isometria=="rotazione oraria":
                            g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                            t=np.array([[np.cos(g),-np.sin(g)],[np.sin(g),np.cos(g)]])
                            z=np.dot(t,pos)
                            x=z[0]
                            y=z[1]
                            showPlot()
                        else:
                            if isometria=="rotazione antioraria":
                                g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                                t=np.array([[np.cos(g),np.sin(g)],[-np.sin(g),np.cos(g)]])
                                z=np.dot(t,pos)
                                x=z[0]
                                y=z[1]
                                showPlot()
