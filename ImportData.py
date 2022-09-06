def ImportData():
    import pandas as pd

    path1 = r'D:\ThesisTrafficAnalysis\data\BMC DATA.csv'
    path2 = r'D:\ThesisTrafficAnalysis\data\BMC DATA_1.csv'
    df = pd.read_csv(path1, low_memory=False)
    df1 = pd.read_csv(path2, low_memory=False)
    df=pd.concat([df,df1], axis=1)
    return df
    # print(df.head())
