from typing import List

def shippingPossible(weights,days,capacity):

    no_of_days = 1
    weightsAssigned = 0
    
    for productWeight in weights:
        if weightsAssigned+productWeight > capacity:
            no_of_days+=1
            weightsAssigned = productWeight
            if no_of_days > days:
                return False
        else:
            weightsAssigned+=1
    
    return True             
    

def shipWithinDays(weights: List[int], days: int) -> int:
    
    start = max(weights)
    end = sum(weights)
    
    res = -1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if shippingPossible(weights,days,mid):
            res = mid
            end = mid-1
        else:
            start = mid+1
    
    return res