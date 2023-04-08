import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        start = 1
        end = max(nums)
        res = -1

        while start <= end:

            mid = (start+end) // 2
            divisorSum = 0

            for num in nums:
                divisorSum+=(math.ceil(num / mid))
            
            if divisorSum <= threshold:
                res = mid
                end = mid-1
            else:
                start = mid+1
            
        return int(res)