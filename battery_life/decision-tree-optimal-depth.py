#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from functions import read_train


def get_mae(max_leaf_nodes, train_X, train_y, val_X, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(train_X, train_y)
    pred = model.predict(val_X)
    return mean_absolute_error(val_y, pred)


def get_mae_values(candidate_max_depth_values, X, y):
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    mae_values = []
    for max_leaf_nodes in candidate_max_depth_values:
        mae_values.append(get_mae(max_leaf_nodes, train_X, train_y, val_X, val_y))
    return mae_values
        

if __name__ == '__main__':
    timeCharged = float(input().strip())

    train = read_train()
    X = train.loc[:, ['time_charged']]
    y = train.time_used
    candidate_max_depth_values = range(2, 150, 2)
    mae_values = get_mae_values(candidate_max_depth_values, X, y)
    optimal_depth = candidate_max_depth_values[np.argmin(mae_values)]

    model_dt_basic = DecisionTreeRegressor(
        max_leaf_nodes=optimal_depth, random_state=1)
    model_dt_basic.fit(X, y)
    # print('training score: ', model_dt_basic.score(X, y))
    
    pred = model_dt_basic.predict(pd.DataFrame({'time_charged': [timeCharged]}))[0]
    print(pred)