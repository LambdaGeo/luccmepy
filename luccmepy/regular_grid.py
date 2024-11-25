

import geopandas as gpd
import numpy as np
from shapely.geometry import box

def create_regular_grid(gdf=None, bounds=None, dim=10, attrs={}, crs="EPSG:29902"):
    """
    Create a square grid that covers a GeoDataFrame area
    or a fixed boundary with x-y coordinates.
    
    Parameters:
        gdf (GeoDataFrame): Optional GeoDataFrame to cover with the grid.
        bounds (tuple): Optional tuple (xmin, ymin, xmax, ymax) defining the grid area.
        n_cells (int): Number of cells along one dimension (e.g., rows or columns).
        attrs (dict): Additional attributes to include in the grid GeoDataFrame.
        crs (str): Coordinate reference system for the output grid.
    
    Returns:
        GeoDataFrame: GeoDataFrame of grid polygons with attributes.
    """


    # Obter limites do GeoDataFrame ou usar limites fornecidos
    if bounds is not None:
        xmin, ymin, xmax, ymax = bounds
    else:
        xmin, ymin, xmax, ymax = gdf.total_bounds

    # Certificar que o grid cobre todo o espaço
    x_edges = np.linspace(xmin, xmax, dim + 1)
    y_edges = np.linspace(ymin, ymax, dim + 1)

    # Criar células do grid
    grid_cells = []
    ids = []
    for i in range(len(x_edges) - 1):
        for j in range(len(y_edges) - 1):
            x0, x1 = x_edges[i], x_edges[i + 1]
            y0, y1 = y_edges[j], y_edges[j + 1]
            poly = box(x0, y0, x1, y1)  # Criar um polígono representando a célula
            grid_cells.append(poly)
            ids.append(f"{j}-{i}")

    # Criar GeoDataFrame com células
    data = {"geometry": grid_cells, "id": ids}
    for key, value in attrs.items():
        data[key] = [value] * len(grid_cells)

    grid_gdf = gpd.GeoDataFrame(data, crs=crs)
    grid_gdf.set_index(["id"], inplace=True)

    return grid_gdf