# Naive Approach

# Time Complexity: O(nlong(n))
# Space Complexity: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Creating a new Array in which each elements of nums
        # is squared
        nums = list(map(lambda x : x*x , nums))

        # Sorting the array
        nums.sort()

        # Returning the answer
        return nums

# Optimal Approach : Two Pointer (cause arrays are sorted)

# Space Complexity: O(n)
# Time Complexity: O(n)

def sortedSquares(nums: list[int]) -> list[int]:
        i = 0
        j = len(nums) - 1
        ans = []

        # We stop the while loop when both the pointers start
        # going in the opposite direction
    
        while i<=j:

            # If the left pointer square value is greater
            # than right pointer square value then we append
            # it its square to the array and increment i
            if pow(nums[i],2) > pow(nums[j],2):
                ans.append(pow(nums[i],2))
                i+=1

            else:
                # If not then right pointer square value
                # is appended and wr increment i.
                ans.append(pow(nums[j],2))
                j-=1

        # Reversing the array to get the right sequence.
        ans.reverse()

        return ans
print(sortedSquares([-4,-1,0,3,10]))