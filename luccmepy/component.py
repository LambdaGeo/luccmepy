

import salabim as sim
from pysal.lib import weights

class Component (sim.Component):

    strategies = {
        "Queen" : weights.contiguity.Queen,
        "Rook" : weights.contiguity.Rook
    }

    def __init__(self, hold = 1, name="", create_neighbohood = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.create_neighbohood = create_neighbohood
        self._hold = hold
        if self.create_neighbohood:
            self.w_ = Component.strategies[self.create_neighbohood].from_dataframe(self.env.gdf, use_index=True)                   

    def neighs(self, idx):
        """
        Retorna os índices dos vizinhos da célula fornecida.
        """
        if self.create_neighbohood:
            ns = self.w_.neighbors[idx]
            #return ns
            return self.env.gdf.loc[ns]
        else:
            return {}
        
    def process(self):
            while True: 
                self.execute() 
                self.hold(self._hold)

    '''
    def __init__(self, hold = 1, name="", create_neighbohood = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.create_neighbohood = create_neighbohood
        self._hold = hold
        
        if self.create_neighbohood:
            self.w_ = Component.strategies[self.create_neighbohood].from_dataframe(self.env.gdf, use_index=True)                   
            self.update_neighborhood()

    def update_neighborhood(self):
         print ("updating neighs")
         self.neighborhood = {}
         for idx, cell in self.env.gdf.iterrows():
            ns = self.w_.neighbors[idx]
            self.neighborhood[idx] = self.env.gdf.loc[ns]

    def neighs(self, idx):
        """
        Retorna os índices dos vizinhos da célula fornecida.
        """
        if self.create_neighbohood:
            return self.neighborhood[idx]
        else:
            return None

    '''