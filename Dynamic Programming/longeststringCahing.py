from os import *
from sys import *
from collections import *
from math import *
from typing import List

def compare(curr,prev):

    i,j = 0,0
    n,m = len(curr),len(prev)

    if n != (m + 1): return False

    while i < n and j < m:
        if curr[i] == prev[j]:
            i+=1
            j+=1
        else:
            i+=1
    
    if (i == n and j == m) or (i == n-1 and j == m):
        return True
    else:
        return False

def longestStrChain(arr: List[str]) -> int:
    arr = sorted(arr, key=len)
    n = len(arr)
    dp = [1 for _ in range(n)]
    hash = [i for i in range(n)]
    maxIndex = 0
    maxLength = 1

    for i in range(n):
        for prev in range(i):
            if compare(arr[i],arr[prev]) and dp[i] < 1 + dp[prev]:
                dp[i] = 1 + dp[prev]
                hash[i] = prev
        if maxLength < dp[i]:
            maxLength = dp[i]
            maxIndex = i
    
    return max(dp)
