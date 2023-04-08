from typing import List
from math import *

def frogJump2(heights: List[int],k):
    n = len(heights)
    dp = [-1] * n
   
    def helper(i):
        nonlocal heights,k
        if i == 0: return 0
        
        if dp[i] != -1:
            return dp[i]
       
        maxStairJump = max(i-k,0)
        minEnergy = inf 
       
        for j in reversed(range(maxStairJump,i)):
           minEnergy = min(minEnergy,(helper(j) + abs(heights[i] - heights[j])))
           
        dp[i] = minEnergy
        return dp[i]
    
    return helper(n-1)

heights = [10, 30, 40, 50, 20]
k = 3
print(frogJump2(heights,k))


def frogJump2II(heights: List[int],k):
    n = len(heights)
    dp = [-1] * n
    dp[0] = 0
    
    for i in range(1,n):
        minEnergy = inf
        maxStairJump = max(i-k,0)
        for j in range(maxStairJump,i):
            minEnergy = min(minEnergy,dp[j] + abs(heights[i]-heights[j]))
        dp[i] = minEnergy
            
    return dp[n-1]

heights = [10, 30, 40, 50, 20]
k = 3
print(frogJump2II(heights,k))     
    