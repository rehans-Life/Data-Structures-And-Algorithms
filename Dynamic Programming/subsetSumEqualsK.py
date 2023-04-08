from os import *
from sys import *
from collections import *
from math import *

# Recursive

def subsetSumToK(n, k, arr):
    
    def helper(i=0,sum=0):

        if sum == k:
            return True
        
        if sum > k:
            return False
        
        if i == n-1:
            return sum+arr[i] == k
        
        take = helper(i+1,sum+arr[i])

        if take:
            return True
        
        notTake = helper(i+1,sum)

        if notTake:
            return True
        
        return False
    
    return helper()

# Memoization

def subsetSumToK(n, k, arr):

    dp = [[-1 for _ in range(k)] for _ in range(n)]

    def helper(i=0,sum=0):

        if sum == k:
            return True
        
        if sum > k:
            return False
        
        if i == n-1:
            return sum+arr[i] == k
        
        take = helper(i+1,sum+arr[i])
        dp[i][sum] = take

        if dp[i][sum]:
            return True
        
        notTake = helper(i+1,sum)
        dp[i][sum] = notTake

        if dp[i][sum]:
            return True
        
        return dp[i][sum]
    
    return helper()

# Tabulation

def subsetSumToK(n, k, arr):
    dp = [[False for _ in range(k+1)] for _ in range(n)]
    
    for i in range(n):
        dp[i][k] = True
    
    for sum in range(k):
        dp[n-1][sum] = sum+arr[i] == k
    
    for i in reversed(range(n-1)):
        for sum in range(k):
            if sum+arr[i] <= k:
                dp[i][sum] = dp[i+1][sum+arr[i]]
            
            if not dp[i][sum]:
                dp[i][sum] = dp[i+1][sum]
            
    return dp[0][0]

# Space Optimisation

def subsetSumToK(n, k, arr):
    front = [False for _ in range(k+1)]
    
    for sum in range(k+1):
        front[sum] = True if sum == k else sum+arr[n-1] == k
    
    for i in reversed(range(n-1)):
        temp = [False] * (k+1)
        temp[k] = True
        for sum in range(k):
            if sum+arr[i] <= k:
                temp[sum] = front[sum+arr[i]]
            
            if not temp[sum]:
                temp[sum] = front[sum]
        front = temp

    return front[0]