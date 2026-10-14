class Molecola:
    def __init__(self,simbolo,elett):
        self.simbolo=simbolo
        self.elettr=elett

    def divisioni(self):
        alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.parti=[]
        simbolo=self.simbolo
        i=0
        while i<len(simbolo):
            if simbolo[i] in alfabeto:
                cont=i
                i+=1
                while i<len(simbolo) and simbolo[i] not in alfabeto:
                    i+=1
                self.parti.append(simbolo[cont:i])
            else:
                i+=1          

    def getDivisioni(self):
        self.divisioni()
        return self.parti
    
    def getElettr(self):
        return self.elettr
    
    def getSimbolo(self):
        return self.simbolo