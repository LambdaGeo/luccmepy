from luccmepy import fill



from pathlib import Path

import geopandas as gpd

data_path = Path(__file__).parent / "data" 

polygons_gdf = gpd.read_file(data_path / "amazonia_grid.zip")

points_gdf = gpd.read_file(data_path / "aeroportos_pnlt_poly_sirgas2000.zip")


fill (
    strategy="min_distance",
    from_gdf=polygons_gdf,
    to_gdf=points_gdf,
    attr_name="distance_to_points"
)

print (polygons_gdf.head())