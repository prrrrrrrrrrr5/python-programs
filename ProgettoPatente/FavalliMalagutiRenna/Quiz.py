from PIL import Image, ImageTk
import os
import random
import tkinter as tk

class Quiz(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Quiz Patente")
        self.geometry("500x300")
        self.__indice=0
        self.__punteggio=0
        self.creaWidget()
        self.lM()
        #self.mainloop()
    
    def creaWidget(self):
        print(self.__indice,self.__punteggio)
        
        self.config(bg="#d0e4d4")
        
        self.__domande=["Il caravan non è un rimorchio",
                        "Quando il traffico risulta canalizzato, è possibile che nella corsia di destra si circoli ad una velocità superiore a quella di sinistra",
                        "Durante un sorpasso in autostrada, mantenersi troppo a lungo sulla corsia di sorpasso può essere motivo di intralcio",
                        "Il segnale raffigurato è un segnale di divieto",
                        "Il segnale raffigurato consente la circolazione ai veicoli che procedono a velocità uguale o superiore a quella indicata",
                        "Chi guida autoveicoli o motocicli deve mostrare, a richiesta degli agenti, l'attestazione di pagamento della tassa di possesso (bollo)",
                        "Il segnale raffigurato preannuncia un incrocio in cui si ha la precedenza sui veicoli provenienti da sinistra",
                        "Se un infortunato della strada ha un'abbondante emorragia esterna, si deve coprire la ferita e far camminare l'infortunato",
                        "Il pannello integrativo raffigurato indica di diminuire la distanza di sicurezza",
                        "La fermata di breve durata è consentita anche in curva",
                        "È bene che il casco sia dotato di visiera",
                        "Non è necessario mettere a punto i freni squilibrati, se il conducente è in grado di correggere l'anomalo comportamento del veicolo agendo sullo sterzo",
                        "La responsabilità civile connessa al sinistro stradale si limita al risarcimento dei danni alle sole cose",
                        "Il traino per incombente situazione di emergenza di un veicolo in avaria deve avvenire attraverso un solido collegamento, anche se non è possibile segnalarlo",
                        "Il segnale raffigurato può essere preceduto da un segnale di preavviso",
                        "Per salvaguardare l'ambiente dall'inquinamento atmosferico e acustico, quando si cambia marcia bisogna premere a fondo il pedale dell'acceleratore",
                        "Il simbolo raffigurato è posto su un dispositivo che dà indicazioni sulla pressione del lubrificante nel motore",
                        "Il segnale raffigurato preannuncia una confluenza sia da destra che da sinistra",
                        "In presenza del segnale DARE PRECEDENZA occorre usare prudenza e moderare la velocità, ma occorre arrestarsi solo in caso di necessità",
                        "Il valore della distanza di sicurezza deve essere stabilito anche in base all'efficienza dei freni",
                        "La sospensione della patente è disposta quando il conducente circola abusivamente con veicolo sottoposto a sequestro",
                        "Le frecce direzionali in figura indicano ai conducenti le direzioni consentite all'incrocio",
                        "In caso di nebbia fitta è opportuno se costretti a fermarsi sulla carreggiata, usare la segnalazione luminosa di pericolo (quattro frecce lampeggianti simultaneamente)",
                        "Durante le operazioni di presegnalazione con il segnale mobile di pericolo il conducente deve indossare il giubbotto ad alta visibilità anche se si trova sulle corsie di emergenza o sulle piazzole di sosta",
                        "Giungendo all'incrocio rappresentato in figura i veicoli passano nel seguente ordine: H, D, B, L",
                        "Il segnale raffigurato preannuncia un divieto di transito agli autobus",
                        "In un veicolo a motore, gli ammortizzatori scarichi aumentano il rischio di rottura delle molle delle sospensioni",
                        "Nell'incrocio rappresentato in figura il veicolo A passa per primo",
                        "Il segnale raffigurato indica che bisogna svoltare a sinistra al secondo incrocio per raggiungere l'Austria",
                        "Se lo sterzo vibra si deve far controllare la bilanciatura delle ruote posteriori"]
        #self.__risposte=["F","F","V","V","F","F","F","F","F","F","V","F","V","V","F","F","V","V","V","V","V","V","V","V","V","F","V","V","V","F"]
        self.__risposte=["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F"]
        
        self.__d2=[random.choice(self.__domande) for i in range(10)]
        
        self.__l = tk.Label(
        self,
        text=self.__d2[0],
        bg="#d0e4d4",
        wraplength=450,  # si adatta alla larghezza della finestra
        justify="left",  # allinea il testo a sinistra
        font=("Helvetica", 12)
        )

        # Pulsanti vero/falso
        self.__v = tk.Button(self, text="Vero", width=10, command=self.vero)
        self.__f = tk.Button(self, text="Falso", width=10, command=self.falso)
        
        # Canvas per immagine (spazio vuoto)
        self.__c = tk.Canvas(self, width=200, height=150, bg="white", highlightthickness=1, highlightbackground="black")
        self.mostraImmagine(self.__domande.index(self.__d2[0]))
        

    def lM(self):
        # Domanda in alto
        self.__l.place(x=25, y=20)
        
        # Sotto: immagine a sinistra
        self.__c.place(x=25, y=100)

        # Pulsanti a destra dell'immagine
        self.__v.place(x=300, y=120)
        self.__f.place(x=300, y=170)


    def vero(self):
        if self.__risposte[self.__indice] == "V":
            self.__punteggio+=1
        self.nextQ()

        
    def falso(self):
        if self.__risposte[self.__indice] == "F":
            self.__punteggio+=1
        self.nextQ()


    def nextQ(self):
        
        print(self.__indice,self.__punteggio)
        self.__indice += 1
        
        if self.__indice < 10:
            self.__l.config(text=self.__d2[self.__indice])
            indice_domanda_originale = self.__domande.index(self.__d2[self.__indice])
            self.mostraImmagine(indice_domanda_originale)
        else:
            # Finito il quiz, mostra il punteggio finale
            self.__l.config(text=f"Quiz finito! Il tuo punteggio è: {self.__punteggio}/{len(self.__d2)}")
            self.__v.config(state="disabled")
            self.__f.config(state="disabled")
            self.__c.delete("all")
            
            self.after(3000, self.destroy)
    
    def get_punteggio(self):
        return self.__punteggio
    
   
    def mostraImmagine(self, indice_domanda):
        if indice_domanda in [3, 4, 6, 8, 14, 16, 17, 21, 24, 25, 27, 28]:
            try:
                path = f"Immagini/{indice_domanda+1}.png"
                img = Image.open(path)
                img = img.resize((200, 150))
                self.__img_tk = ImageTk.PhotoImage(img)
                self.__c.create_image(0, 0, anchor="nw", image=self.__img_tk)
            except Exception as e:
                    print(f"Errore nel caricare l'immagine: {e}")
                    self.__c.delete("all")
        else:
            self.__c.delete("all")



