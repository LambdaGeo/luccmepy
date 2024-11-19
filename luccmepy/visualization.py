
import salabim as sim
import matplotlib.pyplot as plt

class SimpleVisualization (sim.Component):

    def setup(self, plot_params):
        # Criar uma figura para a animação        
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 6))
        self.plot_params = plot_params
        self.plot_params["ax"] = self.ax

    def update(self, year, gdf):
        self.ax.clear()  # Limpa o gráfico antes de redesenhar
    

        gdf.plot(**self.plot_params) 
        self.ax.set_title(f'Map for {year}')  

        plt.draw()  # Desenha o gráfico na tela
        plt.pause(0.01)  # Pausa para a atualização visual


    def process (self):
        while True:
            year = self.env.now() + self.env.startTime
            print(f"[Time {year} ] SimpleVisualization")
            self.update(year, self.env.gdf) 
            self.hold(1)
            
