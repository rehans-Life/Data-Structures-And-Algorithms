class Solution:
    def checkBit(self,n: int,i: int) -> bool:
        mask = 1<<i
        return n if not n&mask else n^mask

solution = Solution()
print(solution.checkBit(13,2))

        