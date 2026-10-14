import random
class Neurone:
    def __init__(self):
        self.__si=[]
        self.__no=[]
        self.__saluti=["ciao", "salve", "buongiorno"]
        self.__risposta=""

    def risposta(self,domanda):
        if domanda in self.__si:
            self.__risposta="si"
            print(self.__risposta)
        else:
            if domanda in self.__no:
                self.__risposta="no"
                print(self.__risposta)
            else:
                if domanda in self.__saluti:
                    self.__risposta=random.choice(self.__saluti)
                    print(self.__risposta)
                else:
                    self.__risposta=random.choice(["si","no"])
                    print(self.__risposta)
                    risposta=input("Era la risposta giusta/Era un saluto? ").lower()
                    if risposta=="saluto" and domanda[-1]=="?":
                        risposta=input("Sei sicuro che fosse un saluto e non una domanda? ")
                        if risposta=="si":
                            risposta="saluto"
                        else:
                            risposta=input("La risposta alla domanda era giusta/Era un saluto? ").lower()
                    self.impara(risposta, domanda)

    def impara(self,risposta,domanda):
        if (domanda not in self.__si) or (domanda not in self.__no):
            if self.__risposta=="si" and risposta=="si":
                self.__si.append(domanda)
            else:
                if self.__risposta=="no" and risposta=="si":
                    self.__no.append(domanda)
                else:
                    if self.__risposta=="si" and risposta=="no":
                        self.__no.append(domanda)
                    else:
                        if self.__risposta=="no" and risposta=="no":
                            self.__si.append(domanda)
                        else:
                            if risposta=="saluto":
                                self.__saluti.append(domanda)
