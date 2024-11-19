import salabim as sim

from pysal.lib import weights


class DemandPreComputedValues (sim.Component):

    def setup(self, annualDemand):
        self.annualDemand = annualDemand

    def process(self):
        while True:
            year = self.env.now() + self.env.startTime
            self.currentDemand = self.annualDemand.loc[year]
            self.hold(1)

    def getCurrentDemand(self):
        return self.currentDemand