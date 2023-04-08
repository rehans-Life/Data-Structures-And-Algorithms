
def longestPalindromeSubsequence(s):
        t = ''.join(reversed(list(s)))
        n = len(s)
        m = len(t)

        prev = [0 for _ in range(m+1)]
        
        for i in range(1,n+1):
            curr = [0 for _ in range(m+1)]
            for j in range(1,m+1):
                
                if s[i-1] == t[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr
        
        return prev[m]