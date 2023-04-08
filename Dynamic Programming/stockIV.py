from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices, n, k):
    next = [[0 for _ in range(k+1)] for _ in range(2)]

    for i in reversed(range(n)):
        curr = [[0 if cap == 0 else -1 for cap in range(k+1)] for _ in range(2)]
        for cap in range(1,k+1):
            curr[1][cap] = max(-prices[i] + next[0][cap], 0 + next[1][cap])
            curr[0][cap] = max(prices[i] + next[1][cap-1], 0 + next[0][cap])

        next = curr
    
    return next[1][k]