
import salabim as sim

from pysal.lib import weights


class PotentialDNeighSimpleRule (sim.Component):


    def setup(self):
        # create neighborhood
        self.w_ = weights.contiguity.Queen.from_dataframe(self.env.gdf, use_index=True)


    def neighs (self, idx):
        ns = self.w_.neighbors[idx] 
        return self.env.gdf.loc[ns] 

    def process(self):
        while True:
            print(f"[Time {self.env.now()} ] PotentialDNeighSimpleRule")

            for lu in self.env.landUseTypes:
                self.env.gdf[lu+"_pot"] = self.env.gdf.apply (lambda r: self.neighs(r.name)[lu].mean(), axis=1)
            

            self.hold(1)

