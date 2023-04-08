import math
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxProduct = -math.inf
        n = len(nums)

        for i in range(n):
            currProduct= 1
            for j in range(i,n):
                currProduct*=nums[j]
                maxProduct=max(maxProduct,currProduct)
        
        return maxProduct

import math
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        # We are going to have to maintain the min and max products of subArrays starting from an 
        # element so that we are able to compute the max product of subArray starting from next
        # consecutive element
        currMin = 1
        currMax = 1

        # MaxProduct which is going to store the maximum product of subArray made from starting of an
        # element.
        maxProduct = max(nums)

        for num in nums:

            temp = num*currMax

            currMax = max(num * currMin, num * currMax, num)
            currMin = min(num*currMin, temp, num)

            maxProduct = max(maxProduct,currMax)

        return maxProduct