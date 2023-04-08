# Brute Force: 2 Pass Solution.

# Space Complexity: O(1)
# Time Complexity: O(n)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 

        for j in range(0,len(nums)):
            if nums[j] == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1 

        for j in range(i,len(nums)):
            if nums[j] == 1:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1

# Optimal - One Pass Solution

# Space Complexity: O(1)
# Time Complexity: O(n)

# In this solution we move all the twos to the right side of 
# the array which is to the end.

# And we move all the Zeroes to the left side of the array which
# is in the beginning.

# Due to this our 1's automatically come in the middle of the array.

# So we basically have a left pointer at index 0 and a right
# pointer at the last index of the array.

def sortColors(nums: list[int]) -> None:
    
    # We need a left pointer to partition our zeroes to the front
    l = 0

    # We also need a right pointer to partition our twos to the 
    # end
    r = 0

    # Then we need a pointer to iterate through the array
    i = 0

    # Creating a function to swap the values
    def swap(i,j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp


    # A while loop that runs until i pointer goes past the right
    # pointer
    while i <= r:

        # If i is pointing at 0 then we swap its value with the
        # value at the index to which our pointer l is pointing at.
        if nums[i] == 0:
            # Swapping the value at index i with the value at index 
            # to which our pointer l is pointing at
            swap(i,l)

            # Then we increment our l pointer cause the current index
            # is filled with zero now to which our l pointer is currently
            # pointing at
            l += 1

            # We also increment our pointer to continue our iteration
            i += 1

        # If our pointer is pointing at a index with value 1 we skip
        # it cause we are making partition for 0 and 2 we dont care
        # about 1 cause its automatically going to be moved to the middle
        elif nums[i] == 1:
            i += 1

        # Else would be when our pointer is pointing at two so in that
        # case we swap the values with the value at index to which our
        # pointer r is pointing at cause we have to more our two to the 
        # right side
        else:
            swap(i,r)

            # Incrementing the pointer r cause we know the current index
            # to which my pointer r is pointing at has a two so we wanna
            # point at another index which doesnt have two in it.
            r += 1

            # Notice we dont increment i cause we want to be able to 
            # check the value that i index stores after swapping from
            # the right pointer's index.