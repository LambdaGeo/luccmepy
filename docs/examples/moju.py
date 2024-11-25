
from pathlib import Path
import geopandas as gpd


from luccmepy import Component, Model, PlotMap

file_name = Path(__file__).parent / "data" / "cs_moju.zip"


env = Model(
    gdf = gpd.read_file(file_name),
    endTime = 10,
    startTime=0
)

PlotMap( 
    plot_params={ "column": "f","cmap": "coolwarm",  "ec" : 'black'}
)

env.run()