def lastOccurence(arr,n,num):
    
    # Initializing the pointers to denote the 
    # start and end of the range in which we are
    # searching in.
    start = 0
    end = n-1
    
    # index of the last occurence of the given 
    # character.
    res = -1
    
    # We wanna stop our iteration after we have completed partioned our
    # array.
    while start <= end:
        
        # Calculating the mid on the basis of we are going to partiton
        # on and check weather if its equal to the given element to search
        mid = (start+end) // 2
        
        if arr[mid] == num:
            # If we have found the element we are looking for then
            # we set our result to that index and we continue our search
            # on the right side from that index cause we need to make 
            # sure we find the last occurence of the element we are 
            # searching for.
            res = mid
            
            start = mid+1
            
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    
    return res
            
print(lastOccurence([2,5,6,10,10,10,16,17],8,10))        