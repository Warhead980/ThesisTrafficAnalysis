def ColRename(df):
    import pandas as pd

    df.columns = ['HH', 'ID', 'ward', 'age', 'sex', 'marital_stat', 'edu', 'occupation','income', 'work_days','WEEKEND_activity']

    df['extra_days'] = 0
    df.extra_days = df.extra_days.astype(int)
    #df.age = df.age.astype(int)

    return df
    # print(df.head())
