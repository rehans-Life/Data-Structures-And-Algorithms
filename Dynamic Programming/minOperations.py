from os import *
from sys import *
from collections import *
from math import *

def canYouMake(s: str, p: str) -> int:
        n = len(s)
        m = len(p)

        prev = [0 for _ in range(m+1)]
        
        for i in range(1,n+1):
            curr = [0 for _ in range(m+1)]
            
            for j in range(1,m+1):
                
                if s[i-1] == p[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])

            prev = curr

        return n + m - (2 * prev[m])