from luccmepy import fill

import matplotlib.pyplot as plt

from pathlib import Path

import geopandas as gpd

data_path = Path(__file__).parent / "data" 

polygons_gdf = gpd.read_file(data_path / "amazonia_grid.zip")

points_gdf = gpd.read_file(data_path / "aeroportos_pnlt_poly_sirgas2000.zip")

# Certifique-se de que ambos os GeoDataFrames estão no mesmo CRS
polygons_gdf = polygons_gdf.to_crs(points_gdf.crs)

fill (
    strategy="min_distance",
    from_gdf=polygons_gdf,
    to_gdf=points_gdf,
    attr_name="min_distance"
)

print (polygons_gdf.head())

fig, ax = plt.subplots(figsize=(10, 10))

# Plotar os polígonos coloridos pelo valor de min_distance
polygons_gdf.plot(
    column='min_distance',  # Coluna usada para coloração
    cmap='viridis',         # Mapa de cores
    legend=True,            # Exibir legenda
    edgecolor=None,      # Cor das bordas
    ax=ax
)
points_gdf.plot(ax=ax, color='red', markersize=10, label='Pontos')  # Pontos


# Título e legenda
plt.title("Polígonos coloridos pela menor distância aos pontos")
plt.legend()
plt.show()