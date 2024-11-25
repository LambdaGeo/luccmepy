
from luccmepy import Component

class AllocationSimpleOrdering (Component):


    def areaAllocated (self, cellarea, column, value):
        df = self.env.gdf
        count = df[df[column] == value].shape[0]
        return count*cellarea


    def execute (self):
            year = self.env.now() + self.env.startTime
            print(f"[Time {year } ] AllocationDSimpleOrdering")
            cellarea = self.env.cellarea
            numofcells = self.env.gdf.shape[0]
            print("-------------------------------------------------------------------------------")
            print(f"Cell Area {cellarea}")
            print(f"Num of cells {numofcells}")
            demand_lu = self.env.demand.getCurrentDemand()
            current_area_lu = {}
            for lu in self.env.landUseTypes:
                current_area_lu[lu] = self.areaAllocated(cellarea,lu,1)
                print(f"Initial area for land use : {lu} -> {current_area_lu[lu]}")
                print(f"Demand area for land use : {lu} -> {demand_lu[lu]}")
            print("-------------------------------------------------------------------------------")


            # codigo ainda bem especifico, so para testar
            # mudando so floresta para desmatament
            # depois veremos a questao das direções, a media que os exemplos exigirem

            for_idx = self.env.gdf.query("f == 1").index
            demand_d = demand_lu["d"] - current_area_lu["d"]
            
            indices = self.env.gdf.loc[for_idx].sort_values (by='d_pot', ascending=False).iloc[:demand_d].index
            
            self.env.gdf.loc[indices, 'f'] = 0
            self.env.gdf.loc[indices, 'd'] = 1
            

            