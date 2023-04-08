from os import *
from sys import *
from collections import *
from math import *

def lcs(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 0
    
    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 0
    
    longestSubStr = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            longestSubStr = max(longestSubStr,dp[i][j])

    return longestSubStr




