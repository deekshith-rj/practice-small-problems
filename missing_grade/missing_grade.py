#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/predict-missing-grade/problem?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-13
"""

import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import time

# Reading the test data -------------------------------------------------------
N_test = int(input())
test = []
for i in range(N_test):
    test.append(json.loads(input()))
_ = [x.pop('serial') for x in test]

# Loading the training data ---------------------------------------------------
train = []
with open('training.json') as f:
    N_train = int(f.readline())
    for i in range(N_train):
        train.append(json.loads(f.readline()))
_ = [x.pop('serial') for x in train]

# Preprocessing the data ------------------------------------------------------
y_train = [x.pop('Mathematics') for x in train]
sub_lists = [list(x.keys()) for x in train]
sub_all = list(set([item for sub_list in sub_lists for item in sub_list]))
X_train = pd.DataFrame(train, columns=sub_all).fillna(0).astype(int)
X_test = pd.DataFrame(test, columns=sub_all).fillna(0).astype(int)

# Training the model ----------------------------------------------------------
model = LinearRegression()
# scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_root_mean_squared_error')
model.fit(X_train, y_train)
y_pred = model.predict(X_test).round().astype(int)
print("\n".join(map(str, y_pred)))