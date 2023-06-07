import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid
import webbrowser

class Dashboard(LateralGrid):
    def __init__(self, master):
        #self.master = master
        #self.frame = tk.Frame(self.master)
        #self.lateralGrid()
        #self.master.frames_abertos.append(self.frame)


       
       self.master = master
       self.lateralGrid()
       self.frame_conteudo = tk.Frame(self.master)    
       #self.master.frames_abertos.append(self.frame)
       self.canvas = tk.Canvas(self.frame_conteudo)
       self.canvas.grid(row=0, column=0, sticky='nsew')
       
                

      # Cria uma barra de rolagem vertical
       self.scroll = tk.Scrollbar(self.frame_conteudo, orient='vertical', command=self.canvas.yview)
       self.scroll.grid(row=0, column=1, sticky='ns')
       self.canvas.configure(yscrollcommand=self.scroll.set)


       # Criação dos Frames internos para conter o conteúdo
       self.frame = tk.Frame(self.canvas)
       self.textBox = tk.Text(self.frame, width=30, height=10 )
       self.textBox.grid( row=1,  column=1 , padx = 150 , pady = 20 ) #Insere o widget Text na grade
       #self.label1 = tk.Label(self.frame, text="")
       #self.label1.grid(row=2,  column=1  ,  padx = 10 , pady = 30  ) #Insere o widget Text na grade
       
      
       # Adiciona os frames ao canvas
       self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW , height=3000)
      
          
        
       '''
         #------------- Scrollbar --------------#

        # Cria um canvas para conter a grade
        self.canvas = tk.Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        # Cria uma barra de rolagem vertical
        self.scroll = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scroll.grid(row=0, column=1, sticky='ns')
        # Vincula a barra de rolagem ao canvas
        self.canvas.configure(yscrollcommand=self.scroll.set)    
        # Criação do Frame Interno para conter o conteúdo
        self.frame_conteudo = tk.Frame(self.canvas)
        self.textBox = tk.Text(self.frame, width=30, height=10)
        self.textBox.grid(row=0, column=0) #Insere o widget Text na grade
        self.canvas.create_window((0, 0), window=self.frame_conteudo, anchor=tk.NW)       
        '''
       #teste scroll
       ''' 
       for i in range(50):
          self.label = tk.Label(self.frame, text=f"Label {i+1}")
          self.label.grid(row=i+1, column=0 , sticky='ns')

       '''
       #self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
       #self.frame.rowconfigure(0, weight=1)
       #self.frame.columnconfigure(0, weight=1)
      
        
       #------------- Scrollbar --------------#
       self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
       self.frame_conteudo.rowconfigure(0, weight=1)
       self.frame_conteudo.columnconfigure(0, weight=1)
       
       self.filesLink = []
       self.filesLink = []
        #criaWidgets()

  
    def read_file(file_path):
     lines = []
     with open(file_path, 'r') as file:
        for line in file:
            # Remove os caracteres de quebra de linha
            line = line.strip()
            # Adiciona a linha ao array
            lines.append(line)
     return lines


    def open_link(event):
     #text.tag_configure("link", foreground="blue", underline=True)

     # Obtenha a posição inicial e final do link clicado
     index = self.text.tag_closest("@%s,%s" % (event.x, event.y))
     start, end = index.split(".")
    
     # Obtenha o texto do link clicado
     link_text = self.text.get(start, end)
    
     # Abra o link no navegador padrão
     webbrowser.open(link_text)       


    def criaWidgets():
     #Pega os arquivos no diretorio raiz e adiciona em um array de "links" ou de "texto"
      # for file in files: #Percorre o diretorio e verifica se é "link" ou "text" e adiciona no array filesLink ou filesText
      
     #criaWidgetsRifas()
     #criaWidgetsFerramentas()
     #criaWidgetsEstrategias()
     pass

  
    def criaWidgetRifas():
     #Cria text box de link caso o arquivo começe com "link"
     #Cria text box de texto apenas para 
     # for file in filesLinks:  #Percorre os arquivos para criar os textbox para o arquivo
      #strings_array = read_file(file_path) #Pega os textos do arquivo e guarda no array
      #cria textbox
     '''
      for file in strings_array:  #Array percorre as linhas do arquivo e cria os links
        #Torna o texto linkável
        text.insert(tk.END, link + '\n\n')
        text.tag_add("link", tk.SEL_FIRST, tk.SEL_LAST)
        text.tag_bind("link", "<Button-1>", open_link) #Abre o evento para o texto
     '''  
     pass

    def criaWidgetFerramenas():
     #Cria text box de link caso o arquivo começe com "link"
     #Cria text box de texto apenas para 
     # for file in filesLinks:  #Percorre os arquivos para criar os textbox para o arquivo
     #strings_array = read_file(file_path) #Pega os textos do arquivo e guarda no array
     #cria textbox
      
     '''
     for file in strings_array:
        #Torna o texto linkável
        text.insert(tk.END, link + '\n\n')
        text.tag_add("link", tk.SEL_FIRST, tk.SEL_LAST)
        #text.tag_configure("link", foreground="blue", underline=True)
        text.tag_bind("link", "<Button-1>", lambda x: ( 
        
          #text.tag_configure("link", foreground="blue", underline=True)
          #Obtenha a posição inicial e final do link clicado
          index = self.text.tag_closest("@%s,%s" % (event.x, event.y))
          start, end = index.split(".")
          # Obtenha o texto do link clicado
          link_text = self.text.get(start, end)
          # Abra o link no navegador padrão
          webbrowser.open(link_text)


        )) #Abre o evento para o texto
     '''  
     pass

    def criaWidgetEstrategias():
     #Cria text box de texto para estrategias.txt
      
     
     pass


    
    def show(self):
        #self.lateralGrid()
        #self.frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame_conteudo.pack( fill=tk.BOTH , expand=True)
        self.master.frames_abertos.append(self.frame_conteudo)
        
        #self.master.frames_abertos.append(self.frame_conteudo)
        #self.master.frames_abertos.append(self.scroll)
        
        
    def hide(self):
        self.frame.pack_forget()
        