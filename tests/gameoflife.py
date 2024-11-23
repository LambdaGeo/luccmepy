import pandas as pd
import geopandas as gpd
import shapely.geometry
import matplotlib.pyplot as plt

import shapely
import numpy as np
import time


import salabim as sim


class SleepTime (sim.Component):

    def setup (self, seconds):
        self.seconds = seconds

    def process (self):
        while True:
            time.sleep(self.seconds)
            self.hold(1)

def create_grid(gdf=None, bounds=None, n_cells=10, crs="EPSG:29902"):
    """Create square grid that covers a geodataframe area
    or a fixed boundary with x-y coords
    returns: a GeoDataFrame of grid polygons
    see https://james-brennan.github.io/posts/fast_gridding_geopandas/
    """

    if bounds != None:
        xmin, ymin, xmax, ymax= bounds
    else:
        xmin, ymin, xmax, ymax= gdf.total_bounds

    attrs = {"state": 0}
    # get cell size
    cell_size = (xmax-xmin)/(n_cells-1)
    # create the cells in a loop
    grid_cells = []
    ids = []
    ln = 0
    cl = 0
    for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
        cl = 0
        for y0 in np.arange(ymin, ymax+cell_size, cell_size):
            x1 = x0-cell_size
            y1 = y0+cell_size
            poly = shapely.geometry.box(x0, y0, x1, y1)
            #print (gdf.overlay(poly, how='intersection'))
            grid_cells.append( poly )
            print (x0, y0, x1, y1)
            print (ln, cl)
            ids.append(f"{cl}-{ln}")
            cl = cl + 1
        ln = ln + 1


    data = {
            "geometry": grid_cells,
             "id":ids
            }
    for key, value in attrs.items():
        data[key] = [value] * len(grid_cells)

    cells = gpd.GeoDataFrame(data,crs=crs)

    cells.set_index(['id'], inplace=True)

    return cells

def insert_glider(gdf, start_x, start_y):
    glider_pattern = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    w = 3
    for i in range(w):
        for j in range(w):
            idx = f"{start_x + i}-{start_y + j}"
            # 2-i para inverter e pegar a partir da linha superior
            gdf.loc[idx, 'state'] = glider_pattern[2-i][j]


gr = create_grid(bounds=(0,0,10,10), n_cells=10)
print (gr.head())

#gr.loc["2-1", "state"] = 1
insert_glider(gr, 5,5)

gr.plot(column="state", ec='black')
plt.show()

'''


from luccmepy import  SimpleVisualization

import salabim as sim


env = sim.Environment()

env.startTime = 2000
env.endTime = 2004 

env.gdf = gr

env.visualization = SimpleVisualization(
    plot_params={
        "column": "state",
        "cmap": "coolwarm",
        "ec" : 'black'
    })

SleepTime(seconds=2)

env.run(till=env.endTime-env.startTime)
'''