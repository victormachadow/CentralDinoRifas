import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("500x500")
        
        # Cria as janelas
        self.janela_inicial = JanelaInicial(self)
        self.janela_secundaria = JanelaSecundaria(self)
        
        # Configura a janela inicial para ser a primeira a aparecer
        self.janela_inicial.show()
        
    def show_janela_secundaria(self):
        # Esconde a janela inicial e mostra a janela secundária
        self.janela_inicial.hide()
        self.janela_secundaria.show()
        
    def show_janela_inicial(self):
        # Esconde a janela secundária e mostra a janela inicial
        self.janela_secundaria.hide()
        self.janela_inicial.show()
        
        
class JanelaInicial:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="Janela Inicial")
        self.label.pack()
        
        self.botao = tk.Button(self.frame, text="Ir para Janela Secundária", command=self.master.show_janela_secundaria)
        self.botao.pack()
        
    def show(self):
        self.frame.pack()
        
    def hide(self):
        self.frame.pack_forget()
        
        
class JanelaSecundaria:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="Janela Secundária")
        self.label.pack()
        
        self.textBox = tk.Text(self.frame, width=30, height=10)
        self.textBox.pack()
        
        self.botao = tk.Button(self.frame, text="Voltar para Janela Inicial", command=self.master.show_janela_inicial)
        self.botao.pack()
        
    def show(self):
        self.frame.pack()
        
    def hide(self):
        self.frame.pack_forget()
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()
