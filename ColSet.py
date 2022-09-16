def ColSet(df):
    df = df.iloc[:, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

    df = df[['ward', 'age', 'age_g', 'sex', 'marital_stat', 'edu', 'occupation', 'income','income_cat',
             '4_wheeler', '2_wheeler', 'cycle','vehicle', 'work_days', 'extra_days', 'total_days']]
    return df
