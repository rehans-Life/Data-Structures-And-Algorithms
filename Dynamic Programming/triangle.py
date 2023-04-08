from os import *
from sys import *
from collections import *
from math import *
from typing import *

# Memoization

# Time Complexity: O(n*m)
# Space Complexity: O(n + n*n)

def minimumPathSum(triangle, n):
    dp = [[-1 for _ in range(i+1)] for i in range(n)]

    def helper(i,j):

        if i == n-1:
            return triangle[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]

        d = triangle[i][j] + helper(i+1,j)
        dr = triangle[i][j] + helper(i+1,j+1)

        dp[i][j] = min(d,dr)

        return dp[i][j]
    
    return helper(0,0)

# Tabulation

# Time Complexity: O(n*m)
# Space Complexity: O(n*n)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(i+1)] for i in range(n)]

        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for i in reversed(range(n-1)):
            for j in range(i+1):
                d = triangle[i][j] + dp[i+1][j]
                dr = triangle[i][j] + dp[i+1][j+1]

                dp[i][j] = min(d,dr)
        
        return dp[0][0]