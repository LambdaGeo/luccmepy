

from geopandas import GeoDataFrame
from pysal.lib import weights


class GeoLuccDataFrame (GeoDataFrame):

    def __init__(self, data=None, *args,  geometry=None, crs=None , **kwargs):
        if (
            kwargs.get("copy") is None
            and isinstance(data, GeoDataFrame)
            and not isinstance(data, GeoLuccDataFrame)
        ):
            kwargs.update(copy=True)
        
        super().__init__(data, *args, **kwargs)

        self.neighbors_ = None
    

    
    def create_neighborhood(self):
        self.neighbors_ = weights.contiguity.Queen.from_dataframe(self, use_index=True).neighbors

    def neighs (self, pos):
        ns = self.neighbors_[pos]  
        if ns:  
               return self.loc[ns]
        raise ("no neighs")
