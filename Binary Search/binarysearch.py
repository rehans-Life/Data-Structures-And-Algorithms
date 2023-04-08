def binarySearch(arr,n,num):
    
    # Setting up two pointers for our range. initially the complete
    # array is in our range of search
    start = 0
    end = n-1
    
    # We wanna end our search if our start exceeds our end cause that means
    # we have finished searching through our array.
    while start <= end:
        # Calcluting the mid value so that we can divide our array
        mid = (start+end) // 2
        
        # If the mid pointer is pointing at the number we are searching
        # for we return the number
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start= mid + 1
        else:
            end = mid-1
            
    return -1    

print(binarySearch([11,15,16,19,24,30,41],7,41))