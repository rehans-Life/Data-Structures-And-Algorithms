import math
def maxKSizeSubarray(arr,k):
    
    n = len(arr)
    
    # Initializing two pointers which are going to denote
    # the size of our window
    i,j=0,0
    
    # A variable which is going to store the maxSum of subArray
    # whose size is k
    maxSum = - math.inf
    
    # A variable which is going to maintain the current subArrays
    # sum whose size is k
    subarraySum = 0
    
    # We are going to run a while loop as long as j pointer is within
    # the array cause if it goes outside then that means we have
    # ran out elements to create more windows of given size k
    while j < n:
        
        # Including our jth element in our subarray sum
        subarraySum+=arr[j]
        
        # We keep incrementing j until our window size is equal to
        # k
        if (j-i+1) < k:
            j+=1
            
        # When length of subarray is equal to k then we check if
        # its sum is the largest we have found up until now.
        elif (j-i+1) == k:
            maxSum = max(maxSum,subarraySum)
            # Then we move our window to the next subArray
            subarraySum-=arr[i]         
            i+=1
            j+=1
        
    return maxSum

print(maxKSizeSubarray([100, 200, 300, 400],2))