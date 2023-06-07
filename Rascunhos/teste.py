import tkinter as tk

valor_textbox = ""
#textBox = None

def criaForm():
      
 # criar a janela principal
 janela = tk.Tk()
 janela.geometry("500x500")  # definir as dimensões da janela
 
 # criar o formulário
 form = tk.Frame(janela)
 

 # criar os campos de formulário
 #Criar os campos formulario: Tipo , num-cotas , preço , preço2x , preço3x , preço5x

 lbl_nome = tk.Label(form, text="Nome:")
 ent_nome = tk.Entry(form)

 lbl_idade = tk.Label(form, text="Idade:")
 ent_idade = tk.Entry(form)

 lbl_altura = tk.Label(form, text="Altura:")
 ent_altura = tk.Entry(form)

 # organizar os campos de formulário lado a lado
 lbl_nome.grid(row=0, column=0)
 ent_nome.grid(row=1, column=0)

 lbl_idade.grid(row=0, column=1)
 ent_idade.grid(row=1, column=1)

 lbl_altura.grid(row=0, column=2)
 ent_altura.grid(row=1, column=2)

 # exibir o formulário
 form.pack()

 # exibir a janela
 janela.mainloop()


def criaForm2():
 

 root = tk.Tk()
 root.geometry("500x500")

 form_frame = tk.Frame(root)
 form_frame.grid(row=0, column=0)

 name_label = tk.Label(form_frame, text="Nome:")
 name_label.grid(row=0, column=0, sticky="e")

 name_entry = tk.Entry(form_frame)
 name_entry.grid(row=0, column=1)

 age_label = tk.Label(form_frame, text="Idade:")
 age_label.grid(row=1, column=0, sticky="e")

 age_entry = tk.Entry(form_frame)
 age_entry.grid(row=1, column=1)

 height_label = tk.Label(form_frame, text="Altura:")
 height_label.grid(row=2, column=0, sticky="e")

 height_entry = tk.Entry(form_frame)
 height_entry.grid(row=2, column=1)

 root.mainloop()


def calcula():
 pass

def get_form_values(textBox):
 texto = textBox.get("1.0", "end")
 print(texto)
 
def openAnotherWindow(): 
 pass


def criaFormRifa():
      
 # criar a janela principal
 janela = tk.Tk()
 janela.title("Dino Rifas Price Simulator")
 janela.geometry("1000x500")  # definir as dimensões da janela
 
 # criar o formulário
 form = tk.Frame(janela)
 frame2 = tk.Frame(janela)

 # criar os campos de formulário
 #Criar os campos formulario: Tipo , num-cotas , preço , preço2x , preço3x , preço5x

 lbl_tipo = tk.Label(form, text="Tipo:")
 ent_tipo = tk.Entry(form)

 lbl_numCotas = tk.Label(form, text="Num-cotas:")
 ent_numCotas = tk.Entry(form)

 lbl_preco = tk.Label(form, text="Preço:")
 ent_preco = tk.Entry(form)
 
 lbl_preco2x = tk.Label(form, text="Preço2x:")
 ent_preco2x = tk.Entry(form)
 
 lbl_preco3x = tk.Label(form, text="Preço3x:")
 ent_preco3x = tk.Entry(form)
 
 lbl_preco5x = tk.Label(form, text="Preço5x:")
 ent_preco5x = tk.Entry(form)
 
 label = tk.Label(form, text="Calcule")
 label2 = tk.Label(form, text="")

 # organizar os campos de formulário lado a lado
 lbl_tipo.grid(row=0, column=0)
 ent_tipo.grid(row=1, column=0)

 lbl_numCotas.grid(row=0, column=1)
 ent_numCotas.grid(row=1, column=1)

 lbl_preco.grid(row=0, column=2)
 ent_preco.grid(row=1, column=2)
 
 lbl_preco2x.grid(row=0, column=3)
 ent_preco2x.grid(row=1, column=3)
 
 lbl_preco3x.grid(row=0, column=4)
 ent_preco3x.grid(row=1, column=4)
 
 lbl_preco5x.grid(row=0, column=5)
 ent_preco5x.grid(row=1, column=5)
 
 label.grid(row=2, column=5)
 textBox = tk.Text(frame2, width=30, height=10)
 textBox.grid(row=5, column=1) #Insere o widget Text na grade
 
 submit_button = tk.Button(form, text="Calcular", command=lambda: get_form_values(textBox) )
 submit_button.grid(row=3, column=1)
 label2.grid(row=4, column=5)
 
 mudaJanela = tk.Button(form, text="mudaJanela", command=openAnotherWindow )
 mudaJanela.grid(row=6, column=1)
 
 form.pack()  # exibir o formulário
 frame2.pack()
 janela.mainloop() # exibir a janela

 
  
#criaForm()
#criaForm2()
criaFormRifa()