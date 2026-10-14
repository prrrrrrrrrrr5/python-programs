#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
Un libro ha:
	autore, titolo, editore, pagine										punti 10	10
	classificazione data da:											
		prime 3 lettere dell'autore+
		prime 3 lettere del titolo+
		prime 3 lettere dell'editore

	Due libri sono uguali se hanno la stessa classificazione			punti 10	10
	Un libro è maggiore di un altro se ha più pagine					punti 10	10
'''
class Libro():
    def __init__(self,aut,title,edit,pag):
        self.__aut=aut
        self.__title=title
        self.__edit=edit
        self.__pag=pag
        self.__class=self.classifica()
    
    def getAutore(self):
        return self.__aut
    def getTitolo(self):
        return self.__title
    def getEditore(self):
        return self.__edit
    def getPag(self):
        return self.__pag
    def getClassificazione(self):
        return self.__class
    
    def classifica(self):
        return self.__aut[0:3]+self.__title[0:3]+self.__edit[0:3]
    
    def __eq__(self, c):
        return self.__class==c.getClassificazione()
    def __gt__(self,c):
        return self.__pag>c.getPag()
    
    def __str__(self):
        return f"{self.__class}"
        #troppo poco. Di un libro non voglio sapere solo la classificazione!
