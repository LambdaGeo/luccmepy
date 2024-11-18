
from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame, PotentialDNeighSimpleRule, SimpleVisualization,AllocationDSimpleOrdering

import salabim as sim


class CopyPotential(sim.Component):
    def process(self):
        while True:
            for lu in self.env.landUseTypes:
                self.env.cs[lu] = self.env.pcs[lu]
            self.hold(1)

file_name = Path(__file__).parent / "data" / "cs_moju.zip"

gdf = gpd.read_file(file_name)



gldf = GeoLuccDataFrame(gdf, id_name='object_id_')

print (gldf.head())

'''
env = sim.Environment()

env.landUseTypes = ["f", "d", "o"]
env.cs = gldf


# essa inicializacao pode ir para uma extensao para o environmente
#env.gdf_landuse = sim.Store("landuse")
#env.gdf_potential = sim.Store("potential")
env.output = sim.Store("output")


## componentes

p1 = PotentialDNeighSimpleRule()

#CopyPotential()
AllocationDSimpleOrdering()

v1 = SimpleVisualization(plot_params={
        "column": "f",
        "cmap": "coolwarm",
    })



env.run(till=100)


'''