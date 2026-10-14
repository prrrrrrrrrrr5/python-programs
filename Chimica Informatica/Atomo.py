class Atomo:
    def __init__(self,elemento,numeriOss,elettr):
        self.__elemento=elemento
        self.__numeriOss=numeriOss
        self.__elettr=elettr
    
    def getSimbolo(self):
        return self.__elemento
    def getNumeriOss(self):
        return self.__numeriOss
    def getElettr(self):
        return self.__elettr
