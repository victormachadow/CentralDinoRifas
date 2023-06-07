import sys
sys.path.append('/controller')
from controller.calculos import Calculos
from controller.calc_planilhas import CPlanilhas
from controller.scrapper_pedidos import ScrapperPedidos
from controller.scrapper_youtube import ScrapperYoutube
import tkinter as tk
from lateral_grid import LateralGrid

'''
*Irá mostrar as rifas terminadas , pelo webscrapper geral do dinorifas

* Arquivo txt Rifas Finalizadas , com as colunas separadas por virgula : nome , codigo , nome_ganhador , num_ganhador , whats_ganhador ,   a fim de registro
 -Caso tenha rifa terminada , preencher com nome , codigo 
 
-----------------------------------------------------------------x
*Botão para abrir os Pedidos para filtrar a rifa finalizada e baixar sua planilha ou procurar o numero da página mesmo.

Ou fazer um webscrapp que filte a rifa específica e pegue os dados dos pedidos gerando uma planilha

-----------------------------------------------------------------x

Gerar uma planilha individual e geral
Gerada planilha com o webscrapper dos dados dos pedidos iguais no painel - Atualizar pedidos


-Pegar numero pedidos determinado dia ( da planilha gerada ) , planilha individual -com input usuario -Opcional

-Pegar numero de pedidos feito no dia atual automaticamente  , de uma rifa especifica e geral , puxar da planilha 
scrappeada ou scrappear direto - automatico
ex: data: 10/10/2023 , pedidos: 15   e rifaNome: nome_rifa , data: 10/10/2023 , pedidos: 15

 *A data é salva em tempo real em ordem , logo quando a data for diferente da data atual ele para de 
 scrappear

 
 
    
'''

class GanhadoresPedidos(LateralGrid):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="Janela Secundária")
        self.label.pack()
        
        self.textBox = tk.Text(self.frame, width=30, height=10)
        self.textBox.pack()
        
        self.botao = tk.Button(self.frame, text="Voltar para Janela Inicial", command=lambda:self.master.show_janela_inicial())
        self.botao.pack()
        
    def show(self): 
        self.frame.pack()
        self.master.frames_abertos.append(self.frame)
        
        
    def hide(self):
        self.frame.pack_forget()
        
        
    def abre_sorteio(self):
        #abre pag sorteio    
        pass
        
    def pegaNumeros_sorteio(self):
        #webscrapp numero sorteio   
        #Ou lê planilha gerada
        pass
        
    def pegaGanhador_sorteio(self,rifa):
        #numSort = pegaNumeros_sorteio
        #le a planilha e compardo com o numero do sorteio
        pass
        
    def pegaPlanilhaRifa(self,rifa):
        pass
    
    def formatData():
     ''' Formatar a String data da janela pedidos
      string_data = "Efetuado<br> 14/03/2023 às 12:41"
      data = string_data.split("<br> ")[1].split(" às ")[0]
      print(data)  # Saída: 14/03/2023
     '''
    pass
    
    def formatPreco():
     ''' Formatar a String da coluna Total
     '''
    pass