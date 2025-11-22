#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.kaggle.com/competitions/ml-olympiad-predicting-wellness)
 on Kaggle.
    
Author: Deekshith Rao
Date: 2024-04-06
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

# Load the data
train = pd.read_csv('./data/bodyfat-comp.csv')
train.drop(columns=['Density', 'Id'], inplace=True)
X_train, y_train = train.drop('BodyFat', axis=1), train['BodyFat']
test = pd.read_csv('./data/bodyfat-validate.csv')

# Fit the model
scaler = StandardScaler()
pca = PCA()
# model = LinearRegression()
model = Ridge()
# model = Lasso(alpha=0.7)
pipe = Pipeline([('scaler', scaler), ('pca', pca), ('model', model)])
param_grid = {
    # 'pca__n_components': [2, 4, 6, 8, 10, 12, 13], 
    # 'model__alpha': np.linspace(0.005, 0.5, 100)
    'model__alpha': [0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 7.5, 10]
}
search = GridSearchCV(pipe, param_grid=param_grid, 
                      scoring='neg_mean_squared_error', verbose=True)
search.fit(X_train, y_train)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
print("Accuracy: " + str(search.best_score_))


# Predict the test data
model.fit(X_train, y_train)
X_test = test.drop(columns=['Id'])
y_pred = model.predict(X_test)
pred = pd.DataFrame({'Id': test['Id'], 'BodyFat': y_pred})
pred.to_csv('./submission.csv', index=False)
