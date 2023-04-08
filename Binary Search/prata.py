def makePPrataPossible(ranks,p,maxTime):
    
    no_of_paratas = 0
    
    for chefRank in ranks:
        
        paratasMade = 1
        timeTaken = chefRank
        
        while True:

            if (timeTaken + ((paratasMade+1)*chefRank)) > maxTime:
                break
            else:
                paratasMade+=1
                timeTaken+=(paratasMade*chefRank)
        
        no_of_paratas+=paratasMade
        
        if no_of_paratas >= p:
            return True
        
    return False 

def parata(ranks,p):
    
    start = min(ranks)
    end = 10000
    res = -1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if makePPrataPossible(ranks,p,mid):
            res = mid
            end = mid-1
        else:
            start = mid+1
             
    return res

print(parata([3,5,2,4,1],13))