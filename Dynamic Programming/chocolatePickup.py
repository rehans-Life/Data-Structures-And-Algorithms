from typing import List
from math import *

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:

    dp = [[[-1 for _ in range(c)] for _ in range(c)] for _ in range(r)]

    def helper(i,j1,j2):
        
        if j1 < 0 or j1 == c or j2 < 0 or j2 == c:
            return -inf
        
        if i == r-1:
            return grid[i][j1] if j1 == j2 else grid[i][j1]+grid[i][j2]
        
        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]
        
        maxSumPath = 0

        for dj1 in range(-1,2):
            for dj2 in range(-1,2):
                if j1 == j2:
                    maxSumPath = max(maxSumPath,grid[i][j1] + helper(i+1,j1+dj1,j2+dj2))
                else:
                    maxSumPath = max(maxSumPath,grid[i][j1] +grid[i][j2] + helper(i+1,j1+dj1,j2+dj2))                  
        
        dp[i][j1][j2] = maxSumPath

        return dp[i][j1][j2]
    
    return helper(0,0,c-1)