
import salabim as sim

from pysal.lib import weights


class PotentialDNeighSimpleRule (sim.Component):


    def setup(self):
        # create neighborhood
        self.w_ = weights.contiguity.Queen.from_dataframe(self.env.gdf, use_index=True)


    def neighs (self, idx):
        ns = self.w_.neighbors[idx] 
        return self.env.gdf.loc[ns] 

    def rule (self,values):
        neighs = self.env.gdf.loc[values] 
        new_values = {}
        for lu in self.env.landUseTypes:
            new_values[lu] = neighs[lu].mean()

        return new_values

    def process(self):
        while True:
            year = self.env.now() + self.env.startTime
            print(f"[Time {year} ] PotentialDNeighSimpleRule")

            neighborhood_means = {key: self.rule(value) for key, value in self.w_.neighbors.items()}
            for lu in self.env.landUseTypes:
                self.env.gdf[lu+"_pot"] = self.env.gdf.apply (lambda r: neighborhood_means[r.name][lu], axis=1)
            

            self.hold(1)

