def firstOccurence(arr,n,num):
    
    start = 0
    end = n -1
    
    # Which is going to store the 1st occurence
    # of the given element
    res = -1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if arr[mid] == num:
    # After we find the element we store the index
    # in a variable 
            res = mid
    # And since we have to make sure that this index is the index of the
    # first occurence of the character.
    # We need to continue our search on the left side of the array
    # to search for another occurence that exists before the current one
    # that we have found.
            end = mid - 1
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    
    return res
