

from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame

def test_instanciacao_geolucc_dataframe():
    """
    Testa a criação de uma instância de GeoLuccDataFrame.
    """
    file_name = Path(__file__).parent / "data" / "csAC.zip"
    print (file_name)

    gdf = gpd.read_file(file_name)

    gldf = GeoLuccDataFrame(gdf, id_name='object_id0')  
    print (type(gldf))
    rows, _ = gldf.shape

    assert isinstance(gldf, GeoLuccDataFrame) and rows > 0