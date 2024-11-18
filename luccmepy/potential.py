
import salabim as sim


class PotentialDNeighSimpleRule (sim.Component):

    def setup(self):
        

        # talvez em outro lugar
        potential = sim.Component("potential")
        
        pcs = self.env.cs[["geometry"]].copy()
        potential.gdf = pcs

        self.to_store (self.env.output, potential)

        self.env.cs.create_neighborhood()


    def process(self):
        while True:
            print(f"[Tempo {self.env.now()} ] Calculo de Potencial")
            potential = self.from_store(self.env.output)

            for lu in self.env.landUseTypes:
                serie = self.env.cs.apply (lambda row: self.env.cs.neighs(row.name)[lu].mean(), axis=1)
                potential.gdf[lu] = serie
            

            self.to_store (self.env.output, potential) 

            self.hold(1)

