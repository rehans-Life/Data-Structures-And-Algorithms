# Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                            ans+=1
        return ans

# Optimal 

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        visited = dict()
        good_pairs = 0
        for num in nums:
            if num in visited:
                good_pairs+=visited[num]
                visited[num]+= 1
            else:
                visited[num] = 1
        return good_pairs