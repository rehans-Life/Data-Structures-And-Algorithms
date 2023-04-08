from os import *
from sys import *
from collections import *
from math import *
from typing import List

def countSquares(n: int, m: int, arr: List[List[int]]):
    
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        if arr[i][0]: dp[i][0] = 1
    
    for j in range(m):
        if arr[0][j]: dp[0][j] = 1 

    for i in range(1,n): 
        for j in range(1,m):
            if arr[i][j]: 
                dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])

    count = 0

    for i in range(n):
        for j in range(m):
            count += dp[i][j]
    
    return count