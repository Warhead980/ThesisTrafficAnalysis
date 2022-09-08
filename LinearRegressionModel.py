import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


def LinReg(df):
    x = df[['income', 'age', 'sex']]
    # x=x1[x1["income"] < 120000]
    # x = np.reshape(x, (-1, 1))

    y = df['total_days']

    # print(x)
    # print(y)

    reg = LinearRegression()
    reg.fit(x, y)

    print('Intercept: \n', reg.intercept_)
    print('Coefficients: \n', reg.coef_)

    # with statsmodels
    x = sm.add_constant(x)  # adding a constant

    modelOLS = sm.OLS(y, x).fit()
    modelWLS = sm.WLS(y, x).fit()
    modelGLS = sm.GLS(y, x).fit()
    predictions = modelOLS.predict(x)

    print(modelOLS.summary())
    print(modelWLS.summary())
    print(modelGLS.summary())


    '''
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
    '''
