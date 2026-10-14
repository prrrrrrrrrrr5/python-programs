#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Ente:
    def __init__(self,nome,cifraB,cifraR):
        self.__nome=nome
        self.__cifraB=cifraB
        self.__cifraR=cifraR
        self.__quoteB=0
        self.__quoteR=0
        self.__contatoreR=0
        self.__contatoreB=0
        self.__quote=0
        self.__tasse=0
    
    def getContatoreR(self):
        return self.__contatoreR
    def getContatoreB(self):
        return self.__contatoreB
    def getTasse(self):
        return self.__tasse
    def getQuoteR(self):
        return self.__quoteR
    def getQuoteB(self):
        return self.__quoteB
    def getQuote(self):
        return self.__quote
    def getCifraR(self):
        return self.__cifraR
    def getCifraB(self):
        return self.__cifraB
    def getNome(self):
        return self.__nome
    def setCifraR(self,cifraR):
        self.__cifraR=cifraR
    def setCifraB(self,cifraB):
        self.__cifraB=cifraB
    
    def adotta(self,persona,soldi):
        self.__quote+=soldi
        if persona==1:
            self.__quoteR+=soldi
            if self.__quoteR>=self.__cifraR:
                self.__contatoreR+=self.__quoteR//self.__cifraR
                self.__quoteR=self.__quoteR%self.__cifraR
        else:
            if persona==2:
                self.__quoteB+=soldi
                if self.__quoteB>=self.__cifraB:
                    self.__contatoreB+=self.__quoteB//self.__cifraB
                    self.__quoteB+=self.__quoteB%self.__cifraB
    

    def tasse(self):
        if self.__quote>=10000:
            self.__tasse=self.__quote*0.3
        else:
            self.__tasse=self.__quote*0.2

    def __str__(self):
        self.tasse()
        return "Al centro di adozione "+str(self.__nome)+" al costo di "+str(self.__cifraB)+" per bambino e "+str(self.__cifraR)+" per ragazzo sono stati adottati "+str(self.__contatoreB)+" bambini, "+str(self.__contatoreR)+" ragazzi, sono stati versati "+str(self.__quote)+" soldi e sono state pagate di tasse "+str(self.__tasse)+" soldi"