# Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        runningSum = []

        for i in range(len(nums)):
            runningSum.append(sum(nums[0:i+1]))
        
        return runningSum

# Optimal : One Liner

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1,len(nums)): nums[i]+=nums[i-1]
        return nums