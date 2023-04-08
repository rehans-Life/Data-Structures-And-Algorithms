# Brute Force 

# Space Complexity: O(1)
# Time Complexity: O(n^3)

import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -math.inf

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subArray = nums[i:j+1]
                maxSum = max(maxSum,sum(subArray))
        
        return maxSum

# Better Approach

# Space Complexity: O(1)
# Time Complexity: O(n^2)

# Reducing one of the loops by not computing the value of each subArray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -math.inf
        for i in range(len(nums)):
            currSum = 0
            for j in range(i,len(nums)):
                currSum+=nums[j]
                maxSum = max(maxSum,currSum)
        
        return maxSum

# Kadane's Algorithm

# Space Complexity: O(1)
# Time Complexity: O(n)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = nums[0]
        currSum = 0

        for num in nums:
            
            currSum+=num
            
            maxSum = max(maxSum,currSum)

            if currSum < 0:
                currSum = 0
        
        return maxSum