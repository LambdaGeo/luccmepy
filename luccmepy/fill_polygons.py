from rasterstats import zonal_stats
from shapely.geometry import Point
import geopandas as gpd
import numpy as np



def fill_zonal_stats(vectors, raster_data, affine, stats, prefix="attr_", nodata=-999):
    """
    Preenche atributos em `vectors` usando estatísticas zonais de um raster.
    
    Parameters:
        vectors (GeoDataFrame): GeoDataFrame com polígonos para análise.
        raster_data (numpy array): Dados do raster.
        affine (Affine): Transformação affine do raster.
        stats (list): Lista de estatísticas zonais a serem calculadas.
        prefix (str): Prefixo para os atributos adicionados.
    """
    stats_output = zonal_stats(
        vectors=vectors, 
        raster=raster_data, 
        affine=affine, 
        nodata = nodata,
        stats=stats
    )
    
    for stat in stats:
        vectors[f"{prefix}{stat}"] = [feature[stat] for feature in stats_output]

def fill_min_distance(from_gdf, to_gdf, attr_name="min_distance"):
    """
    Preenche atributos em `from_gdf` com a distância mínima até geometrias de `to_gdf`.

    Parameters:
        from_gdf (GeoDataFrame): GeoDataFrame com os polígonos a serem preenchidos.
        to_gdf (GeoDataFrame): GeoDataFrame com os pontos de referência.
        attr_name (str): Nome do atributo para armazenar as distâncias mínimas.
    """
    from_gdf[attr_name] = from_gdf.geometry.apply(
        lambda geom: to_gdf.geometry.distance(geom).min()
    )

def fill (strategy, **kwargs):
    """
    Interface principal para escolher a estratégia de preenchimento de atributos.

    Parameters:
        strategy (str): Estratégia de preenchimento ("zonal_stats" ou "min_distance").
        kwargs: Argumentos específicos para cada estratégia.
    """
    if strategy == "zonal_stats":
        fill_zonal_stats(**kwargs)
    elif strategy == "min_distance":
        fill_min_distance(**kwargs)
    else:
        raise ValueError(f"Estratégia desconhecida: {strategy}")
