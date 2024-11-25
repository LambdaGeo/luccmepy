
from luccmepy import Component


class PotentialNeighSimpleRule (Component):


    def rule (self,values):
        neighs = self.env.gdf.loc[values] 
        new_values = {}
        for lu in self.env.landUseTypes:
            new_values[lu] = neighs[lu].mean()

        return new_values

    def execute(self):
            year = self.env.now() + self.env.startTime
            print(f"[Time {year} ] PotentialDNeighSimpleRule")

            # para cada vizinhos ja calculo a media de todos os usos
            neighborhood_means = {key: self.rule(value) for key, value in self.w_.neighbors.items()}

            #atualizo no dataframe
            for lu in self.env.landUseTypes:
                self.env.gdf[lu+"_pot"] = self.env.gdf.apply (lambda r: neighborhood_means[r.name][lu], axis=1)
            

            self.hold(1)


'''
    #mais simples, porem mais demorado
    def rule (self,lu, idx):
        neighs = self.neighs(idx)
        return neighs[lu].mean()

    def execute (self):
        year = self.env.now() + self.env.startTime
        print(f"[Time {year} ] PotentialNeighSimpleRule")

        for lu in self.env.landUseTypes:
            self.env.gdf[lu+"_pot"] = self.env.gdf.index.map(lambda idx: self.rule (lu, idx) )
            
'''