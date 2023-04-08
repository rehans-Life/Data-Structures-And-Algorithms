def findMaxBitonic(arr):
    n = len(arr)
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
    

def ascendingBinarySearch(arr,start,end,num):
    while start <= end:
        mid = (start+end) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    
    return -1

def descendingBinarySearch(arr,start,end,num):
    while start <= end:
        
        mid = (start+end) // 2
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            end = mid-1
        else:
            start = mid+1
        
    return -1

def findBitonic(arr,num):
    
    # First im going to find the maximum element in the bitonic
    # array.
    
    # Becuase by doing this i will be able to divide my array into
    # two sections one would be the ascending sorted array 
    # which is basically the monotonious incresing section
    # then there is the descending sorted array which is formed
    # by the monotonous descreasing section.
    
    n = len(arr) 
     
    peakIndex = findMaxBitonic(arr)
    
    indexInDescArray = descendingBinarySearch(arr,peakIndex,(n-1),num)
    
    indexInAscArray = ascendingBinarySearch(arr,0,peakIndex-1,num)
    
    return max(indexInDescArray,indexInAscArray)

arr = [5,10,15,23,25,20,19,17,16,15,1]

print(findBitonic(arr,12))