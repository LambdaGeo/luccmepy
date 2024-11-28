from luccmepy import fill

import matplotlib.pyplot as plt

from pathlib import Path

import geopandas as gpd

from luccmepy.regular_grid import create_regular_grid

gdf = create_regular_grid (bounds=(10,10,50,50), dim= 20, attrs= {"state": 0})


glider_pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
]

toad_pattern = [
            [0, 1, 1,1],
            [1, 1, 1,0]
]


blinker_pattern = [
            [1, 1, 1]
]
  

fill(
    strategy="pattern",
    gdf=gdf,
    attr="state",
    pattern=toad_pattern,
    start_x=17,
    start_y=2
)

fill(
    strategy="pattern",
    gdf=gdf,
    attr="state",
    pattern=blinker_pattern,
    start_x=15,
    start_y=15
)

fill(
    strategy="pattern",
    gdf=gdf,
    attr="state",
    pattern=glider_pattern,
    start_x=5,
    start_y=5
)

fig, ax = plt.subplots(figsize=(10, 10))

# Plotar os polígonos coloridos pelo valor de min_distance
gdf.plot(
    column='state',  # Coluna usada para coloração
    cmap='viridis',         # Mapa de cores
    legend=False,            # Exibir legenda
    edgecolor=None,      # Cor das bordas
    ax=ax
)


plt.legend()
plt.show()