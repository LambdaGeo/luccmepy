
import salabim as sim


class PotentialDNeighSimpleRule (sim.Component):

    def setup(self):
        
        self.env.gdf.create_neighborhood()


    def process(self):
        while True:
            print(f"[Time {self.env.now()} ] PotentialDNeighSimpleRule")

            for lu in self.env.landUseTypes:
                self.env.gdf[lu+"_pot"] = self.env.gdf.apply (lambda r: self.env.gdf.neighs(r.name)[lu].mean(), axis=1)
            

            self.hold(1)

