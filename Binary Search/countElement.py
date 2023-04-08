def firstOccurance(arr,n,num):
    start = 0 
    end = n-1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == num:
            res = mid
            end = mid-1
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return res    
         

def lastOccurance(arr,n,num):
    start = 0
    end = n - 1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        
        if arr[mid] == num:
            res = mid
            start = mid+1
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1 
    return res   
        
        

def countElement(arr,n,num):
    
    # Will return the index of the first occurance of the given element.
    first = firstOccurance(arr,n,num)
    
    if first == -1: return -1

    # Will return the index of the last occurance of the given element.    
    last = lastOccurance(arr,n,num)
    
    if last == -1: return -1
    
    # Difference between the first and last occurance and adding 1 to the difference will give us the length of section
    # which is contains all instances of the given element.
    freq = (last - first) + 1
    
    return freq   
            
print(countElement([5,12,15,17,17,17,17,20,20],9,20))