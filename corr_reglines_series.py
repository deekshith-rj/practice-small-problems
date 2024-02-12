#!/usr/bin/python
"""
This module is my attempt to solve the problem series "Correlation and 
Regression Lines on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-09
"""

import math

x = [int(x) for x in input().split()[2:]]
y = [int(x) for x in input().split()[2:]]

# Correlation and Regression Lines - a quick recap 1
# (https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true)

ex = sum(x) / len(x)
ey = sum(y) / len(y)

cov = sum([(xi - ex) * (yi - ey) for (xi, yi) in zip(x, y)])
stdx = math.sqrt(sum([(xi-ex) ** 2 for xi in x]))
stdy = math.sqrt(sum([(yi-ey) ** 2 for yi in y]))
corr = cov / (stdx * stdy)

print(round(corr, 3))

# Correlation and Regression Lines - a quick recap 2
# (https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem?isFullScreen=true)

m = sum([xi * yi for xi, yi in zip(x, y)]) / sum([xi ** 2 for xi in x])
c = sum(y) / len(y) - m * (sum(x) / len(x))

print(round(m, 3))
print(c)

# Correlation and Regression Lines - A quick recap 3
# (https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem?isFullScreen=true)

print(m * 10 + c)


# Correlation and Regression Lines - A quick recap 4
# (https://www.hackerrank.com/challenges/correlation-and-regression-lines-4/problem?isFullScreen=true)

print(8.5)
