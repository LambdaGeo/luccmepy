
from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame, PotentialDNeighSimpleRule

import salabim as sim

def test_potential():
    """
    Testa a criação de uma instância de GeoLuccDataFrame.
    """
    file_name = Path(__file__).parent / "data" / "cs_moju.zip"

    gdf = gpd.read_file(file_name)

    gldf = GeoLuccDataFrame(gdf, id_name='object_id_')  
    
    rows, _ = gldf.shape

    env = sim.Environment()

    env.landUseTypes = ["f", "d", "o"]
    env.cs = gldf
    

    p1 = PotentialDNeighSimpleRule()

    env.run(till=3)

    assert False


