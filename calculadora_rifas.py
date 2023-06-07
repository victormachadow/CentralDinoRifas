import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid

'''

AQUI NÃO REGISTRA AS RIFAS REAIS, APENAS SIMULA E PLANEJA FINANCEIRAMENTE AS FUTURAS RIFAS
CRIANDO MODELOS PRONTOS E JÁ SIMULADOS PARA CONSULTAR
    
Calcular o lucro e faturamento minimo com promoções de 2x,3x,5x,10x,20x,30x,50x bilhetes
 baseando-se no numero e valores dos bilhetes em cada promoção
 
  planilha criada: tipo,num-biilhete, cotinha , preço , preço2x , preço3x ,preço5x

Calcular cotinhas menores com base nos preços , inserir valor cotinha e dividir o preço 
 -Na planilha irá apenas modificar os preços com base no numero dessas cotinhas , ex: preço/numero cotas , preço2x/numero
cotas , onde numero é o quantidade de cotinhas


'''

class CalculadoraRifas(LateralGrid):
    def __init__(self, master):
       self.master = master
 
       self.frame_conteudo = tk.Frame(self.master)
       self.canvas = tk.Canvas(self.frame_conteudo)
       self.canvas.grid(row=0, column=0, sticky='nsew')
                
      # Cria uma barra de rolagem vertical
       self.scroll = tk.Scrollbar(self.frame_conteudo, orient='vertical', command=self.canvas.yview)
       self.scroll.grid(row=0, column=1, sticky='ns')
       self.canvas.configure(yscrollcommand=self.scroll.set)

       # Criação dos Frames internos para conter o conteúdo
       self.frame = tk.Frame(self.canvas)
       
       # Adiciona os frames ao canvas
       self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW , height=3000)
       
     
      #------------- Own components -------------#

       self.lbl_tipo = tk.Label(self.frame, text="Tipo:")
       self.ent_tipo = tk.Entry(self.frame)

       self.lbl_numCotas = tk.Label(self.frame, text="Num-cotas:")
       self.ent_numCotas = tk.Entry(self.frame)

       self.lbl_preco = tk.Label(self.frame, text="Preço:")
       self.ent_preco = tk.Entry(self.frame)
 
       self.lbl_preco2x = tk.Label(self.frame, text="Preço2x:")
       self.ent_preco2x = tk.Entry(self.frame)
 
       self.lbl_preco3x = tk.Label(self.frame, text="Preço3x:")
       self.ent_preco3x = tk.Entry(self.frame)
 
       self.lbl_preco5x = tk.Label(self.frame, text="Preço5x:")
       self.ent_preco5x = tk.Entry(self.frame)
 
       self.label = tk.Label(self.frame, text="Calcule")
       self.label2 = tk.Label(self.frame, text="")

 # organizar os campos de formulário lado a lado
       #self.lbl_tipo.grid(row=0, column=0)
       #self.ent_tipo.grid(row=1, column=0)

       self.lbl_numCotas.grid(row=0, column=0)
       self.ent_numCotas.grid(row=1, column=0)

       self.lbl_preco.grid(row=0, column=1)
       self.ent_preco.grid(row=1, column=1)
 
       self.lbl_preco2x.grid(row=0, column=2)
       self.ent_preco2x.grid(row=1, column=2)
 
       self.lbl_preco3x.grid(row=0, column=3)
       self.ent_preco3x.grid(row=1, column=3)
 
       self.lbl_preco5x.grid(row=0, column=4)
       self.ent_preco5x.grid(row=1, column=4)
 
       self.label.grid(row=2, column=5)
       self.textBox = tk.Text(self.frame, width=30, height=10)
       self.textBox.grid(row=4, column=1) #Insere o widget Text na grade
       self.textBox2 = tk.Text(self.frame, width=30, height=10)
       self.textBox2.grid(row=5, column=1) #Insere o widget Text na grade
 
       self.submit_button = tk.Button(self.frame , text="Calcular", command= self.adicionar_texto)
       self.submit_button.grid(row=3, column=1)
       self.label2.grid(row=6, column=5)
       #self.frame.pack()
       self.submit_button2 = tk.Button(self.frame , text="Teste")
       self.submit_button2.grid(row=7, column=1)

       

       #------------- Scrollbar --------------#

               
       
       #teste scroll
       '''
       for i in range(50):
          
          self.label = tk.Label(self.frame, text=f"Label {i+1}")
          self.label.grid(row=i+7, column=2, sticky='ns')   
       ''' 
      #------------- Scrollbar --------------#

       self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
       self.frame_conteudo.rowconfigure(0, weight=1)
       self.frame_conteudo.columnconfigure(0, weight=1)
       
       
       calculadora = Calculos()
       #print(calculadora.printa())
       
       
       
        
    def show(self):
        #self.frame.pack(fill=tk.BOTH, expand=True) # exibir o formulário
        #self.frame2.pack(fill=tk.BOTH, expand=True) #exibi o frame2 q contem o textbox
        self.frame_conteudo.pack( fill=tk.BOTH , expand=True)
        #self.master.frames_abertos.append(self.frame)
        self.master.frames_abertos.append(self.frame_conteudo)
       
        
    def hide(self):
        self.frame.pack_forget()
        #self.frame2.pack_forget()
        

    def get_form_values(self):
        
        
        pass
        
    def adicionar_texto(self):
        texto = self.ent_tipo.get()
        if texto =="":
         print("vazio")
        self.textBox.insert(tk.END, texto + "\n")
    
        
    def save_rifas():
        #Cria e escreve no arquivo.txt
        pass
    
    def print_on_textBox():
        pass
       
       
    def calcula():
        pass
    '''    
    fatMin2x = ""
    fatMin3x = ""
    fatMin5x = ""
    '''
    
    
    
    
    