#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true)
 on HackerRank. Also works (w/o the polynomial features part) for the problem
 https://www.hackerrank.com/challenges/predicting-house-prices/problem?isFullScreen=true
    
Author: Deekshith Rao
Date: 2024-02-09
"""
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def read_input(f):
    return [f(x) for x in input().split(' ')]


F, N = read_input(int)
train = pd.DataFrame(columns=list(range(1, F+1)) + ['y',], dtype=float)
for row in range(N):
    train.loc[row] = read_input(float)
T, = read_input(int)
test = pd.DataFrame(columns=list(range(1, F+1)), dtype=float)
for row in range(T):
    test.loc[row] = read_input(float)


# Separate features and target variables
X_train = train.iloc[:, :-1]
y_train = train.iloc[:, -1]

# Create polynomial features
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)

# Fit polynomial regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predict on test data
X_test_poly = poly.transform(test)
predictions = model.predict(X_test_poly)

print('\n'.join(map(str, predictions)))
