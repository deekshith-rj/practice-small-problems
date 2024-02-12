#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/computing-the-correlation/problem?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-12
"""

from math import sqrt

N = int(input())
scores = []
for i in range(N):
    scores.append([int(x) for x in input().split()])

scores = [list(x) for x in list(zip(*scores))]


def print_corr(x, y):
    x_prod = [xi * yi for xi, yi in zip(x, y)]
    x_sq_sum = sum([xi**2 for xi in x])
    y_sq_sum = sum([yi**2 for yi in y])
    num = N * sum(x_prod) - sum(x) * sum(y)
    den = sqrt(N * x_sq_sum - sum(x)**2) * sqrt(N * y_sq_sum - sum(y)**2)
    print(round(num / den, 2))

print_corr(scores[0], scores[1])
print_corr(scores[1], scores[2])
print_corr(scores[2], scores[0])
