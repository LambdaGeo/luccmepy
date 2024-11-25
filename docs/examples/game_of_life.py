
from luccmepy import Component, Model, PlotMap, create_regular_grid, fill_regular_grid

from luccmepy.models.toys import GameOfLife

from matplotlib.colors import ListedColormap

custom_cmap = ListedColormap(['green', 'red'])
plot_params={ "column": "state","cmap": custom_cmap,  "ec" : 'black'}

env = Model(
    gdf = create_regular_grid (bounds=(10,10,50,50), dim= 20, attrs= {"state": 0}),
    endTime = 10,
    startTime=0
)

glider_pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
]
        

fill_regular_grid (env.gdf, "state", glider_pattern, 5,5)

GameOfLife(create_neighbohood="Queen")

PlotMap( 
    plot_params={ "column": "state","cmap": custom_cmap,  "ec" : 'black'}
)

env.run()

