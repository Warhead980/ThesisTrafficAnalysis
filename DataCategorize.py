import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def DataCategorize(df):

    df['income']=df['income'].multiply(12)

    df.loc[df['income'] == 0, 'income_cat'] = 0
    df['income_cat'] = np.where((df['income'] > 0) &
                                (df['income'] < 150000), 1, df['income_cat'])
    df['income_cat'] = np.where((df['income'] >= 150000) &
                                (df['income'] < 340000), 2,df['income_cat'])
    df['income_cat'] = np.where((df['income'] >= 340000) &
                                (df['income'] < 1700000), 3, df['income_cat'])
    df['income_cat'] = np.where((df['income'] >= 1700000), 4, df['income_cat'])

    df['income']=np.where((df['income'] > 1500000), 0,df['income'])
    df['income_cat'].plot(kind='hist')
    df.plot(kind = 'scatter', x='income', y='age')

    plt.show()

    print(df.head(50))