#!/usr/bin/python
"""
This module is my attempt to solve the Bot Saves Princess problem 
(https://www.hackerrank.com/challenges/saveprincess) on HackerRank. 

Author: Deekshith Rao
Date: 2023-11-29
"""

def displayPathtoPrincess(n, grid):
    """
    Display the path from a bot to a princess in a grid.

    Args:
        n (int): The size of the grid (n x n).
        grid (list): A list of strings representing the grid.

    Returns:
        None

    Example:
        >>> grid = ['---', '-m-', '--p']
        >>> displayPathtoPrincess(3, grid)
        DOWN
        DOWN
        RIGHT
    """
    # Implementation of the function
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_i, bot_j = i, j
            elif grid[i][j] == 'p':
                prin_i, prin_j = i, j
    dir_i, dir_j = prin_i - bot_i, prin_j - bot_j
    print('\n'.join(['DOWN',] * dir_i) if dir_i > 0 else '\n'.join(['UP',] * -dir_i))
    print('\n'.join(['RIGHT',] * dir_j) if dir_j > 0 else '\n'.join(['LEFT',] * -dir_j))


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
