def findCeil(arr,n,x):
    # Initializing two pointers to denote our range of search
    start = 0
    end = n-1

    res = -1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            res = mid
            end = mid-1
        else:
            start = mid+1
    
    return res
print(findCeil(list({1, 2, 8, 10, 10, 12, 19}),7,11))