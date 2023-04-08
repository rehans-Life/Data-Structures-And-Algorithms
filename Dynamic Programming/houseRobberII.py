class Solution:
    def helper(self,prev2,prev,start,end,nums):        
        for i in range(start,end):
            curr = max(nums[i] + prev2,prev)
            prev2 = prev
            prev = curr

        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return max(nums)

        max1  = self.helper(0,nums[0],1,n-1,nums)
        max2  = self.helper(0,nums[1],2,n,nums)
        return max(max1,max2)