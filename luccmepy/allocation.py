
import salabim as sim


class AllocationDSimpleOrdering (sim.Component):

    def process (self):
        while True:
            ano = self.env.now()
            print(f"[Tempo {self.env.now()} ] Alocação")

            for_idx = self.env.cs.query("f == 1").index

            potential = self.from_store(self.env.output)

            indices = potential.gdf.loc[for_idx].sort_values (by='d', ascending=False).iloc[:100].index
            
            self.env.cs.loc[indices, 'f'] = 0
            self.env.cs.loc[indices, 'd'] = 1
            

            self.hold(1)
            self.to_store (self.env.output, potential) 