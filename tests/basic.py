from geopandas import GeoDataFrame

from luccmepy import create_regular_grid, Model, Component


def test_regular_grid():
    gdf = create_regular_grid (bounds=(10,10,50,50), dim= 2, attrs= {"state": 0})

    rows, _ = gdf.shape

    assert isinstance(gdf, GeoDataFrame) and rows == 4


def test_component_model():

    class Test(Component):
        def execute(self):
            env.init = env.init + 1


    env = Model(
        endTime = 10
    )

    env.init = 0

    t = Test()

    env.run()
    assert env.init == 11

