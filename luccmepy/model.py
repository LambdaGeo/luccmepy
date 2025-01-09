
import salabim as sim

class Model(sim.Environment):
    def __init__(self, gdf = None, startTime=0, endTime=0, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.startTime = startTime
        self.endTime = endTime
        self.gdf = gdf        


    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs) 
        #print("Configur do ambiente personalizada foi realizada!")


    def run (self, endTime=None):
        print (f"running from {self.startTime} to {self.endTime}")
        if endTime:
            super().run(till=endTime-self.startTime)    
        else:
            super().run(till=self.endTime-self.startTime)


    def now (self):
        return super().now() + self.startTime