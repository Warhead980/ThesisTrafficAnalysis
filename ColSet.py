def ColSet(df):
    df = df.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]]

    df = df[['ward', 'age', 'sex', 'marital_stat', 'edu', 'occupation', 'income',
             '4_wheeler', '2_wheeler', 'cycle', 'work_days', 'extra_days', 'total_days']]
    return df