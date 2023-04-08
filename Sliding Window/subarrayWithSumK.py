# Given an array nums find the length of the longest subarray with length k.

def longestSumK(nums,k):
    
    n = len(nums)
    
    # Initializing the i and j pointers for my window
    i,j=0,0
    
    # Variable which is going to store my current subarrays sum
    subarraySum = nums[0]
    
    # A variable which is going to store the length of the longest subarray 
    # at different intervals.
    maxSubarray = 0
    
    while j < n:
                
        if subarraySum < k:
            j+=1
        
        elif subarraySum == k:
            maxSubarray = max(maxSubarray,(j-i+1))
            subarraySum-=nums[i]
            i+=1
            j+=1
        
        else:
            subarraySum-=nums[i]
            i+=1
            continue
            
        if j < n: subarraySum+=nums[j]
            
    return maxSubarray

# print(longestSumK([5,2,2,4,1,6,3,4,2],9))
print(len('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'))