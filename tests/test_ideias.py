
from pathlib import Path

import geopandas as gpd

from luccmepy import GeoLuccDataFrame, PotentialDNeighSimpleRule, SimpleVisualization

import salabim as sim



import pandas as pd

# Caminho do arquivo CSV
csv_path = "caminho/para/annual_demand.csv"  # Substitua pelo caminho real

# Carregando o CSV com a coluna 'Year' como índice
df = pd.read_csv(csv_path, index_col="Year")

# Exibindo o DataFrame
print(df)