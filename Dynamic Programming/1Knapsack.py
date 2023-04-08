from math import *

class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [[-1 for _ in range(W+1)] for _ in range(n)]
        
        for capacity in range(W+1):
            dp[0][capacity] = val[0] if wt[0] <= capacity else 0
        
        for i in range(1,n):
            for capacity in range(W+1):
                
                pick = val[i] + dp[i-1][capacity - wt[i]] if wt[i] <= capacity else -inf
                notPick = 0 + dp[i-1][capacity]
                
                dp[i][capacity] = max(pick,notPick)
        
        return dp[n-1][W]

class Solution:
    def knapSack(self,W, wt, val, n):
        prev = [-1 for _ in range(W+1)]
        
        for capacity in range(W+1):
            prev[capacity] = val[0] if wt[0] <= capacity else 0
        
        for i in range(1,n):
            temp = [-1 for _ in range(W+1)]
            for capacity in range(W+1):
                
                pick = val[i] + prev[capacity - wt[i]] if wt[i] <= capacity else -inf
                notPick = 0 + prev[capacity]
                
                temp[capacity] = max(pick,notPick)
            prev = temp
        return prev[W]

class Solution:
    def knapSack(self,W, wt, val, n):
        prev = [-1 for _ in range(W+1)]
        
        for capacity in range(W+1):
            prev[capacity] = val[0] if wt[0] <= capacity else 0
        
        for i in range(1,n):
            for capacity in reversed(range(W+1)):
                
                pick = val[i] + prev[capacity - wt[i]] if wt[i] <= capacity else -inf
                notPick = 0 + prev[capacity]
                
                prev[capacity] = max(pick,notPick)

        return prev[W]
                