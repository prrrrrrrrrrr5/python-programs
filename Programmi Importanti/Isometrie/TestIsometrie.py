from Isometrie import *
import matplotlib.pyplot as plt

# x=float(input("Inserisci di seguito la posizione x del punto \n --> "))
# y=float(input("Inserisci di seguito la posizione y del punto \n --> "))
isom=Isometrie(1,4)
isometria=input("Inserisci di seguito che tipo di isometria vuoi che sia effettuata (traslazione,simmetria asse x, simmetria asse y, simmetria origine, simmetria bisettrice 1 e 3 quad, simmetria bisettrice 2 e 4 quad, rotazione antioraria, rotazione oraria) \n --> ").lower()
x,y=isom.getPos()
plt.subplot().grid()
plt.subplot().axhline(0, linestyle="solid", color="black")
plt.subplot().axvline(0, linestyle="solid", color="black")
plt.plot(x,y, color="green", marker="o")


if isometria=="traslazione":
    # vx=float(input("Inserisci di seguito la componente x del vettore \n --> "))
    # vy=float(input("Inserisci di seguito la componente y del vettore \n --> "))
    x=isom.traslazione(3,3)[0]
    y=isom.traslazione(3,3)[1]
    plt.plot(x,y, color="red", marker="o")
    plt.show()
else:
    if isometria=="simmetria asse x":
        x=isom.simmetriaX()[0]
        y=isom.simmetriaX()[1]
        plt.plot(x,y, color="red", marker="o")
        plt.show()
    else:
        if isometria=="simmetria asse y":
            x=isom.simmetriaY()[0]
            y=isom.simmetriaY()[1]
            plt.plot(x,y, color="red", marker="o")
            plt.show()
        else:
            if isometria=="simmetria origine":
                x=isom.simmetriaO()[0]
                y=isom.simmetriaO()[1]
                plt.plot(x,y, color="red", marker="o")
                plt.show()
            else:
                if isometria=="simmetria bisettrice 1 e 3 quad":
                    x=isom.simmetria13()[0]
                    y=isom.simmetria13()[1]
                    plt.plot(x,y, color="red", marker="o")
                    plt.show()
                else:
                    if isometria=="simmetria bisettrice 2 e 4 quad":
                        x=isom.simmetria24()[0]
                        y=isom.simmetria24()[1]
                        plt.plot(x,y, color="red", marker="o")
                        plt.show()
                    else:
                        if isometria=="rotazione oraria":
                            g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                            x=isom.rotazioneOrario(g)[0]
                            y=isom.rotazioneOrario(g)[1]
                            plt.plot(x,y, color="red", marker="o")
                            plt.show()
                        else:
                            if isometria=="rotazione antioraria":
                                g=float(input("Di quanti gradi vuoi ruotare il punto? \n --> "))
                                x=isom.rotazioneAnti(g)[0]
                                y=isom.rotazioneAnti(g)[1]
                                plt.plot(x,y, color="red", marker="o")
                                plt.show()
