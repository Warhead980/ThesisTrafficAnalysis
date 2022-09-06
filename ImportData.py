def ImportData():
    import pandas as pd
    
    path=r'F:\IIT KGP\III Semester\Thesis\Research\Raw Data\BMC DATA.csv'
    df=pd.read_csv(path, low_memory=False)

    return df
    #print(df.head())
