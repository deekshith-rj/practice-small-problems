#!/usr/bin/python
"""
This module is my attempt to solve the problem 
(https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem?isFullScreen=true)
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-12
"""

x = [int(i) for i in input().split()[2:]]
y = [int(i) for i in input().split()[2:]]

m = sum([xi * yi for xi, yi in zip(x, y)]) / sum([xi ** 2 for xi in x])
# c = sum(y) / len(y) - m * (sum(x) / len(x))

print(round(m, 3))
