def FillData(df):
    import pandas as pd
    import numpy as np

    #occupation


    # total_days
    df.loc[df['edu'] == 'IL', 'occupation'] = 'UNEMPLOYED'
    df.loc[df['occupation'] == 'UNEMPLOYED', 'work_days'] = 0
    df.loc[df['occupation'] == 'HOUSEWIFE', 'work_days'] =+2

    # age filter
    df = df[~df.age.str.contains("MONTHS|months|M", na=False)]
    df.age = df.age.astype(float)
    df['age'] = np.ceil(df.age)
    df.age = df.age.astype(int)
    df = df[df['age'] < 200]

    # ward filter
    df = df[df['ward'].notna()]
    df.ward = df.ward.astype(int)

    # education filter
    df['edu'] = df['edu'].replace(['IL','P','S','H','G','PG','O'],[0,1,2,3,4,5,6])

    # set 1 extra day for MEDICAL (P)
    df.loc[df['WEEKEND_activity'].str.contains('P', case=False), ['extra_days']] += 1
    # set 3 extra day for RECREATIONAL GYM PARK (R1A)
    df.loc[df['WEEKEND_activity'].str.contains('R1A', case=False), ['extra_days']] += 3
    # set 1 extra day for RECREATIONAL MOVIES SPORTS (R1B)
    df.loc[df['WEEKEND_activity'].str.contains('R1B', case=False), ['extra_days']] += 1
    # set 1 extra day for EVERYDAY SHOPPING (M2A)
    df.loc[df['WEEKEND_activity'].str.contains('M2A', case=False), ['extra_days']] += 1
    # set 1 extra day for EAT OUT (R1C)
    df.loc[df['WEEKEND_activity'].str.contains('R1C', case=False), ['extra_days']] += 1
    # set 1 extra day for RELIGIOUS ACTIVITIES (R1D)
    df.loc[df['WEEKEND_activity'].str.contains('R1D', case=False), ['extra_days']] += 1
    # set 1 extra day for SOCIAL (R2)
    df.loc[df['WEEKEND_activity'].str.contains('R2', case=False), ['extra_days']] += 1
    # set 0 extra day for IN HOME ACTIVITIES (H1)
    df.loc[df['WEEKEND_activity'].str.contains('H1', case=False), ['extra_days']] += 0
    # set 1 extra day for IN HOME ACTIVITIES (H2|I1|I2|I3|J1|J2)
    df.loc[df['WEEKEND_activity'].str.contains('H2|I1|I2|I3|J1|J2', case=False), ['extra_days']] += 2

    # work days
    df['work_days'] = df['work_days'].fillna(0)
    df['work_days'] = df['work_days'].replace(
        ['8:00', '7.0', '6.0', '5.0', '4.0', '3.0', '2.0', '1.0', '0.0', '0:00', '   ', 'NOT FIXED'],
        ['7', '7', '6', '5', '4', '3', '2', '1', '0', '0', '0', '5'])

    df.work_days = df.work_days.astype(int)

    # total work days
    df['total_days'] = df['work_days'] + df['extra_days']

    # income filter

    df['income'] = df['income'].replace(['1.5LAC', '25,M000', '1 LAC', '30,M000', '600000', '10000 (HUSBAND PENSION)'],
                                        ['150000', '25000', '100000', '30000', '50000', '10000'])

    list = ['JAGATPUR ADARSHA BIDYA MANDIR', 'REFUSED', 'R', 'C/S', 'REFUNDED', '5', 'BALLYGUNGE', 'SEALDAH', 'U/E']
    df = df[df.income.isin(list) == False]

    df['income'] = df['income'].str.replace(',', '')
    df['income'] = df['income'].astype(float)
    df['income'] = df['income'].fillna(0)
    df['income'] = df['income'].astype(int)

    # 4 wheeler
    df['4_wheeler'] = df['4_wheeler'].fillna(0)
    df['4_wheeler'] = df['4_wheeler'].astype(int)

    # 2 wheeler
    df['2_wheeler'] = df['2_wheeler'].fillna(0)
    df['2_wheeler'] = df['2_wheeler'].astype(int)

    # cycle
    df = df[~df.cycle.str.contains('R|A|GOODS CAR|B|E|V|T|SUZUKI', na=False)]
    df['cycle'] = df['cycle'].fillna(0)

    df['cycle'] = df['cycle'].astype(int)

    return df
