#Arquivo template
import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid

class Planilhas(LateralGrid): # Herda lateral grid caso precise usar
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Cria uma barra de rolagem vertical
        self.scroll = tk.Scrollbar(self.frame, orient='vertical', command=self.canvas.yview)
        self.scroll.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scroll.set)

        # Criação dos Frames internos para conter o conteúdo
        self.frameInterno = tk.Frame(self.canvas)
       
        # Adiciona os frames ao canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW , height=3000)
        

        #------ componentes aqui ---------#

        self.submit_button = tk.Button(self.frameInterno , text="Selecione a(s) planilha(s)")
        self.submit_button.grid(row=1, column=1)


        #----------------- Ajuste canvas ----------------#
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        
        
       

    def show(self):
        #self.lateralGrid()
        self.frame.pack(fill=tk.BOTH , expand=True)
        self.master.frames_abertos.append(self.frame)
        
        
    def hide(self):
        self.frame.pack_forget()
        
