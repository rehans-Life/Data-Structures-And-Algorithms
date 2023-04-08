def orderNotKnown(arr,n,num):
    
    if n == 1:
        return 0
        
    # Setting up two pointers start & end
    start = 0
    end = n -1
    
    # if start is greater than end then that means the array is sorted
    # in descending order because the order is greatest to smallest.
    
    if arr[start] > arr[end]:
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                end = mid-1
            else:
                start = mid+1
    
    # if end is greater than start than that means the array is sorted
    # in increasing order because the order is greater to smallest.
    else:
        while start <= end:
            mid = (start+end) // 2
            
            if arr[mid] == num:
                return mid
            elif arr[mid] < num:
                start = mid+1
            else:
                end = mid-1
    
    return -1

print(orderNotKnown([11],1,11))        

        
        