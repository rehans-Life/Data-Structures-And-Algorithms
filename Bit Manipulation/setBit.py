class Solution:
    def checkBit(self,n: int,i: int) -> bool:
        return n|(1<<i)

solution = Solution()
print(solution.checkBit(12,0))

        