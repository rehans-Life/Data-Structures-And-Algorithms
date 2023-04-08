# Brute Force

# Space Complexity: O(1)
# Time Complexity: O(n^2)

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        while sum(nums) != 0:
            smallest = min(filter(lambda x : x != 0 ,nums))
            nums = list(map(lambda x: (x - smallest) if x != 0 else x,nums))
            operations+=1
        return operations

# Same as Brute Force But Clean

import math

# Space Complexity: O(1)
# Time Complexity: O(n^2)

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        operations = 0

        while sum(nums):
            smallest = math.inf

            for num in nums:
                if num: 
                    smallest = min(num,smallest)                    

            nums = [num-smallest if num != 0 else num for num in nums] 

            operations+=1
        
        return operations