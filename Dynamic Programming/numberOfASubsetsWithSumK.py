from os import *
from sys import *
from collections import *
from math import *
from typing import List

from sys import *
from collections import *
from math import *

from typing import List

def findWays(num: List[int], tar: int) -> int:
    n = len(num)
    dp = [[-1 for _ in range(tar+1)] for _ in range(n)]

    def helper(i,sum):

        if sum < 0: return 0
        
        if i == 0: 
            if sum == 0 and num[0] == 0:
                return 2
            
            if sum == 0 or sum == num[0]:
                return 1
            
            return 0

        if dp[i][sum] != -1: return dp[i][sum]

        pick = helper(i-1,sum-num[i])
        notPick = helper(i-1,sum)

        dp[i][sum] = pick+notPick

        return dp[i][sum]
    
    return helper(n-1,tar)


def findWays(num: List[int], tar: int) -> int:
    n = len(num)
    dp = [[0 for _ in range(tar+1)] for _ in range(n)]

    dp[0][0] = 1
    if num[0] <= tar: dp[0][num[0]]+=1
    
    for i in range(1,n):
        for sum in range(0,tar+1):
            pick,notPick=0,0

            if num[i] <= sum:
                pick = dp[i-1][sum-num[i]]
            
            notPick = dp[i-1][sum]

            dp[i][sum]+= (pick+notPick)
    
    return dp[n-1][tar]


def findWays(num: List[int], tar: int) -> int:
    
    n = len(num)
    prev = [0] * (tar+1)

    prev[0] = 1    
    if num[0] <= tar: 
        prev[num[0]] += 1
    
    for i in range(1,n):
        temp = [0] * (tar+1)
        for sum in range(tar+1):
            pick = 0
            notPick = 0

            if num[i] <= sum:
                pick = prev[sum-num[i]]
            
            notPick = prev[sum]

            temp[sum]+=(pick+notPick)

        prev = temp
    
    return prev[tar]
