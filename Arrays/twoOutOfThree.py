# Brute Force

# Space Complexity: O(n)
# Time Complexcity: O(n^2)

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        
        ans = set()

        for num in nums1:

            if num in nums2:
                ans.add(num)
            
            elif num in nums3:
                ans.add(num)
        
        for num in nums2:

            if num in nums3:
                ans.add(num)

        return list(ans)

print(min([4,3,23]))