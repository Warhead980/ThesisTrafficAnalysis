import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


def LinReg(df):

    df=df[df["income"] < 120000]
    x = df['income'].tolist()
    x = np.reshape(x, (-1, 1))

    y = df['total_days'].tolist()

    # print(x)
    # print(y)

    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)

    plt.plot(x, y, 'o')
    # m, b = np.polyfit(x, y, 1)
    plt.plot(x, model.coef_ * x + model.intercept_)
    plt.show()

    print(f"coefficient of determination: {r_sq}")
    print(f"intercept: {model.intercept_}")
    print(f"slope: {model.coef_}")

    y_pred = model.intercept_ + model.coef_ * x
