# In this question you are given a binary infinite sorted array so a sorted array full of 1's and 0's. 
# so its looks something like this: 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1...........................INFINITY AND BEYOND

def firstOccurence(arr,start,end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == 1:
            res = mid
            end = mid-1
        else:
            start = mid+1
    
    return res 

def binarySortedArray(arr):
    
    # Initializing two pointers which are going to point towards the range wihtin which 1 actually exists
    # inside of.
    start = 0
    end = 1
    
    # Im going to keep creating ranges in forward direction until i find the one which has 1 inside of it each range that i create
    # is going to be of double the size of its previous one so that i can keep on increasing my chances of finding one.
    while 1 > arr[end]:
        start = end
        end*=2
        
    # I need to implement a binary search to find the first occurence of 1 inside of my range.
    # and return its index.
    return firstOccurence(arr,start,end)

print(binarySortedArray([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]))