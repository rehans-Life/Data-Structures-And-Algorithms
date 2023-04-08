def bsInNearlySorted(arr,n,num):
    # Setting up two pointers to denote the range we are searching inside of.
    start = 0
    end = n-1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        # Now in order to check if my middle index is pointing at the element of interest.
        # I need to compare the value with the middle index, with mid+1 and with mid-1.
        # Cause the actual middle index value could be in either of these positions.
        if arr[mid] == num:
            return mid
        elif mid-1 >= 0 and arr[mid-1] == num:
            return mid-1
        elif mid+1 < n and arr[mid+1] == num:
            return mid+1
        # Basic if given number not equal to middle then i check the left or right side on the basis of weather 
        # the given value is greater than or less than middle indexed value
        elif arr[mid] < num:
            start = mid+2
        elif arr[mid] > num:
            end = mid-2
    
    return -1

print(bsInNearlySorted([10, 3, 40, 20, 50, 80, 70],7,10))