import tkinter as tk
from calculadora_rifas import CalculadoraRifas
from dashboard import Dashboard
from youtube_parcerias import YoutubeParcerias
from lateral_grid import LateralGrid
from ganhadores_pedidos import GanhadoresPedidos
from planilhas import Planilhas
from whatsapp import Whatsapp


class Application(tk.Tk):

    frames_abertos = []

    def on_window_resize(event,self):
      # Obtém a nova altura da janela
      nova_altura = event.height

      # Atualiza a altura da linha vertical
      self.grid_rowconfigure(0, minsize=nova_altura)
    
    def __init__(self):
        super().__init__()
        self.title("Central Dino Rifas")
        self.geometry("800x500")
        
        #Inicializa classe lateral grid
        self.lateral_grid = LateralGrid(self)
        # Cria as janelas
        self.calculadora_rifas = CalculadoraRifas(self)
        self.dashboard = Dashboard(self)
        self.planilhas = Planilhas(self)
        self.youtube_parcerias = YoutubeParcerias(self)
        self.ganhadores_pedidos = GanhadoresPedidos(self)
        
        
        # Configura a janela inicial para ser a primeira a aparecer
        #self.calculadora_rifas.show()
        self.dashboard.show()

    def hide_all(self):
        # Percorre a lista de frames abertos e fecha cada um deles, exceto a janela principal
        for frame in self.frames_abertos[1:]:
            #frame.destroy()
            frame.pack_forget() 

    def fechar_outros_frames(self):
        # Percorre a lista de frames abertos e fecha cada um deles, exceto a janela principal
        for frame in self.frames_abertos[0:]:
            #frame.destroy()
            frame.pack_forget()    
        
    def show_calculadoraRifas(self):
       
        self.fechar_outros_frames()
        #self.frames_abertos = [self]
        self.calculadora_rifas.show()
        
    def show_dashboard(self):
       
        self.fechar_outros_frames()
        #self.frames_abertos = [self]
        self.dashboard.show()
    
    def show_ganhadores_pedidos(self):
        self.fechar_outros_frames()
        #self.frames_abertos = [self]
        self.ganhadores_pedidos.show()
        
    def show_youtube_parcerias(self):
        self.fechar_outros_frames()
        #self.frames_abertos = [self]
        self.youtube_parcerias.show()
    
    def show_planilhas(self):

        self.fechar_outros_frames()
        self.planilhas.show()

    '''
    def show_whatsapp():
        self.planilhas.show()
    '''

        
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()        