from geopandas import GeoDataFrame

from luccmepy import create_regular_grid


def test_regular_grid():
    gdf = create_regular_grid (bounds=(10,10,50,50), dim= 10, attrs= {"state": 0})

    rows, _ = gdf.shape

    assert isinstance(gdf, GeoDataFrame) and rows == 100