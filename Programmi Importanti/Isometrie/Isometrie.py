import numpy as np

class Isometrie:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__pos=np.array([x,y])
        
    def getPos(self):
        return self.__pos[0],self.__pos[1]

    def traslazione(self,vx,vy):
        t=np.array([[1,0,vx],[0,1,vy],[0,0,1]])
        p=np.array([[self.__x],[self.__y],[1]])
        return np.dot(t,p)

    def simmetriaX(self):
        t=np.array([[1,0],[0,-1]])
        return np.dot(t,self.__pos)

    def simmetriaY(self):
        t=np.array([[-1,0],[0,1]])
        return np.dot(t,self.__pos)

    def simmetriaO(self):
        t=np.array([[-1,0],[0,-1]])
        return np.dot(t,self.__pos)

    def simmetria24(self):    
        t=np.array([[0,-1],[-1,0]])
        return np.dot(t,self.__pos)

    def simmetria13(self):
        t=np.array([[0,1],[1,0]])
        return np.dot(t,self.__pos)

    def rotazioneAnti(self,x):
        t=np.array([[np.cos(x),-np.sin(x)],[np.sin(x),np.cos(x)]])
        return np.dot(t,self.__pos)

    def rotazioneOrario(self,x):
        t=np.array([[np.cos(x),np.sin(x)],[-np.sin(x),np.cos(x)]])
        return np.dot(t,self.__pos)
