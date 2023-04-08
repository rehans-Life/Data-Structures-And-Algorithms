from typing import List
class Solution:
    def partitionKPossible(self,nums,k,maxSum):
        no_of_subarrays = 1
        subarraySum = 0
        for num in nums:
            if (subarraySum + num) > maxSum:
                no_of_subarrays+=1
                subarraySum = num
                if no_of_subarrays > k: return False
            else:
                subarraySum+=num
        return True
    
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        
        res = -1

        while start <= end:
            mid = (start+end) // 2

            if self.partitionKPossible(nums,k,mid):
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res