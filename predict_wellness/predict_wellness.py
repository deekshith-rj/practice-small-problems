#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/stockprediction?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-09
"""

import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import cross_val_score

# Load the data
train = pd.read_csv('./data/bodyfat-comp.csv')
train.drop(columns=['Density', 'Id'], inplace=True)
X_train, y_train = train.drop('BodyFat', axis=1), train['BodyFat']
test = pd.read_csv('./data/bodyfat-validate.csv')

# Fit the model
model = LinearRegression()
model = Ridge(alpha=0.5)
model = Lasso(alpha=0.65)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
