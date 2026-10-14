#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Una biblioteca ha:
	un nome, 
	un tipo (cittadina, universitaria, scolastica)
			in ordine di importanza
	una lista di libri													punti 20	20
	
Una biblioteca è > di un'altra se:										punti 20	20
	ha più libri o
	a parità di libri
		ha un tipo migliore

'''
class Biblioteca:
    def __init__(self,nome,tipo,libri):
        self.__nome=nome
        self.__tipo=tipo
        self.__libri=libri
    def getNome(self):
        return self.__nome
    def getTipo(self):
        return self.__tipo
    def getLibri(self):
        return self.__libri
    def setNome(self,nome):
        self.__nome=nome
    def setTipo(self,tipo):
        self.__tipo=tipo
    def setLibri(self,libri):
        self.__libri=libri

    def __gt__(self,c):
        if len(self.__libri)>len(c.getLibri()):
            return True
        else:
            if len(self.__libri)==len(c.getLibri()) and self.__tipo>c.getTipo():
                return True
            else:
                return False
    def __str__(self):
				#troppo furbo 
        if self.__tipo == 1:
            temp = 'cittadina'
        else:
            if self.__tipo == 2:
                temp = 'universitaria'
            else:
                temp = 'scolastica'
                
        return f"La biblioteca {temp} {self.__nome} con i seguenti libri: " #dovete mettere qui la lista dei libri
                
