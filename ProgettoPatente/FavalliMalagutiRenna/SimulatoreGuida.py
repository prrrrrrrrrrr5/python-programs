import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class SimulatoreGuida(tk.Toplevel):
    def __init__(self, callback_fine_prova):
        super().__init__()
        self.callback_fine_prova = callback_fine_prova
        self.title("Simulatore di Guida")
        self.geometry("900x600")
        self.angolo_auto = 0
        self.creaWidget()
        self.lM()
        self.bind_all("<Key>", self.muovi_auto)

    def creaWidget(self):
        self.canvas = tk.Canvas(self, bg="lightgray", width=900, height=600)

        try:
            strada_img = Image.open("Immagini/Strada.png").resize((900, 600))
            self.strada_tk = ImageTk.PhotoImage(strada_img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.strada_tk)
        except:
            self.canvas.create_rectangle(0, 0, 900, 600, fill="gray")

        try:
            self.img_auto_original = Image.open("Immagini/Auto.png").resize((40, 60))
            self.img_auto_tk = ImageTk.PhotoImage(self.img_auto_original)
            self.auto = self.canvas.create_image(100, 500, anchor="nw", image=self.img_auto_tk)
        except:
            self.auto = self.canvas.create_rectangle(100, 500, 140, 560, fill="blue")

        self.ostacoli = []
        ostacoli_posizioni = [(300, 450), (500, 350), (600, 250), (700, 150)]
        try:
            self.img_ostacolo = Image.open("Immagini/Ostacolo.png").resize((50, 50))
            self.img_ostacolo_tk = ImageTk.PhotoImage(self.img_ostacolo)
            for x, y in ostacoli_posizioni:
                ost = self.canvas.create_image(x, y, anchor="nw", image=self.img_ostacolo_tk)
                self.ostacoli.append(ost)
        except:
            for x, y in ostacoli_posizioni:
                ost = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="red")
                self.ostacoli.append(ost)

        self.parcheggio = self.canvas.create_rectangle(800, 500, 880, 580, outline="green", width=3)

        self.bordi = [
            self.canvas.create_rectangle(0, 0, 20, 600, fill="black"),
            self.canvas.create_rectangle(880, 0, 900, 600, fill="black"),
            self.canvas.create_rectangle(0, 0, 900, 20, fill="black"),
            self.canvas.create_rectangle(0, 580, 900, 600, fill="black")
        ]

    def lM(self):
        self.canvas.place(x=0, y=0)

    def muovi_auto(self, event):
        dx = dy = 0
        if event.keysym == 'Up':
            dy = -5
            self.angolo_auto = 0
        elif event.keysym == 'Down':
            dy = 5
            self.angolo_auto = 180
        elif event.keysym == 'Left':
            dx = -5
            self.angolo_auto = 270
        elif event.keysym == 'Right':
            dx = 5
            self.angolo_auto = 90

        self.canvas.move(self.auto, dx, dy)
        self.aggiorna_direzione_auto()

        if self.collisione_bordi() or self.collisione_ostacoli():
            messagebox.showerror("Errore", "Prova fallita.")
            self.callback_fine_prova(False)
            self.unbind_all("<Key>")
            self.destroy()
        elif self.in_parcheggio():
            messagebox.showinfo("Successo", "Parcheggio riuscito! Prova superata.")
            self.callback_fine_prova(True)
            self.unbind_all("<Key>")
            self.destroy()

    def aggiorna_direzione_auto(self):
        if hasattr(self, 'img_auto_original'):
            ruotata = self.img_auto_original.rotate(-self.angolo_auto)
            self.img_auto_tk = ImageTk.PhotoImage(ruotata)
            self.canvas.itemconfig(self.auto, image=self.img_auto_tk)

    def collisione_bordi(self):
        coords_auto = self.canvas.bbox(self.auto)
        return any(self.intersezione(coords_auto, self.canvas.bbox(b)) for b in self.bordi)

    def collisione_ostacoli(self):
        coords_auto = self.canvas.bbox(self.auto)
        return any(self.intersezione(coords_auto, self.canvas.bbox(o)) for o in self.ostacoli)

    def in_parcheggio(self):
        return self.intersezione(self.canvas.bbox(self.auto), self.canvas.bbox(self.parcheggio))

    def intersezione(self, box1, box2):
        return not (box1[2] < box2[0] or box1[0] > box2[2] or box1[3] < box2[1] or box1[1] > box2[3])
