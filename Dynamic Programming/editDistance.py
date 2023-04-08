class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def helper(i,j):

            if i < 0: return j+1
            
            if j < 0: return i+1

            if dp[i][j] != -1: return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = 0 + helper(i-1,j-1)
                return dp[i][j]
            else:
                replace = 1 + helper(i-1,j-1)
                delete = 1 + helper(i-1,j)
                insert = 1 + helper(i,j-1)
                dp[i][j] = min(replace,delete,insert)
                return dp[i][j]
        
        return helper(n-1,m-1)