class Legami:
    def __init__(self):
        self.__legame=""
    
    def legame(self,atomo1,atomo2):
        if abs(atomo1.getElettr()-atomo2.getElettr())<0.4:
            self.__legame="Covalente polare"
        else:
            if abs(atomo1.getElettr()-atomo2.getElettr())<1.8:
                self.__legame="Covalente apolare"
            else:
                self.__legame="Ionico"
    
    def getLegame(self):
        return self.__legame