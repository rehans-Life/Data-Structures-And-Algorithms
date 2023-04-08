# You are given a Bitonic Array and you need to find its maximum
# element - A bitonic array is an array that monotonoically increases
# and then monotically decreases.

# Monotically increases means its increasing without any duplicate
# elements

# 3,4,5,6,7,8,9,10 => Is monotically inceasing cause there are 
# no repreating elements in this increasing order

# 3,4,4,5,6,7 => This is not monotically increasing cause
# there are repeating elements in this increasing order.

# Similar concept applied to monotically decreasing as well.

def findMaxBitonic(arr,n):
    
    # Setting up two pointers which are going to denote the range
    # of our search
    start = 0
    end = n-1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        if mid > 0 and mid < n-1:
            
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                end = mid-1
            elif arr[mid+1] > arr[mid]:
                start = mid+1
        
        elif mid == 0:
            
            if arr[mid] > arr[mid+1]:
                return mid
            else:
                start = mid+1
                
        elif mid == (n-1):
            
            if arr[mid] > arr[mid-1]:
                return mid
            else:
                end = mid-1
                
                
            