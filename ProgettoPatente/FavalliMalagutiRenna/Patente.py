from GUI4W import *
from Quiz import *
from SimulatoreGuida import *
import random

class EsameDellaPatente(GUI4W):
    def creaWidget(self):
        self.__istruzioni=tk.Label(text='''                          ISTRUZIONI PER LA PROVA: 
                                  per effettuare l'esame pratico della patente,
                                bisogna prima superare il quiz (massimo 2 errori)''',anchor="center")
        self.__l2=tk.Label(text="ESAME DELLA PATENTE")
        
        
        self.__quiz=tk.Button(text="Quiz Patente 📄")
        self.__quiz.bind("<Button>", self.evento)
        self.__sim=tk.Button(text="Simulatore Guida 🚗", state=tk.DISABLED)
        self.__sim.bind("<Button>", self.evento)
        
        
        
    def lM(self):
        self.config(bg="tomato") 
        self.__istruzioni.config(bg="tomato",font=("Helvetica", 8, "bold"))
        self.__l2.config(bg="tomato",font=("Times New Roman", 20, "bold"))
        self.__quiz.place(x=200,y=200)
        self.__sim.place(x=190, y=240)
        self.__istruzioni.place(x=19,y=130)
        self.__l2.place(x=90, y=90)
    
    
    def apriScheda(self):
        self.__nF=Quiz()
        print("o")
    
    def evento(self, event):
        if event.widget == self.__quiz:
            self.__nF = Quiz()
            self.wait_window(self.__nF)
            print("Quiz terminato con punteggio:", self.__nF.get_punteggio())

            if self.__nF.get_punteggio() > 7:
                self.__sim.config(state=tk.NORMAL)
                msg.showinfo("Complimenti!", "Hai superato il quiz! Il simulatore è sbloccato.")
            else:
                msg.showwarning("Mi dispiace", "Non hai superato il quiz. Riprovaci!")
        else:
            if event.widget==self.__sim:
                self.__sG=SimulatoreGuida(self.fine_prova_guida)
                
    def fine_prova_guida(self, superata):
        if superata:
            self.__attestato_btn = tk.Button(text="Ricevi Attestato 🎓", command=self.chiedi_dati_attestato)
            self.__attestato_btn.place(x=180, y=280)

    def chiedi_dati_attestato(self):
        finestra = tk.Toplevel(self)
        finestra.title("Inserisci Dati per Attestato")
        finestra.geometry("300x200")

        tk.Label(finestra, text="Nome:").pack(pady=5)
        entry_nome = tk.Entry(finestra)
        entry_nome.pack()

        tk.Label(finestra, text="Cognome:").pack(pady=5)
        entry_cognome = tk.Entry(finestra)
        entry_cognome.pack()

        def genera_attestato():
            nome = entry_nome.get()
            cognome = entry_cognome.get()
            if nome and cognome:
                messagebox.showinfo("Attestato", f"Congratulazioni {nome} {cognome}, hai ottenuto la patente!")
                finestra.destroy()
            else:
                messagebox.showwarning("Attenzione", "Compila entrambi i campi.")

        tk.Button(finestra, text="Genera Attestato", command=genera_attestato).pack(pady=20)
    
g=EsameDellaPatente("Esame Della Patente","500x400")

