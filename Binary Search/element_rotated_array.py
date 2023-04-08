def minimumElementInArray(arr,n):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start+end) // 2
        
        left = (mid+n-1) % n
        right = (mid+1) % n
        
        if arr[left] > arr[mid] and arr[right] > arr[mid]:
            return mid

        if arr[end] <= arr[mid]:
            start = mid+1
        else:
            end = end-1

def bs(arr,start,end,num):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return -1

def elementInRotatedArray(arr,n,num):
    
    minimumIndex = minimumElementInArray(arr,n)
    
    # Applying binary search on the left sorted section
    # section of the array in search of the given element.
    bsInLeftSortedArray = bs(arr,0,minimumIndex-1,num)
    
    # Applying binary search on the right sorted section
    # of the array in search of the given element.
    bsInRightSortedArray = bs(arr,minimumIndex,n-1,num)
    
    return max(bsInLeftSortedArray,bsInRightSortedArray)