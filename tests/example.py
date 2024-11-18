
from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame, PotentialDNeighSimpleRule, SimpleVisualization,AllocationDSimpleOrdering

import salabim as sim



file_name = Path(__file__).parent / "data" / "cs_moju.zip"

gdf = gpd.read_file(file_name)

gldf = GeoLuccDataFrame(gdf)



env = sim.Environment()

env.landUseTypes = ["f", "d", "o"]
env.gdf = gldf

SimpleVisualization(plot_params={
        "column": "f",
        "cmap": "coolwarm",
    })

PotentialDNeighSimpleRule()

AllocationDSimpleOrdering()





env.run(till=12)


