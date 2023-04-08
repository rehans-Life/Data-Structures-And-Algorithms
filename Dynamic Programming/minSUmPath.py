from math import *

# Memoization

# Time Complexity: O(n*m)
# Space Complexity: O(n+m + n*m)

def minSumPath(grid):
    
    n = len(grid)
    m = len(grid[0])

    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def helper(row,col):

        if row == 0 and col == 0:
            return grid[row][col]
        
        if row < 0 or col < 0:
            return inf
        
        if dp[row][col] != -1:
            return dp[row][col]
        
        up = grid[row][col] + helper(row-1,col)
        left = grid[row][col] + helper(row,col-1)

        dp[row][col] = min(up,left)
    
        return dp[row][col]
    
    return helper(n-1,m-1)

# Space Optimisation

# Time Complexity: O(n*m)
# Space Complexity: O(m)

def minSumPath(grid):
    
    n = len(grid)
    m = len(grid[0])

    prev = [0] * m

    for i in range(n):
        temp = [0] * m
        for j in range(m):
            if i == 0  and j == 0:
                temp[j] = grid[i][j]
            else:
                up,left = inf,inf

                if i > 0:
                    up = grid[i][j] + prev[j]

                if j > 0:
                    left = grid[i][j] + temp[j-1]

                temp[j] = min(up,left)

        prev = temp

    return prev[m-1]  
    