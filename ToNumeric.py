def ToNumeric(df):

    # sex number
    df["sex"] = df["sex"].replace(['M', 'F'], [0, 1])

    # marital status number
    df["marital_stat"] = df['marital_stat'].replace(['M', 'S', 'W', 'D', 'SE'], [1,2,3,4,5])

    # edu number
    df['edu']=df['edu'].replace(['H','S','G','PG','P','M'],[1,2,3,4,5,6])

    return df