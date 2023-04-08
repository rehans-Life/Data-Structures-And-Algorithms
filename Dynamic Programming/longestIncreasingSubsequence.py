from sys import stdin
import sys 
sys.setrecursionlimit(10**7)

def longestIncreasingSubsequence(arr, n):

    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    for prev in range(n+1):
        dp[n][prev] = 0
    
    for i in reversed(range(n)):
        for prev in range(n+1):
            longestLen = 0

            if prev == 0 or arr[i] > arr[prev-1]:
                longestLen = 1 + dp[i+1][i+1]
            
            longestLen = max(longestLen,0 + dp[i+1][prev])

            dp[i][prev] = longestLen
    
    return dp[0][0]

def longestIncreasingSubsequence(arr, n):
    dp = [1 for _ in range(n)]

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev]:
                dp[i] = max(dp[i], 1 + dp[prev])
    
    return max(dp)


def longestIncreasingSubsequence(arr, n):
    lis = []
    lis.append(arr[0])
    length = 1

    for i in range(1,n):
        if arr[i] > lis[length-1]:
            lis.append(arr[i])
            length+=1
        else:
            correctPosition = bs(lis,length,arr[i])
            lis[correctPosition] = arr[i]
    
    return length

def bs(lis,n,num):
        res = -1

        start = 0
        end = n - 1

        while start <= end:
            mid = (start+end) // 2

            if lis[mid] == num:
                return mid

            if lis[mid] > num:
                res = mid
                end = mid-1
            else:
                start = mid+1
        
        return res
