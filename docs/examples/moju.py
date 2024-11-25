
from pathlib import Path
import geopandas as gpd
import pandas as pd

from luccmepy.components.topdown.potential import PotentialNeighSimpleRule
from luccmepy.components.topdown.demand import DemandPreComputedValues
from luccmepy.components.topdown.allocation import AllocationSimpleOrdering

from luccmepy import Component, Model, PlotMap



file_name = Path(__file__).parent / "data" / "cs_moju.zip"


env = Model(
    gdf = gpd.read_file(file_name),
    startTime=2000,
    endTime = 2004
)

env.landUseTypes = ["f", "d", "o"]
env.cellarea = 1

env.potential = PotentialNeighSimpleRule(create_neighbohood="Queen")

# Caminho do arquivo de demanda
csv_path = Path(__file__).parent / "data" / "moju_annual_demand.csv" 

env.demand = DemandPreComputedValues(
        annualDemand=pd.read_csv(csv_path, index_col="Year")
)

env.allocation = AllocationSimpleOrdering()

PlotMap( 
    plot_params={ "column": "f","cmap": "coolwarm"}
)

env.run()
#print (env.gdf.head())