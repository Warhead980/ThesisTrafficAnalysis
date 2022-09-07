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

# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# setting maximum number of columns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 18)

df = ImportData()
df = ColFilter(df)
df = ColRename(df)
df = FillData(df)
df = ToNumeric(df)
df=df.sort_values('ID')
#df=ColSet(df)
CheckUnique(df, 'cycle')
print(list(df.columns.values))
print(df.dtypes)

print('---DATA PREVIEW---')
print(df.head(50))

#CorelationMatrix(df)
#LinReg(df)