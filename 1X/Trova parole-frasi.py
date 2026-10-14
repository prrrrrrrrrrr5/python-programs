import glob, os
import tkinter

documenti = {}
documenti_trovati = []

os.chdir("C:\Users\IVAN\Desktop\File Testo")
for nome_documento in glob.glob(".txt"):
    documento = open(nome_documento,"r")
    testo = documento.read().lower()
    documento.close()
    documenti[nome_documento] = testo

finestra_principale = tkinter.Tk()

menu_ricerca = tkinter.Frame(finestra_principale)
menu_ricerca.grid(sticky=tkinter.N)
tkinter.Label(menu_ricerca,
              text="Frase o parola da cercare").grid(row=0)
campo_di_ricerca = tkinter.Entry(menu_ricerca)
