import tkinter as tk

def imprimir_texto():
    texto = caixa_texto.get("1.0", "end")
    print(texto)

janela = tk.Tk()

caixa_texto = tk.Text(janela, width=30, height=10)
caixa_texto.grid(row=1, column=1, rowspan=2)

botao = tk.Button(janela, text="Imprimir texto", command=imprimir_texto)
botao.grid(row=3, column=1)

janela.mainloop()


