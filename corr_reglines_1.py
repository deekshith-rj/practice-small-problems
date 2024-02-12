#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-09
"""

import math

x = [int(x) for x in input().split()[2:]]
y = [int(x) for x in input().split()[2:]]

# print(x)
# print(y)

ex = sum(x) / len(x)
ey = sum(y) / len(y)

cov = sum([(xi - ex) * (yi - ey) for (xi, yi) in zip(x, y)])
stdx = math.sqrt(sum([(xi-ex) ** 2 for xi in x]))
stdy = math.sqrt(sum([(yi-ey) ** 2 for yi in y]))
corr = cov / (stdx * stdy)

print(round(corr, 3))


# from scipy.stats import pearsonr
# print(pearsonr(x, y))
