from os import *
from sys import *
from collections import *
from math import *

def maxProfit(prices, n):

    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    
    def helper(i,buy,cap):

        if cap == 0: return 0
        if i == n: return 0
        if dp[i][buy][cap] != -1: return dp[i][buy][cap]

        if buy:
            profit = max(-prices[i] + helper(i+1,0,cap), 0 + helper(i+1,1,cap))
        else:
            profit = max(prices[i] + helper(i+1,1,cap-1), 0 + helper(i+1,0,cap))
        
        dp[i][buy][cap] = profit
        return dp[i][buy][cap]
    
    return helper(0,1,2)


def maxProfit(prices, n):

    dp = [[[0 if cap == 0 else -1 for cap in range(3)] for _ in range(2)] for _ in range(n+1)]

    for buy in range(2):
        for cap in range(3):
            dp[n][buy][cap] = 0
    
    for i in reversed(range(n)):
        for cap in range(1,3):
            dp[i][1][cap] = max(-prices[i] + dp[i+1][0][cap], 0 + dp[i+1][1][cap])
            dp[i][0][cap] = max(prices[i] + dp[i+1][1][cap-1], 0 + dp[i+1][0][cap])
    
    return dp[0][1][2]

def maxProfit(prices, n):

    next = [[0 for _ in range(3)] for _ in range(2)]

    for i in reversed(range(n)):
        curr = [[0 if cap == 0 else -1 for cap in range(3)] for _ in range(2)]
        for cap in range(1,3):
            curr[1][cap] = max(-prices[i] + next[0][cap], 0 + next[1][cap])
            curr[0][cap] = max(prices[i] + next[1][cap-1], 0 + next[0][cap])

        next = curr
    
    return next[1][2]