#Arquivo template view
import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube

import tkinter as tk
from lateral_grid import LateralGrid

class Nome_Classe(LateralGrid): # Herda lateral grid caso precise usar
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        #------ componentes aqui ---------#

        #------------- Scrollbar --------------#

        #Montar os frames desta forma:
        '''
        self.frame_conteudo = tk.Frame(self.master) #frame principal dentro do frame pai da aplicação
        self.canvas = tk.Canvas(self.frame_conteudo) #Cria canvas dentro do frame principal
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.scroll = tk.Scrollbar(self.frame_conteudo, orient='vertical', command=self.canvas.yview) #scrollbar
        self.scroll.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.frame = tk.Frame(self.canvas) #Frame interno para por os componentes dentro do canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW , height=3000) #Adiciona frame interno ao canvas

                                    #Ajusta o canvas e o frame de principal ao scroll

        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame_conteudo.rowconfigure(0, weight=1)
        self.frame_conteudo.columnconfigure(0, weight=1)

        self.frame_conteudo.pack( fill=tk.BOTH , expand=True) #Em show() frame principal que da display

        #Usar grid para posicionar os elementos no frame interno , na vertical
        
        
        '''

        # Cria um canvas para conter a grade
        self.canvas = tk.Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky='nsew')
       
        
        # Cria uma barra de rolagem vertical
        self.scroll = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scroll.grid(row=0, column=1, sticky='ns')
        # Vincula a barra de rolagem ao canvas
        #self.scroll.config(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        
        # Criação do Frame Interno para conter o conteúdo
        self.frame_conteudo = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_conteudo, anchor=tk.NW)       
        
        #teste scroll
        '''
        for i in range(50):
          
          self.label = tk.Label(self.frame_conteudo, text=f"Label {i+1}")
          self.label.grid(row=i+1, column=2, sticky='ns')

        '''
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        #------------- Scrollbar --------------#
        
        
       

    def show(self):
        #self.lateralGrid()
        self.frame.pack()
        self.master.frames_abertos.append(self.frame)
        
        
    def hide(self):
        self.frame.pack_forget()
        
