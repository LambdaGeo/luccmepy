
import salabim as sim


class AllocationDSimpleOrdering (sim.Component):

    def process (self):
        while True:
            
            print(f"[Time {self.env.now()} ] AllocationDSimpleOrdering")

            # codigo ainda bem especifico, so para testar
            for_idx = self.env.gdf.query("f == 1").index

            indices = self.env.gdf.loc[for_idx].sort_values (by='d_pot', ascending=False).iloc[:100].index
            
            self.env.gdf.loc[indices, 'f'] = 0
            self.env.gdf.loc[indices, 'd'] = 1
            
            self.hold(1)
            