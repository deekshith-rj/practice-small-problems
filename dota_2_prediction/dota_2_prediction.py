#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/dota2prediction/problem?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-13
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score

K = int(input())
X_test_raw = []
for i in range(K):
    heroes = input().strip().split(",")
    X_test_raw.append(dict(zip(heroes, [1] * 5 + [-1] * 5)))

X_train_raw = []
heroes_all = []
y_train = []
with open('./trainingdata.txt') as f:
    for line in f:
        heroes = line.strip().split(",")
        X_train_raw.append(dict(zip(heroes[:10], [1] * 5 + [-1] * 5)))
        heroes_all.extend(heroes[:10])
        y_train.append(int(heroes[10]))

heroes_all = list(set(heroes_all))
X_train = pd.DataFrame(X_train_raw, columns=heroes_all).fillna(0).astype(int)
X_test = pd.DataFrame(X_test_raw, columns=heroes_all).fillna(0).astype(int)
y_train = pd.Series(y_train)

model = LogisticRegression()
# skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='roc_auc')
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n".join(map(str, y_pred)))
