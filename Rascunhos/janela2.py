import tkinter as tk
class Janela2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # cria os widgets
        self.label = tk.Label(self, text="Janela 2")
        self.button = tk.Button(self, text="Voltar para Janela 1", command=self.ir_para_janela1)
        
        # posiciona os widgets na grid
        self.label.grid(row=0, column=0)
        self.button.grid(row=1, column=0)
        
    def ir_para_janela1(self):
        # destroi a janela atual
        self.destroy()
        
        # cria a nova janela
        janela1 = Janela1(self.master)
        janela1.grid(row=0, column=0)