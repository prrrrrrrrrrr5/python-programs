import random

class Neurone:
    def __init__(self):
        self.__guess = random.randint(0, 100)
    
    def calcola(self, n):
        cont = 0
        while self.__guess != n:
            if n < self.__guess:
                self.__guess = random.randint(0, self.__guess)
            else:
                if self.__guess < n:
                    self.__guess = random.randint(self.__guess, 100)
            cont += 1
        print("Numero:" ,n, "Guess:" ,self.__guess, "Contatore:", cont)
