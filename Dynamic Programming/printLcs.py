
def printLcs(s, t):
        n = len(s)
        m = len(t)

        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 0

        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        lcs  = ["*"] * dp[n][m]
        index = dp[n][m] - 1
        i = n
        j = m
        
        while i != 0 and j != 0:
            if s[i-1] == t[j-1]:
                lcs[index] = s[i-1]
                index-=1
                i-=1
                j-=1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    j-=1
                else:
                    i-=1            
        
        return ''.join(lcs)

print(printLcs('xyz','yuz'))