# importing builtin classes
import numpy as np

# importing custom classes
from ImportData import *
from ColumnFiltering import *
from ColRename import *
from FillData import *
from CheckUnique import *
from ToNumeric import *
from ColSet import *
from CorelationMatrix import *
from LinearRegressionModel import *
from ipfn import *

# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# setting maximum number of columns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 18)


df = ImportData()
df=ipfn
df = ColFilter(df)
df = ColRename(df)
df = FillData(df)
df = ToNumeric(df)
df=ColSet(df)

CheckUnique(df, 'work_days')
#df=df.sort_values('ID')
print(list(df.columns.values))
print(df.dtypes)
z=(df['total_days'] == 0).sum()
print('0s in total_days ',z)

z1=(df['occupation'] == 'BUSINESS').sum()
#print('extras in occup ',z1)

print('---DATA PREVIEW---\n',df.head(50))

CorelationMatrix(df)
LinReg(df)