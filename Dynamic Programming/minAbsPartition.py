from os import *
from sys import *
from collections import *
from math import *

def minSubsetSumDifference(arr, n):
    
    k = sum(arr)

    prev = [False] * (k+1)

    prev[0] = True

    if arr[0] <= k: prev[arr[0]] = True

    for i in range(1,n):
        temp = [False] * (k+1)
        temp[0] = True
        for target in range(1,k+1):
            if arr[i] <= target:
                temp[target] = prev[target-arr[i]]
            
            if not temp[target]:
                temp[target] = prev[target]
        prev = temp
    
    minAbsDiff = inf
    for target,canAchieve in enumerate(prev):
        if canAchieve:
            partition2sSum = k - target
            absDifference = abs(target - partition2sSum)
            minAbsDiff = min(minAbsDiff,absDifference)
        if target == len(prev) // 2: break
    
    return minAbsDiff