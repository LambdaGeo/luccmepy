
from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame, PotentialDNeighSimpleRule, SimpleVisualization

import salabim as sim



class Consumer(sim.Component):
   def process(self):
      while True:
            product = self.from_store(products)
            print("--",product.value)
            self.hold(1)


class Producer(sim.Component):
   
   def setup (self):
       product = sim.Component("teste")
       product.value = 10
       self.to_store(products, product)

   def process(self):
      while True:
            
            
            self.hold(1)


env = sim.Environment(trace=False)


consumer = Consumer()
producer = Producer()

env.run(10)

#producer.status.print_histogram(values=True)
#consumer.status.print_histogram(values=True)
#products.length.print_histogram()