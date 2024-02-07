#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
# import seaborn as sns
# import matplotlib.pyplot as plt

from functions import read_train

if __name__ == '__main__':
    timeCharged = float(input().strip())
    train = read_train()
    X = train.loc[:, ['time_charged']]
    y = train.time_used

    model_dt_basic = LinearRegression()
    model_dt_basic.fit(X, y)

    print(model_dt_basic.predict(pd.DataFrame({'time_charged': [timeCharged]}))[0])
