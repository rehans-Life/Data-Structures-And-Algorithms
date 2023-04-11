class Solution:
    def nonRepeating(self,arr):
        xor = 0
        for num in arr: xor^=num
        return xor

arr = [3,5,2,3,5,2,9]
solution = Solution()
print(solution.nonRepeating(arr))

        