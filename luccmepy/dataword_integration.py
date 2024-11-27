
import datadotworld as dw
import geopandas as gpd


from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def dw_query (dataset, query, geo_column = 'wkt', query_type='sparql'):
    results = dw.query('landchangedata/dbcells', query, query_type)
    gdf = gpd.GeoDataFrame(results.dataframe, geometry=gpd.GeoSeries.from_wkt(results.dataframe[geo_column]))
    return gdf