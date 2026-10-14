import numpy as np
import matplotlib.pyplot as plt

class Isometrie:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__pos=np.array([x,y])
        
    def getPos(self):
        return self.__pos[0],self.__pos[1]

    #Inizializzazione grafico con il punto da trasformare

    def setGrafico(self,x,y):
        x,y=self.getPos()
        plt.subplot().grid()
        plt.subplot().axhline(0, linestyle="solid", color="black")
        plt.subplot().axvline(0, linestyle="solid", color="black")
        plt.plot(x,y, color="green", marker="o")

    #Trasformazione isometrica: traslazione

    def traslazione(self,vx,vy):
        t=np.array([[1,0,vx],[0,1,vy],[0,0,1]])
        p=np.array([[self.__x],[self.__y],[1]])
        z=np.dot(t,p)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Trasformazione isometrica: simmetria rispetto all'asse x

    def simmetriaX(self):
        t=np.array([[1,0],[0,-1]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Trasformazione isometrica: simmetria rispetto all'asse x

    def simmetriaY(self):
        t=np.array([[-1,0],[0,1]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Trasformazione isometrica: simmetria rispetto all'origine

    def simmetriaO(self):
        t=np.array([[-1,0],[0,-1]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Trasformazione isometrica: simmetria rispetto alla bisettrice del secondo e del quarto quadrante

    def simmetria24(self):    
        t=np.array([[0,-1],[-1,0]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Trasformazione isometrica: simmetria rispetto alla bisettrice del primo e del terzo quadrante

    def simmetria13(self):
        t=np.array([[0,1],[1,0]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Traslazione isometrica: rotazione antioraria

    def rotazioneAnti(self,x):
        t=np.array([[np.cos(x),-np.sin(x)],[np.sin(x),np.cos(x)]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()

    #Traslazione isometrica: rotazione oraria

    def rotazioneOrario(self,x):
        t=np.array([[np.cos(x),np.sin(x)],[-np.sin(x),np.cos(x)]])
        z=np.dot(t,self.__pos)
        self.__x=z[0]
        self.__y=z[1]
        self.showPlot()
    
    #Funzione per mostrare il plot di matlplotlib
    
    def showPlot(self):
        plt.plot(self.__x,self.__y, color="red", marker="o")
        plt.show()
