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

#dbf = DBF('F:\IIT KGP\III Semester\Thesis\Research\Map Files/Landuse_BMC.dbf')
#df = DataFrame(iter(dbf))
df=pd.read_csv(r'F:\IIT KGP\III Semester\Thesis\Research\1.csv')

# TODO: landuse classification: Residential, Retail, Service, Others

print(df.head(10))
print(df.dtypes)
#df['%']=100*df['Shape_Area']/df.groupby('Landuse_AN')['Shape_Area'].transform('sum')

df["Total"] = df.groupby(['Id','Landuse_AN'])["Shape_Area"].transform('sum')

#df["TTotal"] =df.groupby(['Id','Landuse_AN'], as_index=False)["Total"].sum()
#df["Percent"] = 100*df["Shape_Area"] / df["Total"]

#dfm=df.groupby(['Id','Landuse_AN']).first()
#dfm.to_frame()
#df.reset_index(inplace=True)
df['TTotal']=df.groupby(['Id','Landuse_AN']).transform('sum')
#print(df)
print(df)
#print(df)
#print(df)