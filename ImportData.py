def ImportData():
    import pandas as pd

    # path1 = r'https://raw.githubusercontent.com/Warhead980/ThesisTrafficAnalysis/main/data/BMC%20DATA.csv'
    # path2 = r'https://raw.githubusercontent.com/Warhead980/ThesisTrafficAnalysis/main/data/BMC%20DATA_1.csv'
    # df = pd.read_csv(path1, index_col=0)
    # df1 = pd.read_csv(path2, index_col=0)

    df = pd.read_csv(r'D:\ThesisTrafficAnalysis\data\BMC DATA.csv', index_col=0)
    df1 = pd.read_csv(r'D:\ThesisTrafficAnalysis\data\BMC DATA_1.csv', index_col=0)
    df = pd.concat([df, df1], axis=1)
    df = df.reset_index()
    return df
    # print(df.head())
