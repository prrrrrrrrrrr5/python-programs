from GUI import *

class Prova(GUI4W):
    
    def creaWidget(self):
        self.__l=tk.Label(text="Prova")
        self.__b=tk.Button(text="Bottone", command=self.bottone)
        self.__cb=ttk.Combobox(values=[1,2,3], state="readonly")
        
    def lM(self):
        self.__l.place(x=10,y=10)
        self.__b.place(x=10,y=30)
        self.__cb.place(x=10,y=50)
        
        
    def bottone(self):
        self.__b.config(bg="#007FFF")
        
p=Prova("Prova","300x300")