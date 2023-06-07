import tkinter as tk
from janela2 import Janela2

class Janela1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # cria os widgets
        self.label = tk.Label(self, text="Janela 1")
        self.button = tk.Button(self, text="Ir para Janela 2", command=self.ir_para_janela2)
        
        # posiciona os widgets na grid
        self.label.grid(row=0, column=0)
        self.button.grid(row=1, column=0)
        
    def ir_para_janela2(self):
        # destroi a janela atual
        self.destroy()
        
        # cria a nova janela
        janela2 = Janela2(self.master)
        janela2.grid(row=0, column=0)
        
        
# cria a janela principal
root = tk.Tk()

# cria a primeira janela
janela1 = Janela1(root)
janela1.grid(row=0, column=0)

# define as dimensoes da janela principal
root.geometry("500x500")

# inicia a GUI
root.mainloop()        