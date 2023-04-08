def longestIncreasingSubsequence(arr, n):
    dp = [1 for _ in range(n)]
    hash = [i for i in range(n)]
    maxIndex = 0
    maxLength = 1

    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                dp[i] = 1 + dp[prev]
                hash[i] = prev
        if maxLength < dp[i]:
            maxLength = dp[i]
            maxIndex = i
    
    lis = []
    i = maxIndex

    while True:
        lis.append(arr[i])
        if i == hash[i]: break
        i = hash[i]
    
    lis.reverse()
    
    return lis