
from luccmepy import Component

class DemandPreComputedValues (Component):

    def setup(self, annualDemand):
        self.annualDemand = annualDemand

    def execute(self):
        year = self.env.now() 
        self.currentDemand = self.annualDemand.loc[year]

    def getCurrentDemand(self):
        return self.currentDemand