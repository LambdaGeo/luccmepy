
from luccmepy import Component, Model, PlotMap, create_regular_grid

from luccmepy.models.toys import FireModelProb

from matplotlib.colors import ListedColormap
custom_cmap = ListedColormap(['green', 'red', 'brown'])


FOREST = 0
BURNING = 1
BURNED = 2

env = Model(
    gdf = create_regular_grid (bounds=(10,10,50,50), dim= 20, attrs= {"state": FOREST}),
    endTime = 10
)

env.gdf.loc["10-10","state"] = BURNING


PlotMap( hold= 3,name="Plotando",
    plot_params={ "column": "state","cmap": custom_cmap,  "ec" : 'black'}
)


FireModelProb(create_neighbohood="Rook", name="FireModel")

env.run(10)