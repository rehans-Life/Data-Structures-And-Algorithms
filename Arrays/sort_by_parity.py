# Optimal

# Space Complexity: O(1)
# Time Complexity: O(n)

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # Our left pointer starting from the left side.
        i = 0

        # Our Right pointer starting from the right side.
        j = len(nums) - 1

        # While loop which is going to run until the left and right pointer cross each other
        while i <= j:

            # If i is pointing at a even number we move to the next element directly cause 
            # there is no need to remove an even number from the left side.
            if nums[i] % 2 == 0:
                i+=1
                continue
            
            # If j is pointing at a odd number we move it to the next element directly again
            # cause there is no need move an odd number from the right side.
            if nums[j] % 2 != 0:
                j-=1
                continue
            
            # If j is pointing at a even number and i is pointing at a odd number
            # we switch their values.
            if nums[j] % 2 == 0 and nums[i] % 2 != 0:
                
                # Switching the values.
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

                # Moving both the pointers to compare next elements
                i+=1
                j-=1
        
        return nums

# Optimal 2

# Space Complexity: O(1)
# Time Complexity: O(n)

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0

        for j,num in enumerate(nums):

            if num % 2 == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1

        return num
    