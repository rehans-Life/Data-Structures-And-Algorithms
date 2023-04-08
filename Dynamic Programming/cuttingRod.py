from math import *

def cutRod(price, n):

    prev = [-1 for _ in range(n+1)]
    
    for target in range(n+1):
        prev[target] = target * price[0]
    
    for i in range(1,n):
        curr = [-1 for _ in range(n+1)]       
        for target in range(n+1):

            pick = price[i] + curr[target-(i+1)] if (i+1) <= target else -inf
            notPick = 0 + prev[target]

            curr[target] = max(pick,notPick)           
        
        prev = curr
    
    return prev[n]


def cutRod(price, n):

    prev = [-1 for _ in range(n+1)]
    
    for target in range(n+1):
        prev[target] = target * price[0]
    
    for i in range(1,n):     
        for target in range(n+1):

            pick = price[i] + prev[target-(i+1)] if (i+1) <= target else -inf
            notPick = 0 + prev[target]

            prev[target] = max(pick,notPick)           
    
    return prev[n]

