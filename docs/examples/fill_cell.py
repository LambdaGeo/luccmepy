from luccmepy import fill

import matplotlib.pyplot as plt

from pathlib import Path

import geopandas as gpd
import rasterio

data_path = Path(__file__).parent / "data" 

polygons_gdf = gpd.read_file(data_path / "amazonia_grid.zip")


raster_path = "zip://" + str (data_path / "amazoniaveg.zip")
print (raster_path)
with rasterio.open(raster_path) as src:
    raster_data = src.read(1)  # Carrega a primeira banda do raster
    affine = src.transform    # Transforma affine associada ao raster
    nodata = src.nodata


fill(
    strategy="zonal_stats",
    vectors=polygons_gdf,
    raster_data=raster_data,
    nodata=nodata,
    affine=affine,
    stats=["mean", "max", "min"],
    prefix="zonal_"
)



fig, ax = plt.subplots(figsize=(10, 10))

# Plotar os polígonos coloridos pelo valor de min_distance
polygons_gdf.plot(
    column='zonal_mean',  # Coluna usada para coloração
    cmap='viridis',         # Mapa de cores
    legend=True,            # Exibir legenda
    edgecolor=None,      # Cor das bordas
    vmax=1,
    vmin= 0,
    ax=ax
)



# Título e legenda
plt.legend()
plt.show()