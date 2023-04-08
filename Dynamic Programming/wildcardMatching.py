class Solution:    
    def isMatch(self, s: str, p: str) -> bool:        
        n = len(p)
        m = len(s)

        prev = [False for _ in range(m+1)]
        prev[0] = True

        for i in range(1,n+1):
            curr = [-1 for _ in range(m+1)]

            for k in range(1,i+1):
                if p[k-1] != '*':
                    curr[0] = False
            
            if curr[0] == -1:
                curr[0] = True

            for j in range(1,m+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    curr[j] = prev[j-1]
                elif p[i-1] == '*':
                    curr[j] = prev[j] or curr[j-1]
                else:
                    curr[j] = False
            
            prev = curr

        return prev[m]