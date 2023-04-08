def parataPossible(ranks,n,p,mid):
    no_of_paratas = 0
    currTime = 0
    currParatas = 0
    i = 0
   
    while i < n:
       currParatas+=1
       if currTime + currParatas*ranks[i] > mid:
           currParatas=1
           i+=1
           if i < n: 
            currTime = currParatas*ranks[i]
       else:
            currTime+=currParatas*ranks[i]
       no_of_paratas+=1    

    return True if no_of_paratas >= p else False            

def parata(ranks,n,p):
    start = 1
    end = 0     
    res = -1
    
    for i in range(1,p+1):
        end += i*max(ranks)

    while start <= end:
        
        mid = (start+end) // 2
        
        if parataPossible(ranks,n,p,mid):
            res = mid
            end = mid-1
            print(mid)
        else:
            start = mid+1
    
    return res

print(parata([1,2,3,4],4,10))