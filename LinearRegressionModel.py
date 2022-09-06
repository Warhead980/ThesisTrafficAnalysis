import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

def LinReg(df):
    #x=np.reshape(df['income'],(-1,1))
    x=df['income']
    #x=np.reshape(x,(-1, 1))
    y=df['total_days']
    x.values.tolist()
    y.values.tolist()
    print(x.info)
    print(y.info)
    #print(x[1][1])
    #print(y)
    #model = LinearRegression()
    #model.fit(x,y)
    #r_sq = model.score(x, y)
    #print(f"coefficient of determination: {r_sq}")