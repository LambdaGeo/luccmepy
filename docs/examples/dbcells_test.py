




import geopandas as gpd


from luccmepy import Model, PlotMap, dw_query

sparql = '''
PREFIX : <https://landchangedata.linked.data.world/d/dbcells/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
prefix sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>

SELECT ?cell ?wkt
WHERE {
  ?cell geo:asWKT ?wkt.
   ?cell sdmx-dimension:refArea "AC".
}
'''


  



env = Model(
    gdf =  dw_query ("landchangedata/dbcells", sparql),
    endTime = 10,
    startTime=0
)

PlotMap( 
    plot_params={ "cmap": "coolwarm",  "ec" : 'black'}
)

env.run()