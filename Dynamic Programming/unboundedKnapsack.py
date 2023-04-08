from os import *
from sys import *
from collections import *
from math import *

def unboundedKnapsack(n, w, profit, weight):

    dp = [[-1 for _ in range(w+1)] for _ in range(n)]
    
    def helper(i,w):

        if i == 0: return (w // weight[i]) * profit[i]
        if dp[i][w] != -1: return dp[i][w]

        pick = profit[i] + helper(i,w-weight[i]) if weight[i] <= w else -inf
        notPick = 0 + helper(i-1,w)

        dp[i][w] = max(pick,notPick)
        return dp[i][w]
    
    return helper(n-1,w)

def unboundedKnapsack(n, w, profit, weight):

    prev = [-1 for _ in range(w+1)]

    for capacity in range(w+1):
        prev[capacity] = (capacity // weight[0]) * profit[0]

    for i in range(1,n):
        curr = [-1 for _ in range(w+1)]
        for capacity in range(w+1):
            pick = profit[i] + curr[capacity-weight[i]] if weight[i] <= capacity else -inf
            notPick = 0 + prev[capacity]    
            curr[capacity] = max(pick,notPick)        
        prev = curr
    
    return prev[w]

def unboundedKnapsack(n, w, profit, weight):

    prev = [-1 for _ in range(w+1)]

    for capacity in range(w+1):
        prev[capacity] = (capacity // weight[0]) * profit[0]

    for i in range(1,n):
        for capacity in range(w+1):
            pick = profit[i] + prev[capacity-weight[i]] if weight[i] <= capacity else -inf
            notPick = 0 + prev[capacity]    
            prev[capacity] = max(pick,notPick)        
    
    return prev[w]