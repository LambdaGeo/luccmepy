

from geopandas import GeoDataFrame
from pysal.lib import weights


class GeoLuccDataFrame (GeoDataFrame):

    def __init__(self, data=None, *args, id_name, geometry=None, crs=None , **kwargs):
        if (
            kwargs.get("copy") is None
            and isinstance(data, GeoDataFrame)
            and not isinstance(data, GeoLuccDataFrame)
        ):
            kwargs.update(copy=True)
        
        super().__init__(data, *args, **kwargs)
        self.set_index(id_name, inplace=True)
        self.neighs_ = None

    # problema com relacao ao retorno da vizinhanca

    # custo alto de memoria
    def create_neighborhood(self):
        self.neighbors = weights.contiguity.Queen.from_dataframe(self, use_index=True).neighbors
        #values = map(lambda idx: self.loc[idx], neighbors.values())
        #self.neighs_ = dict(zip(neighbors.keys(), values))

    def neighs (self, idx):
        return self.loc[self.neighbors[idx]]
        #return self.neighs_[idx]