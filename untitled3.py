import tkinter as tk

#Programmazione event driven= guidata dagli eventi
#Evento=interazione dell'utente con l'interfaccia grafica

class CiaoMondo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prova")
        self.geometry("300x300")
        self.creaW()
        self.layoutManager()
        self.mainloop()
	
    def creaW(self):
        self.__l=tk.Label(text="Ciao")
        self.__test=tk.StringVar()
        self.__e=tk.Entry(self,textvariable=self.__test)
        self.__lb=tk.Listbox(selectmode=tk.BROWSE)
        self.__lb.insert(1,"Ciao")
        self.__lb.insert(2,"iao")
        self.__b=tk.Button()
        

	
    def layoutManager(self):
        self.__l.place(x=10,y=10)
        self.__e.place(x=100,y=100)
        self.__lb.place(x=300,y=300)
        self.__b.place(x=500,y=500)
        self.__b.width("50x100")
#wizard of incapsulation pk instanziamo solo senza sapere cosa cè dentro. non possiamo nodificare le loro coseù
#fa tutto lui da solo e teniamo le cose private :) :(
#
c=CiaoMondo()
