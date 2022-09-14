def ColRename(df):
    import pandas as pd

    df.columns = ['HH', 'ID', 'ward', 'age', 'age_g','sex', 'marital_stat', 'edu', 'occupation','income', 'work_days',
                  'WEEKEND_activity', '4_wheeler', '2_wheeler', 'cycle']

    df['extra_days'] = 0
    df.extra_days = df.extra_days.astype(int)
    #df.age = df.age.astype(int)

    return df
    # print(df.head())
