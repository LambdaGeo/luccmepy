
from pathlib import Path

import geopandas as gpd

from luccmepy import  PotentialDNeighSimpleRule, SimpleVisualization,AllocationDSimpleOrdering

import salabim as sim


env = sim.Environment()

file_name = Path(__file__).parent / "data" / "cs_moju.zip"
env.gdf = gpd.read_file(file_name)

env.landUseTypes = ["f", "d", "o"]

SimpleVisualization(plot_params={
        "column": "f",
        "cmap": "coolwarm",
    })

PotentialDNeighSimpleRule()

AllocationDSimpleOrdering()

env.run(till=12)


