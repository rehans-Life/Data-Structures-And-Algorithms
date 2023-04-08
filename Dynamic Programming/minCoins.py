from math import *
from typing import List

# Memoization

# Time Complexity: O(n*x)
# Space Complexity: O(x + n*x)

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [[-1 for _ in range(x+1)] for _ in range(n)]

    def helper(i,target):

        if i == 0:
            return target // num[i] if target % num[i] == 0 else inf
        
        if dp[i][target] != -1: return dp[i][target]

        pick = 1 + helper(i,target-num[i]) if num[i] <= target else inf
        notPick = 0 + helper(i-1,target)

        dp[i][target] = min(pick,notPick)
        return dp[i][target]
    
    minCoins = helper(n-1,x) 

    return minCoins if minCoins != inf else -1

# Tabulation

# Time Complexity: O(n*x)
# Space Complexity: O(n*x)

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    dp = [[-1 for _ in range(x+1)] for _ in range(n)]

    for target in range(x+1):
        dp[0][target] = target // num[0] if target % num[0] == 0 else inf

    for i in range(1,n):
        for target in range(x+1):
            pick = 1 + dp[i][target-num[i]] if num[i] <= target else inf
            notPick = 0 + dp[i-1][target]
            dp[i][target] = min(pick,notPick)
    
    return dp[n-1][x] if dp[n-1][target] != inf else -1

# Space Complexity

# Time Complexity: O(n*x)
# Space Complexity: O(x)

def minimumElements(num: List[int], x: int) -> int:
    n = len(num)
    prev = [-1 for _ in range(x+1)]

    for target in range(x+1):
        prev[target] = target // num[0] if target % num[0] == 0 else inf

    for i in range(1,n):
        temp = [-1 for _ in range(x+1)]
        for target in range(x+1):
            pick = 1 + temp[target-num[i]] if num[i] <= target else inf
            notPick = 0 + prev[target]
            temp[target] = min(pick,notPick)
        prev = temp
    
    return prev[x] if prev[x] != inf else -1
