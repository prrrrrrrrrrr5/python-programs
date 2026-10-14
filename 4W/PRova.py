import tkinter as tk
from tkinter import messagebox

class IAQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz sull'Intelligenza Artificiale")
        self.geometry("400x300")
        
        # Domande e risposte del quiz
        self.questions = [
            {
                "question": "Che cos'è l'intelligenza artificiale?",
                "options": ["Simulazione del pensiero umano", "Una macchina che pensa come un umano", "Un software per giochi", "Un algoritmo di ricerca"],
                "answer": "Simulazione del pensiero umano"
            },
            {
                "question": "Chi è considerato il padre dell'intelligenza artificiale?",
                "options": ["Alan Turing", "John McCarthy", "Marvin Minsky", "Geoffrey Hinton"],
                "answer": "John McCarthy"
            },
            {
                "question": "Cos'è un algoritmo di apprendimento supervisionato?",
                "options": ["Un algoritmo che impara senza supervisioni", "Un algoritmo che apprende da dati etichettati", "Un algoritmo che prende decisioni casuali", "Un algoritmo che ripete gli stessi passi"],
                "answer": "Un algoritmo che apprende da dati etichettati"
            },
            {
                "question": "Cosa significa il termine 'deep learning'?",
                "options": ["Apprendimento attraverso strutture profonde", "Apprendimento tramite l'intelligenza umana", "Apprendimento senza supervisione", "Un tipo di linguaggio di programmazione"],
                "answer": "Apprendimento attraverso strutture profonde"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.creaWidget()  # Crea i widget
        self.lM()  # Posiziona i widget

    def creaWidget(self):
        # Crea tutti i widget necessari per il quiz
        self.question_label = tk.Label(self, text="", wraplength=350, font=('Arial', 14), justify='left')
        
        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self, text="", variable=self.var, value="", font=('Arial', 12), command=self.check_answer)
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(self, text="Prossima domanda", command=self.next_question, font=('Arial', 12), state=tk.DISABLED)

    def lM(self):
        # Posiziona i widget sulla finestra
        self.question_label.pack(pady=20)
        
        for i, button in enumerate(self.option_buttons):
            button.pack(anchor='w', padx=20)
        
        self.next_button.pack(pady=20)
        
        self.load_question()  # Carica la prima domanda

    def load_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option, value=option)
        
        self.var.set(None)
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_answer == correct_answer:
            self.score += 1
        
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Risultato", f"Il tuo punteggio finale è: {self.score}/{len(self.questions)}")
        self.quit()

if __name__ == "__main__":
    app = IAQuizApp()
    app.mainloop()
