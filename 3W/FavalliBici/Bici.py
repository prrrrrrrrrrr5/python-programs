#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
class Bici:
    def __init__(self,marca,modello,colore):
        self.__marca=marca
        self.__modello=modello
        self.__colore=colore
        self.__gonfio=False
        self.__lucchetto=True
        self.__fanale=False
        self.__pressione=0
        self.__ok=False
    def getMarca(self):
        return self.__marca
    def getModello(self):
        return self.__modello
    def getColore(self):
        return self.__colore
    def getGonfio(self):
        if self.__gonfio:
            return "gonfia"
        else:
            return "non gonfia"
    def getLucchetto(self):
        if self.__lucchetto:
            return "aperto"
        else:
            return "chiuso"
    def getFanale(self):
        if self.__fanale:
            return "acceso"
        else:
            return "spento"
    def getPressione(self):
        return self.__pressione
    def setColore(self,colore):
        self.__colore=colore
    def gonfiare(self):
        self.__pressione+=0.5
        if self.__pressione>=2 and self.__pressione<3.6:
            self.__gonfio=True
    def lucchetto(self,domanda):
        if domanda=="chiudere":
            self.__lucchetto=True
        else:
            if domanda=="aprire":
                self.__lucchetto=False
    def fanale(self,domanda):
        if domanda=="accendere":
            self.__fanale=True
        else:
            if domanda=="spegnere":
                self.__fanale=False
    def ok(self):
        if self.__gonfio and not self.__lucchetto:
            self.__ok=True
    def __str__(self):
        self.ok()
        if self.__ok:
            return "La bicicletta marca "+str(self.__marca)+" modello "+str(self.__modello)+" colore "+str(self.__colore)+" con il fanale "+str(self.getFanale())+" con il lucchetto "+str(self.__lucchetto)+" può partire"
        else:
            return "La bicicletta marca "+str(self.__marca)+" modello "+str(self.__modello)+" colore "+str(self.__colore)+" con il fanale "+str(self.getFanale())+" con il lucchetto "+str(self.__lucchetto)+" non può partire"
            