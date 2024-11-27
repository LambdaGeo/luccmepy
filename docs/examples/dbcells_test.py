




import geopandas as gpd


from luccmepy import Model, PlotMap, dw_query

sparql_ = '''
PREFIX : <https://landchangedata.linked.data.world/d/dbcells/>
prefix geo: <http://www.opengis.net/ont/geosparql#>
prefix sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>

SELECT ?cell ?wkt
WHERE {
  ?cell geo:asWKT ?wkt.
  ?cell sdmx-dimension:refArea "AC".
}
'''


sparql = '''

prefix dbc-measure: <http://www.purl.org/linked-data/dbcells/measure#>
prefix qb: <http://purl.org/linked-data/cube#>
prefix dbc-code: <http://www.purl.org/linked-data/dbcells/code#>
prefix dbc-attribute: <http://www.purl.org/linked-data/dbcells/attribute#>
prefix sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
prefix ds: <https://purl.org/dbcells/dataset#> 

SELECT ?id ?dist_river ?wkt 
where {
    ?cell geo:asWKT ?wkt;
        sdmx-dimension:refArea "AC".

    ?id a qb:Observation;
        qb:dataSet ds:7bbec547-e601-40a4-9991-1b25d05d4af4;
        sdmx-dimension:refArea ?cell;
        dbc-measure:distance ?dist_river.

}
'''





env = Model(
    gdf =  dw_query ("lambdageo/luccmebrdrivers", sparql),
    endTime = 10,
    startTime=0
)

print (env.gdf.head())

PlotMap( 
    plot_params={ "column":"dist_river","cmap": "coolwarm",  "ec" : 'black'}
)

env.run()