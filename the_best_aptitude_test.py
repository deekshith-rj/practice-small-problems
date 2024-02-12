#!/usr/bin/python
"""
This module is my attempt to solve the problem 
https://www.hackerrank.com/challenges/the-best-aptitude-test/problem?isFullScreen=true
 on HackerRank.
    
Author: Deekshith Rao
Date: 2024-02-12
"""

from scipy.stats import pearsonr

T = int(input())

for t in range(T):
    N = int(input())
    gpas = [float(x) for x in input().split()]
    apt_scores = [[int(x) for x in input().split()] for i in range(5)]
    corrs = [pearsonr(gpas, apt_scores[i]) for i in range(len(apt_scores))]
    max_corr_index = max(range(len(corrs)), key=lambda i: corrs[i][0])
    print(max_corr_index+1)
