# Memoization

# Time Complexity: O(n * v)
# Space Comlexity: O(v + n*v)

def countWaysToMakeChange(denominations, value):    
    
    n = len(denominations)
    dp = [[-1 for _ in range(value+1)] for _ in range(n)]
    
    def helper(i,target):

        if i == 0: return 1 if target % denominations[i] == 0 else 0
        if dp[i][target] != -1: return dp[i][target]

        pick = helper(i,target-denominations[i]) if denominations[i] <= target else 0
        notPick = helper(i-1,target)

        dp[i][target] = pick+notPick
        return dp[i][target]

    return helper(n-1,value)

# Tabulation

# Time Complexity: O(n * v)
# Space Comlexity: O(n*v)

def countWaysToMakeChange(denominations, value):    
    
    n = len(denominations)
    dp = [[-1 for _ in range(value+1)] for _ in range(n)]

    for target in range(value+1): 
        dp[0][target] = 1 if target % denominations[0] == 0 else 0

    for i in range(1,n):
        for target in range(value+1):

            pick = dp[i][target-denominations[i]] if denominations[i] <= target else 0
            notPick = dp[i-1][target] 

            dp[i][target] = pick+notPick 
    
    return dp[n-1][target]

# Space Optimisation

# Time Complexity: O(n * v)
# Space Comlexity: O(v)


def countWaysToMakeChange(denominations, value):    
    
    n = len(denominations)
    prev = [-1 for _ in range(value+1)]

    for target in range(value+1): 
        prev[target] = 1 if target % denominations[0] == 0 else 0

    for i in range(1,n):
        
        temp = [-1 for _ in range(value+1)]
        for target in range(value+1):

            pick = temp[target-denominations[i]] if denominations[i] <= target else 0
            notPick = prev[target] 

            temp[target] = pick+notPick 
        prev = temp
    
    return prev[target]

