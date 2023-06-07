import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid

class YoutubeParcerias(LateralGrid):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        referencia = self
        referencia.text = "referencia: calculadora-rifas"
        
        '''
        self.label = tk.Label(self.frame, text="Janela Secundária")
        self.label.pack()
        
        self.textBox = tk.Text(self.frame, width=30, height=10)
        self.textBox.pack()
        
        self.botao = tk.Button(self.frame, text="Voltar para Janela Inicial", command=self.master.show_janela_inicial)
        self.botao.pack()
        '''
        
    def show(self):
        self.frame.pack()
        self.master.frames_abertos.append(self.frame)
        
    def hide(self):
        self.frame.pack_forget()
        
  #----------------------- escopo funcoes -----
        