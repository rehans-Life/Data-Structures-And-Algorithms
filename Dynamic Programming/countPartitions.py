from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    sumArray = 0
    for num in arr: sumArray+=num

    if (sumArray-d) < 0 or (sumArray-d) % 2 != 0: 
        return 0

    tar = (sumArray-d) // 2

    dp = [[0 for _ in range(tar+1)] for _ in range(n)]

    dp[0][0] = 1
    if arr[0] <= tar: dp[0][arr[0]]+=1
    
    for i in range(1,n):
        for sum in range(0,tar+1):
            pick,notPick=0,0

            if arr[i] <= sum:
                pick = dp[i-1][sum-arr[i]]
            
            notPick = dp[i-1][sum]

            dp[i][sum]+= (pick+notPick)
    
    return dp[n-1][tar] % 1000000007


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    sumArray = 0
    for num in arr: sumArray+=num

    if (sumArray-d) < 0 or (sumArray-d) % 2 != 0: 
        return 0

    tar = (sumArray-d) // 2

    prev = [0 for _ in range(tar+1)]

    prev[0] = 1
    if arr[0] <= tar: prev[arr[0]]+=1
    
    for i in range(1,n):
        temp = [0 for _ in range(tar+1)]
        for sum in range(0,tar+1):
            pick,notPick=0,0

            if arr[i] <= sum:
                pick = prev[sum-arr[i]]
            
            notPick = prev[sum]

            temp[sum]+= (pick+notPick)
        prev = temp 

    return prev[tar] % 1000000007
