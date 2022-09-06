# importing builtin classes
import numpy as np

# importing custom classes
from ImportData import *
from ColumnFiltering import *
from ColRename import *
from FillData import *
from CheckUnique import *
from ToNumeric import *
from CorelationMatrix import *
# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# setting maximum number of columns
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)

df = ImportData()
df = ColFilter(df)
df = ColRename(df)
df = FillData(df)
df = ToNumeric(df)

#CheckUnique(df, 'edu')
print(df.dtypes)
print(df.head(20))

CorelationMatrix(df)