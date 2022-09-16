from dbfread import DBF
from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# supress warnings
import warnings

warnings.filterwarnings("ignore")

# setting maximum number of columns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 500)
pd.set_option('display.float_format', '{:.2f}'.format)

# TODO: landuse classification: Residential, Retail, Service, Others
# path1= r'F:\IIT KGP\III Semester\Thesis\Research\Map Files\Landuse_BMC.csv'
# path1=r'F:\IIT KGP\III Semester\Thesis\Research\1.csv'
path1 = r'https://raw.githubusercontent.com/Warhead980/ThesisTrafficAnalysis/main/data/Landuse_BMC.csv'
df = pd.read_csv(path1, index_col=0)
print(df.head(10))
print(df['Landuse_AN'].unique())
df.dropna()
df['Landuse_AN'] = df['Landuse_AN'].replace(['R1', 'R2', 'R3'], 'R')
df['Landuse_AN'] = df['Landuse_AN'].replace(['C1', 'C2', 'C3', 'C4', 'C5'], 'C')
df['Landuse_AN'] = df['Landuse_AN'].replace(['PS', 'PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'PS6', 'PS7'], 'PS')
df['Landuse_AN'] = df['Landuse_AN'].replace(['M1', 'M2', 'M3'], 'M')
df['Landuse_AN'] = df['Landuse_AN'].replace(['P1', 'P2', 'P3'], 'P')
df['Landuse_AN'] = df['Landuse_AN'].replace(['PA1', 'PA2', 'PA5', 'PA6'], 'A')
df['Landuse_AN'] = df['Landuse_AN'].replace(['E1', 'E2', 'E3'], 'E')
df['Landuse_AN'] = df['Landuse_AN'].replace(['I1', 'I2', 'I3'], 'I')
df['Landuse_AN'] = df['Landuse_AN'].replace(['S5', 'S4', 'S'], 'S')

df['Landuse_AN'] = df['Landuse_AN'].replace(['T1', 'T5'], 'T')

df['Landuse_AN'] = df['Landuse_AN'].replace(['R'], 'R')
df['Landuse_AN'] = df['Landuse_AN'].replace(['C'], 'C')
df['Landuse_AN'] = df['Landuse_AN'].replace(['PS', 'M', 'P', 'E', 'S'], 'O')
df['Landuse_AN'] = df['Landuse_AN'].replace(['I', 'A'], 'S')

print(df['Landuse_AN'].unique())
# df['Landuse_AN'].plot()
#fig, ax = plt.subplots()
#df['Landuse_AN'].value_counts().plot(ax=ax, kind='bar')
#plt.show()

df['Total'] = df.groupby(['Id'])["Shape_Area"].transform('sum')
df['P'] = df['Shape_Area'] / df['Total']
df['PP'] = 100 * df.groupby(['Id', 'Landuse_AN'])["P"].transform('sum')
print(df.groupby(['Id', 'Landuse_AN']).first())

# df.reset_index()
df = df.loc[:, ['Id','Landuse_AN', 'PP']]
# df.drop(['B', 'C'], axis=1)
# df.drop

df=df.groupby(['Id', 'Landuse_AN']).first().apply(list).reset_index()
df.to_csv(r'F:\IIT KGP\III Semester\Thesis\Research\Raw Data\LU.csv')