import numpy as np
import pandas as pd

def ColFilter(df):

    df = df.iloc[:, [0,1,2,3,5,6,8,9,12,18,1060]]


    return df
