#Arquivo template
import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid

class Whatsapp(LateralGrid): # Herda lateral grid caso precise usar
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        #------ componentes aqui ---------#
        
        
       

    def show(self):
        #self.lateralGrid()
        self.frame.pack()
        self.master.frames_abertos.append(self.frame)
        
        
    def hide(self):
        self.frame.pack_forget()
        
