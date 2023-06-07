import tkinter as tk

class LateralGrid:
  
    def __init__(self, master):
        self.master = master #Pega referência da classe Application

    def lateralGrid(self):
       frame_grid = tk.Frame(self.master)
       frame_grid.columnconfigure(0, minsize=100, weight=1)
       
       #print(self.text)

        # Cria uma barra de rolagem vertical
       scrollbar = tk.Scrollbar( frame_grid , orient='vertical')
       scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Cria um canvas para conter a grade
       canvas = tk.Canvas( frame_grid , width=200 )
       canvas.pack(side=tk.LEFT, fill=tk.Y)
       # Vincula a barra de rolagem ao canvas
       canvas.configure(yscrollcommand=scrollbar.set)
       scrollbar.config(command=canvas.yview)
       
       
        # Cria um frame para conter os botões
       frame_buttons = tk.Frame(canvas)
       canvas.create_window((0, 0), window=frame_buttons, anchor=tk.NW)

       rifas_button = tk.Button(frame_buttons , text="Rifas",command=lambda:self.master.show_ganhadores_pedidos())
       rifas_button.pack(pady=5)

       mensagens_button = tk.Button(frame_buttons , text="Mensagens",command=lambda:self.master.show_ganhadores_pedidos())
       mensagens_button.pack(pady=5)

       calculadora_button = tk.Button(frame_buttons , text="Calculadora_promos",command=lambda:self.master.show_calculadoraRifas())
       calculadora_button.pack(pady=5)

       dash_button = tk.Button(frame_buttons , text="Dashboard",command=lambda:self.master.show_dashboard())
       dash_button.pack(pady=5)

       youtube_button = tk.Button(frame_buttons , text="Youtube parcerias",command=lambda:self.master.show_youtube_parcerias())
       youtube_button.pack(pady=5)

       pedidos_button = tk.Button(frame_buttons , text="Ganhadores&Pedidos",command=lambda:self.master.show_ganhadores_pedidos())
       pedidos_button.pack(pady=5)

       planilhas_button = tk.Button(frame_buttons , text="Planilhas",command=lambda:self.master.show_planilhas())
       planilhas_button.pack(pady=5)

       whatsapp_button = tk.Button(frame_buttons , text="Whatsapp",command=lambda:self.master.show_ganhadores_pedidos())
       whatsapp_button.pack(pady=5)

       

       for i in range(50):
          
         label = tk.Label(frame_buttons, text=f"Label {i+1}")
         label.pack(pady=5)

          
       canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
       frame_grid.rowconfigure(0, weight=1)
       frame_grid.columnconfigure(0, weight=1)
       frame_grid.pack(side=tk.LEFT, fill=tk.Y)
       
         

        #-----------------------x---------------------------------#
       #Desenho da linha vertical usando o widget tk.Canvas

       #frame_canvas = tk.Frame(frame_grid)
       #frame_canvas.pack(fill='both', expand=True)
       canvas2 = tk.Canvas( frame_grid , width=1, height=1500, background='black')
       #canvas2.grid(row=0, column=1, padx=0, sticky='ns')
       canvas2.pack(side=tk.LEFT, padx=0)
       #self.master.bind('<Configure>', self.master.on_window_resize )

       #----------------------x--------------------------------#

       

       

       
        