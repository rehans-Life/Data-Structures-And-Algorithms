from os import *
from sys import *
from collections import *
from math import *

def isPalindrome(string):
    n = len(string)

    i = 0   
    j = n-1

    while i <= j:

        if string[i] != string[j]:
            return False
        
        i+=1
        j-=1
    
    return True

def palindromePartitioning(string):

    n = len(string)
    dp = [-1 for _ in range(n+1)]

    dp[n] = 0

    for i in reversed(range(n)):
        minPartitions = inf
        temp = ""
        for j in range(i,n):
            temp+=string[j]

            if isPalindrome(temp):
                partitions = 1 + dp[j+1]
                minPartitions = min(minPartitions,partitions)
        
        dp[i] = minPartitions
    
    return dp[0] - 1
