def allocatingPossible(stalls,k,mid):
    cows = 1
    currCowPosition = stalls[0]
    
    for i in range(1,len(stalls)):
        if abs(currCowPosition - stalls[i]) >= mid: 
            cows+=1
            currCowPosition = stalls[i]
        if cows == k:
            return True
    return False

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    start = 1
    end = max(stalls) - min(stalls)
    
    res = -1
    
    while start <= end:
        mid = (start+end) // 2
        
        if allocatingPossible(stalls,k,mid):
            res = mid
            start = mid+1
        else:
            end = mid-1
    
    return res