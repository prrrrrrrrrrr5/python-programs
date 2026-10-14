from abc import *
import tkinter as tk
import tkinter.ttk as ttk

class GUI4W(tk.Tk,ABC):
    
    def __init__(self,t,g):
        super().__init__()
        self.title(t)
        self.geometry(g)
        self.creaWidget()
        self.lM()
        self.mainloop()

    @abstractmethod
    def creaWidget(self):
        pass
    
    @abstractmethod
    def lM(self):
        pass
