
import matplotlib.pyplot as plt
import time
from IPython.display import clear_output


from luccmepy import Component

class IPlotMap (Component):

    def setup(self, plot_params):
        # Criar uma figura para a animação        
        self.plot_params = plot_params


    def update(self, year, gdf):
        
        clear_output(wait=True)  # Limpa a saída do notebook para exibir apenas o gráfico atualizado
        ax = gdf.plot(**self.plot_params) 
        ax.set_title(f'Map for {year}')  

        plt.draw()  # Desenha o gráfico na tela
        plt.pause(0.01)  # Pausa para a atualização visual
    


    def execute (self):
        year = self.env.now() 
        self.update(year, self.env.gdf) 
   

class PlotMap (Component):

    def setup(self, plot_params):
        # Criar uma figura para a animação        
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 6))
        self.plot_params = plot_params
        

    def update(self, year, gdf):
        self.ax.clear()  # Limpa o gráfico antes de redesenhar
    

        gdf.plot(ax=self.ax, **self.plot_params) 
        self.ax.set_title(f'Map for {year}')  

        plt.draw()  # Desenha o gráfico na tela
        plt.pause(0.01)  # Pausa para a atualização visual
        


    def process (self):
        while True:
            year = self.env.now() + self.env.startTime
            print(f"[Time {year} ] SimpleVisualization")
            self.update(year, self.env.gdf) 
            self.hold(1)