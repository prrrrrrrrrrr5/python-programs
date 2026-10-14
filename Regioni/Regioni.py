from GUI4W import *

class Regioni(GUI4W):
    
    def creaWidget(self):
        #Creo le etichette
        self.__reg=tk.Label(text="Regione")
        self.__pro=tk.Label(text="Provincia")
        self.__pwd=tk.Label(text="Password:")
        self.__reg2=tk.Label(text="Regione:")
        self.__pro2=tk.Label(text="Provincia:")
        
        #Creo le liste di regioni e provincie
        self.__regioni=["Emilia-Romagna", "Lombardia"]
        self.__provincieER=["Bologna", "Rimini", "Reggio Emilia", "Ferrara", "Forli-Cesena", "Modena", "Parma", "Piacenza", "Ravenna"]
        self.__provincieL=["Milano", "Bergamo", "Lodi", "Como", "Brescia", "Cremona", "Lecco", "Mantova", "Monza e Brianza", "Pavia", "Sondrio", "Varese"]
        self.__provincie=[self.__provincieER, self.__provincieL] #Lista delle liste delle province 
        
        #Creo i menù a tendina
        self.__cReg=ttk.Combobox(values=self.__regioni, state="readonly")
        self.__cReg.current(0) #Metto il primo membro che si vede all'inizio del programma (indice 0)
        self.__cReg.bind("<<ComboboxSelected>>", self.evento) #Lega le robe del menù a tendina all'evento, se non c'è questo, i due combobox non sono legati e quindi non cambiano
        self.__cPro=ttk.Combobox(values=self.__provincie[0], state="readonly")
        self.__cPro.current(0)
        
        #Creo le caselle di testo
        self.__op=tk.Entry()
        self.__op.bind("<FocusOut>", self.evento) #Lega un'azione compiuta sul widget ad un evento (che crei te)
        self.__opReg=tk.Entry(state=tk.DISABLED)
        self.__opPro=tk.Entry(state=tk.DISABLED) 
        self.__opPro.bind("<FocusOut>", self.evento)
    
    def lM(self):
        #Per piazzare tutte le cose
        self.__reg.place(x=10, y=10)
        self.__pro.place(x=10, y=40)
        self.__pwd.place(x=10, y=200)
        self.__reg2.place(x=10, y=230)
        self.__pro2.place(x=10, y=260)
        
        self.__cReg.place(x=70, y=10)
        self.__cPro.place(x=70, y=40)
        
        self.__op.place(x=70, y=200)
        self.__opReg.place(x=70, y=230)
        self.__opPro.place(x=70, y=260)
        
        
    def evento(self,event):
        password="a"
        if event.widget==self.__op: #op sono le caselle di testo
            if self.__op.get()==password: #se quello che hai messo nella casella di testo della password è la password attivi le altre caselle di testo
                self.__opReg.config(state=tk.NORMAL)
                self.__opPro.config(state=tk.NORMAL)
                
        else:
            if event.widget==self.__cReg: #se l'evento è il combobox delle regioni
                x=self.__regioni.index(self.__cReg.get()) #prendi l'index della regione
                self.__cPro.config(values=self.__provincie[x]) #metto la lista di regioni corrispondente
                self.__cPro.current(0) #metto il primo membro che si vede
            
            else:
                if event.widget==self.__opPro: #Se l'evento è la casella di testo dove metti le province
                    x=self.__opReg.get() #x è il testo dentro la casella delle regioni
                    if x not in self.__regioni: #se x non è nella lista delle regioni
                        self.__regioni.append(x) #lo aggiungo alla lista
                        self.__provincie.append([]) #aggiungo alla lista delle province una lista vuota (chè avrà lo stesso indice della regione appena messa)
                    i=self.__regioni.index(x) #prendo l'indice della regione
                    x=self.__opPro.get() #prendo quello che c'è nella casella di testo delle provincie
                    if x not in self.__provincie[i]: #se non c'è già nella lista[i] delle provincie lo aggiungo a quella lista (ovvero la lista con lo stesso indice della regione messa)
                        self.__provincie[i].append(x)
                    
                    self.__cReg.config(values=self.__regioni) #aggiorno i valori delle regioni e delle provincie
                    self.__cPro.config(values=self.__provincie)
                    
                    self.__opReg.config(state=tk.DISABLED) #disattivo le caselle di testo di regione e provincie
                    self.__opPro.config(state=tk.DISABLED)
        
r=Regioni("Regioni","500x500")
