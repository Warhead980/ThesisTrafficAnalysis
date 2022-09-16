import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def DataCategorize(df):

    # income category
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

    # edu number
    df['edu'] = df['edu'].replace(['H', 'S', 'G', 'PG', 'P', 'M'], [1, 2, 3, 4, 5, 6])

    df.loc[(df["occupation"] == "BUSINESS") |
           (df["occupation"] == "SMALL BUSINESS"), 'occupation'] = '1'

    df.loc[(df["occupation"] == "HEALTH PROFESSIONALS") |
           (df["occupation"] == "GOVT EMPLOYEE") |
           (df["occupation"] == "PVT EMPLOYEE") |
           (df["occupation"] == "TEACHING PROFESSIONALS") |
           (df["occupation"] == "UNDEFINED") |
           (df["occupation"] == "WORKER"), 'occupation'] = '2'

    df.loc[(df["occupation"] == "RETIRED") |
           (df["occupation"] == "UNEMPLOYED") |
           (df["occupation"] == "HOUSEWIFE"), 'occupation'] = '3'

    # age category
    df.loc[(df["age_g"] == "Above 60"), 'age_g'] = 1
    df.loc[(df["age_g"] == "30 to 60"), 'age_g'] = 2
    df.loc[(df["age_g"] == "25 to 30"), 'age_g'] = 3
    df.loc[(df["age_g"] == "18 to 25"), 'age_g'] = 4
    df.loc[(df["age_g"] == "12 to 18"), 'age_g'] = 5
    df.loc[(df["age_g"] == "6 to 12"), 'age_g'] = 6
    df.loc[(df["age_g"] == "0 to 6"), 'age_g'] = 7
    df.age_g = df.age_g.astype(int)

    #df['income_cat'].plot(kind='hist')
    df.plot(kind = 'hist', x='income', y='age')

    plt.show()

    return df