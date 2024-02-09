#!/usr/bin/python
"""
This module is my attempt to solve the Bot Saves Princess problem 
(https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true)
 on HackerRank. 

Author: Deekshith Rao
Date: 2024-02-09
"""
import pandas as pd


def read_input(f):
    return [f(x) for x in input().split(' ')]


F, N = read_input(int)
train = pd.DataFrame(columns=list(range(1, F+1)) + ['y',], dtype=float)
for row in range(N):
    train.loc[row] = read_input(float)
T, = read_input(int)
test = pd.DataFrame(columns=list(range(1, F+1)), dtype=float)
for row in range(T):
    test.loc[row] = read_input(float)
