#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:18:03 2019

@author: omer
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X, y , test_size = 1/3 , random_state = 0 )

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train), color='blue')
plt.show()


plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train), color='blue')
plt.show()



