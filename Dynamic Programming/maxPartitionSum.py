from os import *
from sys import *
from collections import *
from math import *
from typing import List

def maximumSubarray(num: List[int], k: int) -> int:
    
    n = len(num)
    dp = [-1 for _ in range(n+1)]

    dp[n] = 0

    for i in reversed(range(n)):
        maxSum = -inf
        maxValue = num[i]
        length = 0

        for j in range(i,min(k+i,n)):
            maxValue = max(maxValue,num[j])
            length+=1
            sum = maxValue * length + dp[j+1]
            maxSum = max(maxSum,sum)
        
        dp[i] = maxSum      

    return dp[0]