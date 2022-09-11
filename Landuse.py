from dbfread import DBF
from pandas import DataFrame
import pandas as pd
import numpy as np

# setting maximum number of columns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 18)
pd.set_option('display.max_rows', 500)
pd.set_option('display.float_format', '{:.2f}'.format)

dbf = DBF('F:\IIT KGP\III Semester\Thesis\Research\Map Files/Landuse_BMC.dbf')
df = DataFrame(iter(dbf))

print(df.head(10))
print(df.columns)
print(df.groupby(['Id','Landuse_AN']).sum('Shape_Area'))