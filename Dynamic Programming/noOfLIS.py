from os import *
from sys import *
from collections import *
from math import *

from typing import List


def findNumberOfLIS(arr: List[int]) -> int:
    n = len(arr)

    dp = [1 for _ in range(n)]
    count = [1 for _ in range(n)]

    maxLength = 1
    noOfLIS = 0

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev]:
                if dp[i] < (1 + dp[prev]):
                    dp[i] = 1 + dp[prev]
                    count[i] = count[prev]
                elif dp[i] == (1 + dp[prev]):
                    count[i] += count[prev]
        
        if dp[i] > maxLength:
            maxLength = dp[i]
            noOfLIS = count[i]
        elif dp[i] == maxLength:
            noOfLIS += count[i]           

    return noOfLIS