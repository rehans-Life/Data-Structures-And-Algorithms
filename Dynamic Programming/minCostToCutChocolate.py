from os import *
from sys import *
from collections import *
from math import *
from typing import List

def cost(n: int, c: int, cuts: List[int]) -> int:
    
    cuts.sort()
    cuts.insert(0,0)
    cuts.append(n)

    n = len(cuts)

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            dp[i][j] = 0
    
    for i in reversed(range(1,c+1)):
        for j in range(i,c+1):
            minCost = inf
            for k in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                minCost = min(cost,minCost)
            dp[i][j] = minCost         

    return dp[1][c]