from typing import *
from math import *

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        nums.insert(0,1)
        nums.append(1)

        m = len(nums)

        dp = [[-1 for _ in range(m)] for _ in range(m)]

        for i in range(1,m):
            for j in range(i):
                dp[i][j] = 0
        
        for i in reversed(range(1,n+1)):
            for j in range(i,n+1):
                maxCoins = -inf

                for k in range(i,j+1):
                    coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    maxCoins = max(coins,maxCoins)

                dp[i][j] = maxCoins              
    
        return dp[1][n]
    
print(False^False)