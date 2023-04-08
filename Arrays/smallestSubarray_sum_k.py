# Brute Force

# Space Complexity: O(1)
# Time Complexity: O(n^2)

import math
class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        smallestSubarrayLength = math.inf
        
        for i in range(n):
            currSum = 0
            for j in range(i,n):
                currSum+=a[j]
                if currSum > x:
                    smallestSubarrayLength = min(smallestSubarrayLength,((j+1)-i))
        
        return smallestSubarrayLength
    
# Optimal

# Space Complexity: O(1)
# Time Complexity: O(n)
from typing import List
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        currSum = nums[0]
        smallest = math.inf

        while j < n:
            length = j+1-i
            if length == smallest:
                currSum-=nums[i]
                i+=1
                continue
            if currSum >= target:
                smallest = min(smallest,length)
                currSum-=nums[i]
                i+=1
            else:
                j+=1
                if j < n:
                    currSum+=nums[j]
        return smallest if smallest != math.inf else 0
    