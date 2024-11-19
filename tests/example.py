
from pathlib import Path

import geopandas as gpd
import pandas as pd

from luccmepy import  PotentialDNeighSimpleRule, SimpleVisualization,AllocationDSimpleOrdering, DemandPreComputedValues

import salabim as sim


env = sim.Environment()

file_name = Path(__file__).parent / "data" / "cs_moju.zip"
env.gdf = gpd.read_file(file_name)

env.landUseTypes = ["f", "d", "o"]
env.startTime = 2000
env.endTime = 2004 

env.cellarea = 1



env.potential = PotentialDNeighSimpleRule()

####################
## Demanda
####################
# pode ser carregada de um arquivo csv, ou criada manualmente

# Caminho do arquivo de demanda
csv_path = Path(__file__).parent / "data" / "moju_annual_demand.csv" 

env.demand = DemandPreComputedValues(
        annualDemand=pd.read_csv(csv_path, index_col="Year")
)

env.allocation = AllocationDSimpleOrdering()


env.visualization = SimpleVisualization(
    plot_params={
        "column": "f",
        "cmap": "coolwarm",
    })

env.run(till=env.endTime-env.startTime)


