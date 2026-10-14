import tkinter

finestra=tkinter.Tk()
finestra.geometry("275x65")
finestra.title("Differenza")

menu=tkinter.Frame(finestra)
menu.grid(sticky=tkinter.N)
tkinter.Label(menu,
              text="Inserire primo numero").grid(row=0)
camporicerca=tkinter.Entry(menu)
camporicerca.grid(row=0, column=1)
tkinter.Button(menu, text="Avanti").grid(row=1)
